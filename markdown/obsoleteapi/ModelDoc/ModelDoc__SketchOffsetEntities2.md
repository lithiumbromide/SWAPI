---
title: "ModelDoc::SketchOffsetEntities2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchOffsetEntities2.htm"
---

# ModelDoc::SketchOffsetEntities2

This method is obsolete and has been superseded by [ModelDoc2::SketchOffsetEntities2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SketchOffsetEntities2.htm).

Description

This method generates entities in the active sketch by offsetting the selected geometry by the specified amount.

Syntax (OLE Automation)

retval = ModelDoc.SketchOffsetEntities2 ( offset, bothDirections, chain )

| Input: | (double) offset | Offset distance in meters |
| --- | --- | --- |
| Input: | (BOOL) bothDirections | TRUE to offset in both directions |
| Input: | (BOOL) chain | TRUE if you want entire chain of entities offset, FALSE if you want only selected sketch entities offset |
| Return: | (BOOL) retval | TRUE if the offset was successful |

Syntax (COM)

status = ModelDoc->SketchOffsetEntities2 ( offset, bothDirections, chain, &retval )

| Input: | (double) offset | Offset distance in meters |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) bothDirections | TRUE to offset in both directions |
| Input: | (VARIANT_BOOL) chain | TRUE if you want entire chain of entities offset, FALSE if you want only selected sketch entities offset |
| Output: | (VARIANT_BOOL) retval | TRUE if the offset was successful |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The geometry selected for offset can be an edge, loop, face, external sketch curve, external sketch contour, set of edges, or set of external sketch curves.

Specifying TRUE to the chain argument offsets the selected entity and any other entities that belong to the same contour or chain; for example, contiguous geometric entities like edges.

NOTE: If the selected geometry is a sketch item, it must be an external sketch curve; for example, it cannot be an item in the active sketch. To offset sketch segments within the active sketch, use ModelDoc::SketchOffset.
