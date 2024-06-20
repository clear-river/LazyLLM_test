import lazyllm
from lazyllm import pipeline, _0
from lazyllm.flow import Parallel
from lazyllm import TrainableModule
from lazyllm.tools import Reranker, Retriever
from lazyllm.tools import Document

documents = Document(dataset_path='/file/to/yourpath', embed=TrainableModule('bge-large-zh-v1.5'))
with pipeline() as ppl:
    with Parallel().sum as ppl.prl:
        prl.retriever1 = Retriever(documents, parser='CoarseChunk', similarity_top_k=6)
        prl.retriever2 = Retriever(documents, parser='SentenceDivider', similarity='chinese_bm25', similarity_top_k=6)
    ppl.reranker = Reranker(types='ModuleReranker', model='bge-reranker-large') | bind(ppl.input, _0)
    ppl.top1 = lambda nodes: f'《{nodes[0].metadata["file_name"].split(".")[0]}》{nodes[0].get_content()}' if len(nodes) > 0 else '未找到'
    ppl.formatter = (lambda ctx, query: dict(context_str=ctx, query_str=query)) | bind(query=ppl.input)
    ppl.llm = lazyllm.TrainableModule('internlm2-chat-7b').prompt(lazyllm.ChatPrompter('你将扮演一个人工智能问答助手的角色，完成一项对话任务。在这个任务中，你需要根据给定的上下文以及问题，给出你的回答。', extro_keys=['context_str'])) 
mweb = lazyllm.WebModule(ppl, port=23456).start().wait()