# -*- coding: utf-8 -*-
# @Time    : 2024/7/8 21:45
# @Author  : nongbin
# @FileName: llm_api_request.py
# @Software: PyCharm
# @Affiliation: tfswufe.edu.cn
import os
from typing import Optional, List, Union, Annotated, Dict, Any

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from volcenginesdkarkruntime import Ark


class Message(BaseModel):
    role: str = Field(..., exclude=False)
    content: str = Field(..., exclude=False)


class ResponseFormat(BaseModel):
    type_: str


class ToolChoice(BaseModel):
    type: str
    function: Optional[dict]


class ChatRequest(BaseModel):
    messages: List[Message]
    model: str
    frequency_penalty: Optional[float] = 0
    logit_bias: Optional[dict] = None
    logprobs: Optional[Union[bool, None]] = False
    top_logprobs: Optional[Union[int, None]] = None
    max_tokens: Optional[Union[int, None]] = None
    n: Optional[Union[int, None]] = 1
    presence_penalty: Optional[float] = 0
    response_format: Optional[ResponseFormat] = None
    seed: Optional[Union[int, None]] = None
    stop: Optional[Union[str, List[str], None]] = None
    stream: Optional[Union[bool, None]] = False
    stream_options: Optional[Any] = None
    temperature: Optional[float] = 0.95
    top_p: Optional[float] = 1
    tools: Optional[List[Dict]] = None
    tool_choice: Optional[Union[str, ToolChoice]] = None
    user: Optional[str] = None

app = FastAPI()
