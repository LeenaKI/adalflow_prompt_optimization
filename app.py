import streamlit as st
import adalflow as adal
from adalflow.components.model_client.google_client import GoogleGenAIClient
from adalflow.optim.types import ParameterType

class PromptOptimizationPipeline(adal.Component):
    def __init__(self, model_client: adal.ModelClient, model_kwargs: dict):
        super().__init__()
        self.system_prompt = adal.Parameter(
            data=(
                "You are an expert in prompt optimization. Your task is to rewrite the given user prompt to make it more "
                "detailed, structured, and effective for AI models. Ensure clarity and that the intent of the original prompt "
                "is preserved."
            ),
            role_desc="Provides instructions for the AI to perform prompt optimization",
            requires_opt=True,
            param_type=ParameterType.PROMPT,
        )
        self.prompt_optimizer = adal.Generator(
            model_client=model_client,
            model_kwargs=model_kwargs,
            template="{{system_prompt}}\n\nUser Prompt: {{input_prompt}}\n\nOptimized Prompt:",
            prompt_kwargs={
                "system_prompt": self.system_prompt,
            },
            use_cache=False,
        )

    def call(self, user_prompt: str) -> str:
        output = self.prompt_optimizer(prompt_kwargs={"input_prompt": user_prompt})
        return output.data

st.title("Adalflow Prompt Optimization with Gemini")

# API Key Input
api_key = st.text_input("Enter your Google API Key:", type="password")

if api_key:
    # Initialize Google Gemini Client with user-provided API key
    gemini_model = {
        "model_client": GoogleGenAIClient(api_key=api_key),
        "model_kwargs": {
            "model": "gemini-1.5-flash",   
            "max_output_tokens": 4000,     
            "temperature": 0.0,          
            "top_p": 0.95,                 
            "stop_sequences": None,       
        },
    }

    prompt_optimizer = PromptOptimizationPipeline(**gemini_model)

    # User Input Section
    user_prompt = st.text_area("Enter your custom prompt:")

    # Button to generate optimized prompt
    if st.button("Optimize Prompt"):
        try:
            optimized_prompt = prompt_optimizer(user_prompt)
            st.success("Optimized Prompt:")
            st.write(optimized_prompt)
        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.warning("Please enter your Google API key to proceed.")
