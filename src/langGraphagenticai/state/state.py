from pydantic import BaseModel,Field
from typing import Dict,Any,Annotated
from typing_extensions import TypedDict,List
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages:Annotated[List[Dict[str,Any]],add_messages]