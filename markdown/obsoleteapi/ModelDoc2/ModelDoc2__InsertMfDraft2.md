---
title: "ModelDoc2::InsertMfDraft2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertMfDraft2.htm"
---

# ModelDoc2::InsertMfDraft2

This method is obsolete and has been superseded by [FeatureManager::InsertMultifaceDraft](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertMultifaceDraft.htm).

Description

This method creates a multi-face draft.

Syntax (OLE Automation)

void ModelDoc2.InsertMfDraft2 ( angle, flipDir, isEdgeDraft, propType, stepDraft )

| Input: | (double) angle | Draft angle in radians |
| --- | --- | --- |
| Input: | (BOOL) flipDir | Flip the direction of the draft; the draft direction is determined by the selected direction, which could be a planar face, a reference plane, an edge, or two vertices; if you refer to the mark argument in ModelDocExtension::SelectByID, these items would have a selection mark of 1; faces to draft a selection mark of 2, and draft edges a selection mark of 4 |
| Input: | (BOOL) isEdgeDraft | Determine if it is an edge or neutral plane draft; TRUE if this is an edge draft and the user selects edges to be drafted; FALSE if this is a face draft and the user selects faces to draft (the system automatically selects the faces next to the edge to be drafted) |
| Input: | (long) propType | Propagation type (see Remarks ) |
| Input: | (BOOL) stepDraft | TRUE if the draft is a step draft, FALSE if not |

Syntax (COM)

status = ModelDoc2->InsertMfDraft2 ( angle, flipDir, isEdgeDraft, propType, stepDraft )

| Input: | (double) angle | Draft angle in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flipDir | Flip the direction of the draft; the draft direction is determined by the selected direction, which could be a planar face, a reference plane, an edge, or two vertices; if you refer to the mark argument in ModelDocExtension::SelectByID, these items would have a selection mark of 1; faces to draft a selection mark of 2, and draft edges a selection mark of 4 |
| Input: | (VARIANT_BOOL) isEdgeDraft | Determine if it is an edge or neutral plane draft; TRUE if this is an edge draft and the user selects edges to be drafted; FALSE if this is a face draft and the user selects faces to draft (the system automatically selects the faces next to the edge to be drafted) |
| Input: | (long) propType | Propagation type (see Remarks ) |
| Input: | (VARIANT_BOOL) stepDraft | TRUE if the draft is a step draft, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Make the selections using ModelDocExtension::SelectByID before calling this method.

The propagation type argument propType can be one of the following values:

- 0 = no propagation.
- 1 = propagate to the next tangent faces that share the base neutral plane. You can specify this option for an edge draft or neutral plane draft.
- 2 = propagate to all faces that are a neighbor of the neutral plane.
- 3 = propagate to all faces that are a neighbor of the neutral plane on all the inner loops (for example, all faces of a pocket or a boss).
- 4 = propagate to all faces that are a neighbor of the neutral plane on the outer loop (e.g. the sides of a box with the bottom face as neutral plane).

This method is the same as interactively creating a draft by selecting Insert, Features, Draft. See the SolidWorks Help for more information about what entities are valid for selection.
