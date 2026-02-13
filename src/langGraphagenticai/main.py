import streamlit as st 
from src.langGraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAi application with StreamLit UI
    this function initailaizes the UI, ahndles user inpu, configures the LLM Model.
    sets up the graph based on the selected use case , and displays the output while
    implementing excepton handling for robustness.
    """
    
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlitui()
    
    if not user_input:
        st.error("Failed to load user input. Please check the UI configuration.")
        return
    
    user_message=st.chat_input("Enter your message here:")
    
    """if user_message:
        try:
            obj_llm_config=GroqLLM(user_controls_input=user_input)
            model=obj_llm_config.get_llm_model()
            """