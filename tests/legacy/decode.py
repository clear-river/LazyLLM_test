import xml.etree.ElementTree as ET

xml_string='''
<Flow type="Pipeline" items="['gendata', 'action', 'module', 'coll2']">
    <Function type="lambda" code="ICAgIGdlbmRhdGE9bGFtYmRhIHg6IGRpY3QoaW5wdXQ9eCwgYmFja2dyb3VuZD0nYmFjaycpLAo="></Function>
    <Module type="Action" name="a1" return_trace="False" sub-category="Flow" type="Pipeline" items="[]">
        <Function type="action_func" code="ZGVmIGFjdGlvbl9mdW5jKHgsICosIG9yaSk6CiAgICByZXR1cm4gZidhY3Rpb24oe3h9KScK"></Function>
    </Module>
    <Module type="Server" name="m3" stream=False return_trace=False pre="None" post=<Function type=m3_post code=ZGVmIG0zX3Bvc3QoeCk6CiAgICByZXR1cm4gZidwb3N0Myh7eH0pJwo=></Function>>
        <Module type=Server name=m2 stream=False return_trace=False pre=None post=None>
            <Module type=Trainable name=m mode=finetune basemodel= target= stream=False return_trace=False></Module>
        </Module>
    </Module>
    <Common type=ResultCollector name=result value={}></Common>
</Flow>'''

root=ET.fromstring(xml_string)