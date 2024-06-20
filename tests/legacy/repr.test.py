import json
import base64
import inspect

def prep_repr(category, type, *, name=None, **kwargs):
    result = {'category': category, 'type': type}
    if name:
        result['name'] = name
    return result.update(kwargs)

class FuncWrapper(object):
    def __init__(self, f):
        self.f = f.f if isinstance(f, FuncWrapper) else f

    def __call__(self, *args, **kw): return self.f(*args, **kw)
    
    def prep_repr(self):
        result = prep_repr('Function',self.f.__name__.strip('<>'))
        # so we don't have to consider code transfer.
        return result

    def __repr__(self):
        repr = self.prep_repr()
        return json.dumps(repr)

test_func = lambda ctx, query: dict(context_str=ctx, query_str=query)
    
print(FuncWrapper(test_func))