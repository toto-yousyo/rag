import json
import logging
import os
import os
import re
import time
from datatime import timedelta
from typing import Any

from add_document import initialize_vectorstore
from dotenv import load_dotenv
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory, MomentoChatMessageHistory
from langchain.schema import HumanMessage, LLMResult, SystemMessage
from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler
from slack_bolt.adapter.socket_mode import SocketModeHandler

CHAT_UPDATE_INTERVAL_SEC = 1

load_dotenv()

# logging
SlackRequestHandler.clear_all_log_handlers()
logging.basicConfig(format="%(asctime)s [%(levelname)%]")
