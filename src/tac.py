from collections import defaultdict
from prs import ASTExpr, Bin, Lit, Ref
import prs
from enum import Enum

class Type(Enum): 
    Decl = 1
    Math = 2

class Tac: 
    def __repr__(self): 
        if self.type == Type.Decl: return f"{self.name} = {self.l}"
        elif self.type == Type.Math: return f"{self.name} = {self.l} {self.op} {self.r}"
        return None
    def __init__(self, type, name, l = None, op = None, r = None): 
        self.type = type
        self.name = name
        self.l = l
        self.op = op
        self.r = r

def postorder_dfs(node: Bin | Lit | Ref, tac_map: defaultdict[list], col = 0, row = 0):
    if node.type != prs.Type.Bin: return node.value
    l = postorder_dfs(node.l, tac_map, col    , row + 1)
    r = postorder_dfs(node.r, tac_map, col + 1, row + 1)
    key = "R" + str(row) + "_C" + str(col)
    tac_map[key].append((l, node.op, r))
    return key

def parse_node(node: ASTExpr) -> str: 
    tacs = []
    if node.value.type == prs.Type.Bin:
        tac_map = defaultdict(list)
        postorder_dfs(node.value, tac_map)
        for i,key in enumerate(tac_map):
            counter = 1
            for tac in tac_map[key]: 
                name = f"{key}" if i < len(tac_map) - 1 else node.name
                counter += 1
                # tacs.append(f"{name} = {tac[0]} {tac[1]} {tac[2]}")
                tacs.append(Tac(Type.Math, name, tac[0], tac[1], tac[2]))
    elif node.value.type == prs.Type.Lit:
        tacs.append(Tac(Type.Decl, node.name, node.value.value))
    return tacs

def run(*,nodes: list[ASTExpr]): return [x for node in nodes for x in parse_node(node)]