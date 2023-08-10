from langchain.llms import CTransformers

print('Loading LLAMA model...')
llm = CTransformers(
    model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
    model_type='llama',
    config={
        'max_new_tokens': 100,
        'temperature': 0.01
    }
)

print('Generating text...')
import time
start = time.time()
print(llm("AI is going to"))
print('Time taken: {time.time() - start}.')