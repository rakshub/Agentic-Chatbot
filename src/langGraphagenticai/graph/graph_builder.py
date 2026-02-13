from langgraph.graph import StateGraph
from src.langGraphagenticai.state.state import State
from langgraph.graph import START,END   

class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph=StateGraph(State)
        
    def basic_chatbot_build_graph(self):
        #self.basic_chatbot=State()
        
        self.graph.add_node("chatbot","")
        self.graph.add_edge(START,"chatbot")
        self.graph.add_edge("chatbot",END)
        