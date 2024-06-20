import lazyllm

def action_func(x, *, ori):
    return f'action({x})'

def m3_post(x):
    return f'post3({x})'

m = lazyllm.module.TrainableModule().finetune_method(lazyllm.finetune.dummy)\
    .deploy_method(lazyllm.deploy.dummy).mode('finetune')
m.name='m'
m2 = lazyllm.ServerModule(m)
m2.name='m2'
m3 = lazyllm.ServerModule(m2, post=m3_post)
m3.name='m3'
m3.evalset([1])

a1 = lazyllm.ActionModule(action_func)
a1.name='a1'

c = lazyllm.ResultCollector()

ppl = lazyllm.pipeline(
    gendata=lambda x: dict(input=x, background='back'),
    action=a1,
    module=m3,
    coll2=c('result')
)

print(ppl)


# m2.update()
# m2.eval_result

# import xml.etree.ElementTree as ET

# obj_desc='''<Module type=Server stream=False return_trace=False>
#     <Module type=Trainable mode=finetune basemodel= target= stream=False return_trace=False></Module>
# </Module>'''

# root = ET.fromstring(obj_desc)
