from pydantic import BaseModel,Field
from typing import Dict,Any
from typing_extensions import TypedDict,list
from langgraph.graph.message import add_messsages

class State(TypedDict):
    message:Annotated[list,add_messages]