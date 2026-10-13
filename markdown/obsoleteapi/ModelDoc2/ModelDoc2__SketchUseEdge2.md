---
title: "ModelDoc2::SketchUseEdge2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SketchUseEdge2.htm"
---

# ModelDoc2::SketchUseEdge2

This method is obsolete and has been superseded by [SketchManager::SketchUseEdge](sldworksAPI.chm::/SketchManager/SketchManager__SketchUseEdge.htm).

Description

This method uses the selected edges to generate geometry in the active sketch.

Syntax (OLE Automation)

retval = ModelDoc2.SketchUseEdge2 ( chain )

| Input: | (BOOL) chain | TRUE if you want entire chain of entities offset, FALSE if you want only selected sketch entities offset (see Remarks ) |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the offset is successful, FALSE if not |

Syntax (COM)

status = ModelDoc2->SketchUseEdge2 ( chain, &retval )

| Input: | (VARIANT_BOOL) chain | TRUE if you want entire chain of entities offset, FALSE if you want only selected sketch entities offset (see Remarks ) |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the offset is successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Specifying TRUE to the chain argument offsets the selected entity and any other entities that belong to the same contour or chain (contiguous, geometric entities like edges).

See ModelDoc2::SketchOffsetEntities2 method for similar functionality.
