import logging
import sys
import os
from llama_index import GPTSimpleVectorIndex, GPTListIndex, GPTTreeIndex, SimpleDirectoryReader, LLMPredictor
from llama_index import download_loader
from pathlib import Path
from langchain import OpenAI


os.environ['OPENAI_API_KEY'] = "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"

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="gpt-3.5-turbo", max_tokens=1300))

# BilibiliTranscriptReader = download_loader("BilibiliTranscriptReader")
# PDFReader = download_loader("PDFReader")
CJKPDFReader = download_loader("CJKPDFReader")


loader = CJKPDFReader()
# documents = loader.load_data(video_urls=['https://www.bilibili.com/video/BV1KK4y1P7Df/'])
documents = loader.load_data(file=Path('/Users/moss/Desktop/aliyun.pdf'))
# documents = SimpleDirectoryReader('data').load_data()
print(documents)
# index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor)

index = GPTSimpleVectorIndex.load_from_disk('index.json')
# index.save_to_disk('index.json')

# response = index.query("What is a summary of this collection of text? Answer in Chinese", response_mode="tree_summarize")
# response = index.query("用中文详细总结全文并给出重点列表", response_mode="tree_summarize")
response = index.query("什么是数字化运营体系的核心三要素？")
print(response)
