import ast
from ast import *
from ast_decompiler import decompile


def handle_names(names, file):
    out = []

    for name in names:
        if file:
            if name.asname:
                out.append(f'"./{name.name}.js" as {name.asname}')
            else:
                out.append(f'"./{name.name}.js"')
        else:
            if name.asname:
                out.append(f'{name.name} as {name.asname}')
            else:
                out.append(f'{name.name}')

    return ', '.join(out)


def create_raw_js(out):
    return Expr(value=Call(
        func=Name(id='RawJS', ctx=Load()), args=[Str(s=out)], keywords=[]))


class RewriteImport(ast.NodeTransformer):
    def visit_Import(self, node):
        return create_raw_js('import ' + handle_names(node.names, True))

    def visit_ImportFrom(self, node):
        return create_raw_js('import ' + handle_names(node.names, False) +
                             f' from "./{node.module}.js"')

    def visit_Call(self, node):
        if isinstance(node.func, Name) and node.func.id == 'export':
            return create_raw_js(f'export default {node.args[0].id}')
        else:
            return node


def imports2raw(expr):
    p = ast.parse(expr)
    rw = RewriteImport()
    r = rw.visit(p)
    return decompile(r)
