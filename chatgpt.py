import os
import sys

import openai
from langchain_community.chains import ConversationalChain
from langchain_community.chat_models import ChatOpenAI
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.indexes import VectorstoreIndexCreator
from langchain_community.indexes.vectorstore import VectorStoreIndexWrapper
from langchain_community.llms import OpenAI
from langchain_community.vectorstores import Chroma

import constants

os.environ["OPENAI_API_KEY"] = constants.APIKEY

query = sys.argv[1]
print(query)
