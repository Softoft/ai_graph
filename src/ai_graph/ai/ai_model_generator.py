import pydantic
from openai.types.chat import ParsedChatCompletion

from src.ai_graph.ai.base_ai_config import OpenAIModelVersion
from src.ai_graph.ai.base_ai_model import BaseAIModel
from src.ai_graph.ai.model_describer import ModelDescriber
from src.ai_graph.ai.open_ai_client import OpenAiClient


class AIModelGenerator[OM: BaseAIModel](BaseAIModel):
    def __init__(self, assistant_name: str, client: OpenAiClient, open_ai_model_version: OpenAIModelVersion,
                 temperature: float,
                 max_tokens: int, instructions: str,
                 input_describer: ModelDescriber,
                 retry_wait_min: int = 4, retry_wait_max: int = 128, retry_attempts: int = 20):
        """
        AIModelGenerator is responsible for generating AI models based on a given configuration.

        :param assistant_name: The name of the assistant using this model.
        :param client: The OpenAI client used for generating completions.
        :param open_ai_model_version: The version of the OpenAI model being used.
        :param temperature: The temperature setting for the model (affects randomness).
        :param max_tokens: The maximum number of tokens to generate.
        :param instructions: Instructions for the AI model.
        :param input_describer: A describer for generating the model's input prompts.
        :param retry_wait_min: Minimum wait time between retries in case of failure.
        :param retry_wait_max: Maximum wait time between retries in case of failure.
        :param retry_attempts: Number of retry attempts in case of failure.
        """
        super().__init__(assistant_name=assistant_name, client=client, model=open_ai_model_version,
                         temperature=temperature, max_tokens=max_tokens, instructions=instructions,
                         retry_wait_min=retry_wait_min, retry_wait_max=retry_wait_max, retry_attempts=retry_attempts,
                         input_describer=input_describer)

    async def _get_chat_completion(self, input_instance, output_type: type[pydantic.BaseModel], *args,
                                   **kwargs) -> ParsedChatCompletion:
        """
        Generates a chat completion based on the input instance.

        :param input_instance: The input data to generate the prompt.
        :param output_type: The expected output type for the completion.
        :return: A parsed chat completion response.
        """
        prompt = self._input_describer.generate_description(input_instance)
        return await self._client.get_parsed_chat_completion(prompt=prompt,
                                                             model_version=self._model.get_model_version(),
                                                             temperature=self._temperature,
                                                             max_tokens=self._max_tokens,
                                                             instruction=self._instructions,
                                                             response_format=output_type)

    async def get_parsed_completion(self, input_instance: pydantic.BaseModel, output_type: type[pydantic.BaseModel],
                                    *args, **kwargs) -> OM:
        """
        Returns the parsed completion result based on the input instance.

        :param input_instance: The input data to generate the completion.
        :param output_type: The expected output type for the completion.
        :return: The generated output object.
        """
        return (await self._get_chat_completion(input_instance, output_type, *args, **kwargs)).choices[0].message.parsed
