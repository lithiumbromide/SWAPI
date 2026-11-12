---
title: "ModelDoc::InsertMfDraft"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertMfDraft.htm"
---

# ModelDoc::InsertMfDraft

This method is obsolete and has been superseded by [ModelDoc::InsertMfDraft2](ModelDoc__InsertMfDraft2.htm).

Description

This method creates a multiface draft.

Syntax (OLE Automation)

void ModelDoc.InsertMfDraft ( angle, flipDir, isEdgeDraft, propType)

| Input: | (double) angle | Draft angle in radians |
| --- | --- | --- |
| Input: | (BOOL) flipDir | Flip the direction of the draft; the draft direction is determined by the selected direction which could be a planar face, a reference plane, an edge, or two vertices; if you refer to the last argument in SelectByMark and AndSelectByMark, these items would have a selection mark of 1; the faces to be drafted have a selection mark of 2 and the draft edges have a selection mark of 4 |
| Input: | (BOOL) isEdgeDraft | Determine if it is an edge or neutral plane draft; TRUE if this will be an edge draft and the user will select edges to be drafted, FALSE if this is to be a face draft and the user will select faces to be drafted (the system will automatically select the faces next to the edge to be drafted) |
| Input: | (long) propType | Propagation type |

Syntax (COM)

status = ModelDoc->InsertMfDraft ( angle, flipDir, isEdgeDraft, propType )

| Input: | (double) angle | Draft angle in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flipDir | Flip the direction of the draft; the draft direction is determined by the selected direction which could be a planar face, a reference plane, an edge, or two vertices; if you refer to the last argument in SelectByMark and AndSelectByMark, these items would have a selection mark of 1; the faces to be drafted have a selection mark of 2 and the draft edges have a selection mark of 4 |
| Input: | (VARIANT_BOOL) isEdgeDraft | Determine if it is an edge or neutral plane draft; TRUE if this will be an edge draft and the user will select edges to be drafted, FALSE if this is to be a face draft and the user will select faces to be drafted (the system will automatically select the faces next to the edge to be drafted) |
| Input: | (long) propType | Propagation type |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The propagation type argument propType can be:

- 0 = no propagation
- 1 = propagate to the next tangent faces that share the base neutral plane. This option can be specified for edge draft or neutral plane draft
- 2 = propagate to all faces that are a neighbor of the neutral plane
- 3 = propagate to all faces that are a neighbor of the neutral plane on all the inner_loops (e.g. all faces of a pocket or a boss)
- 4 = propagate to all faces that are a neighbor of the neutral plane on the outer loop (e.g. the sides of a box with the bottom face as neutral plane)
