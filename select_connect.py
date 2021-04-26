# code snippet
# selects all vertices connected to currently selected verts
# mesh should be in edit mode, but no checks are done at all
# run this from the text editor

import bpy
import bmesh

C = bpy.context

bm = bmesh.from_edit_mesh(C.object.data)

to_visit = []

for v in bm.verts:
    v.tag = False
    if v.select :
        to_visit.append(v)

while to_visit:
    v = to_visit.pop()
    if v.tag : continue
    v.tag = True
    for e in v.link_edges:
        v2 = e.other_vert(v)
        if not v2.tag :
            v2.select = True
            to_visit.append(v2)

bmesh.update_edit_mesh(C.object.data)
