---
title: "ModelDoc::InsertMfDraft2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertMfDraft2.htm"
---

# ModelDoc::InsertMfDraft2

This method is obsolete and has been superseded by [ModelDoc2::InsertMfDraft2](../ModelDoc2/ModelDoc2__InsertMfDraft2.htm).

Description

This method creates a multiface draft.

Syntax (OLE Automation)

void ModelDoc.InsertMfDraft2 ( angle, flipDir, isEdgeDraft, propType, stepDraft )

| Input: | (double) angle | Draft angle in radians |
| --- | --- | --- |
| Input: | (BOOL) flipDir | Flip the direction of the draft; the draft direction is determined by the selected direction which could be a planar face, a reference plane, an edge, or two vertices; if you refer to the last argument in SelectByMark and AndSelectByMark, these items would have a selection mark of 1; the faces to be drafted have a selection mark of 2 and the draft edges have a selection mark of 4 |
| Input: | (BOOL) isEdgeDraft | Determine if it is an edge or neutral plane draft; TRUE if this will be an edge draft and the user will select edges to be draft, FALSE if this is to be a face draft and the user will select faces to be drafted (the system will automatically select the faces next to the edge to be drafted) |
| Input: | (long) propType | Propagation type, |
| Input: | (BOOL) stepDraft | TRUE if the draft is a step draft, FALSE if not |

Syntax (COM)

status = ModelDoc->InsertMfDraft2 ( angle, flipDir, isEdgeDraft, propType, stepDraft )

| Input: | (double) angle | Draft angle in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flipDir | Flip the direction of the draft; the draft direction is determined by the selected direction which could be a planar face, a reference plane, an edge, or two vertices; if you refer to the last argument in SelectByMark and AndSelectByMark, these items would have a selection mark of 1; the faces to be drafted have a selection mark of 2 and the draft edges have a selection mark of 4 |
| Input: | (VARIANT_BOOL )isEdgeDraft | Determine if it is an edge or neutral plane draft; TRUE if this will be an edge draft and the user will select edges to be draft, FALSE if this is to be a face draft and the user will select faces to be drafted (the system will automatically select the faces next to the edge to be drafted) |
| Input: | (long) propType | Propagation type |
| Input: | (VARIANT_BOOL) stepDraft | TRUE if the draft is a step draft, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The propagation type argument propType mat be one of the following values:

- 0 = no propagation
- 1 = propagate to the next tangent faces that share the base neutral plane. This option can be specified for edge draft or neutral plane draft
- 2 = propagate to all faces that are a neighbor of the neutral plane
- 3 = propagate to all faces that are a neighbor of the neutral plane on all the inner loops (for example, all faces of a pocket or a boss)
- 4 = propagate to all faces that are a neighbor of the neutral plane on the outer loop (for example, the sides of a box with the bottom face as neutral plane)

This method is the same as interactively creating a draft by selecting Insert, Features, Draft.

See the SolidWorks Help for more information about what entities are valid for selection.

Make the selections using a SelectByMark method before calling this method.
