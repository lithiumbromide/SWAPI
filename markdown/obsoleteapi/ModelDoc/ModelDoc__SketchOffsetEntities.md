---
title: "ModelDoc::SketchOffsetEntities"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchOffsetEntities.htm"
---

# ModelDoc::SketchOffsetEntities

This method is obsolete and is now superseded by [ModelDoc::SketchOffsetEntities2](ModelDoc__SketchOffsetEntities2.htm).

Description

This method generates entities in the active sketch by offsetting the selected geometry by the specified amount.

Syntax (OLE Automation)

void ModelDoc.SketchOffsetEntities ( offset, flip)

| Input: | (double) offset | Offset distance in meters |
| --- | --- | --- |
| Input: | (BOOL) flip | TRUE if the offset direction should be flipped, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SketchOffsetEntities ( offset, flip )

| Input: | (double) offset | Offset distance in meters |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flip | TRUE if the offset direction should be flipped, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The geometry selected for offset can be an edge, loop, face, external sketch curve, external sketch contour, set of edges, or set of external sketch curves.

NOTE: If the selected geometry is a sketch item, it must be an external sketch curve; for example, it cannot be an item in the active sketch. To offset sketch segments within the active sketch, use ModelDoc::SketchOffset.
