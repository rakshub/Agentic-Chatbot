import streamlit as st 
from src.langGraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langGraphagenticai.LLMs.groqLLM import GroqLLM
from src.langGraphagenticai.graph.graph_builder import GraphBuilder
from src.langGraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit
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
    
    if user_message:
        try:
            obj_llm_config=GroqLLM(user_controls_input=user_input)
            model=obj_llm_config.get_llm_model()
            if not model:
                st.error("Failed to initialize the LLM model. Please check the configuration.")
                return
            usecase=user_input.get("selected_usecase")
            if not usecase:
                st.error("Failed to determine the selected use case.")
                return
            
            graph_builder=GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error setting up the graph: {str(e)}")
                return
            state={"messages":[user_message]}
        except Exception as e:
            st.error(f"Error initializing the application: {str(e)}")
            return