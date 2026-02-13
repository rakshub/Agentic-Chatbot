from langgraph.graph import StateGraph
from src.langGraphagenticai.state.state import State
from langgraph.graph import START,END   
from src.langGraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph=StateGraph(State)
        
    def basic_chatbot_build_graph(self):
        self.basic_chatbot=BasicChatbotNode(self.llm)
        
        self.graph.add_node("chatbot",self.basic_chatbot.process)
        self.graph.add_edge(START,"chatbot")
        self.graph.add_edge("chatbot",END)
        
        
    def setup_graph(self,usecase):
        if usecase=="basic_chatbot":
            self.basic_chatbot_build_graph()
        return self.graph_builder.compile()