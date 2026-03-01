from langgraph.graph import StateGraph
from src.langGraphagenticai.state.state import State
from langgraph.graph import START,END   
from src.langGraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langGraphagenticai.tools.search_tool import get_tools,create_tool_node
from langgraph.prebuilt import ToolNode,tools_condition
from src.langGraphagenticai.nodes.chatbot_with_tools_node import ChatbotWithToolsNode
class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph=StateGraph(State)
        
    def basic_chatbot_build_graph(self):
        self.basic_chatbot=BasicChatbotNode(self.llm)
        
        self.graph.add_node("chatbot",self.basic_chatbot.process)
        self.graph.add_edge(START,"chatbot")
        self.graph.add_edge("chatbot",END)
    
    def chatbot_with_tools_build_graph(self):
        tools=get_tools()
        tool_node=create_tool_node(tools)
        llm=self.llm
        
        obj_chatbot_with_node=ChatbotWithToolsNode(llm)
        chatbot_node=obj_chatbot_with_node.create_chatbot(tools)
        
        self.graph.add_node("chatbot",chatbot_node)
        self.graph.add_edge("tools",tool_node)
        self.graph.add_edge(START,"chatbot")
        self.graph.add_conditional_edges("chatbot",tools_condition)
        self.graph.add_edge("tools","chatbot")
        self.graph.add_edge("chatbot",END)
        
    def setup_graph(self,usecase):
        if usecase=="Basic Chatbot":
            self.basic_chatbot_build_graph()
        if usecase=="ChatBot with Web":
            self.chatbot_with_tools_build_graph()
        return self.graph.compile()