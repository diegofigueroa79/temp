from langchain.prompts.prompt import PromptTemplate
import boto3


TEMPLATE = """
I am providing two RDF graphs. Please combine the two RDF graphs into one RDF graph.
Only provide the final graph in the output, no description needed.

Graph 1:

{graph1}

Graph 2:

{graph2}
"""

def connect_bedrock():
	boto_session = boto3.Session()
    aws_region = boto_session.region_name
    bedrock_runtime = boto_session.client("bedrock-runtime", region_name=aws_region)
    
    modelId = "meta.llama2-70b-chat-v1"
    
    llm = Bedrock(model_id=modelId, client=bedrock_runtime, model_kwargs={"temperature": 0})
	return llm

def construct_prompt(graph1, graph2):
	prompt = PromptTemplate(
		input_variables=["graph1", "graph2"],
		template=TEMPLATE
	)
	prompt.format(graph1=graph1, graph2=graph2)
	return prompt

def parse_response(response):
    return joined_graph

def join_graphs(graph1, graph2):
	llm = connect_bedrock()
	prompt = construct_prompt(graph1, graph2)
	response = llm(prompt)
	joined_graph = parse_response(response)
	return joined_graph

