---
title: "ModelDoc::SketchUseEdge2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchUseEdge2.htm"
---

# ModelDoc::SketchUseEdge2

This method is obsolete and has been superseded by [ModelDoc2::SketchUseEdge2](../ModelDoc2/ModelDoc2__SketchUseEdge2.htm).

Description

This method uses the selected edges to generate geometry in the active sketch.

Syntax (OLE Automation)

retval = ModelDoc.SketchUseEdge2 ( chain )

| Input: | (BOOL) chain | TRUE if you want entire chain of entities offset, FALSE if you want only selected sketch entities offset |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the offset was successful |

Syntax (COM)

status = ModelDoc->SketchUseEdge2 ( chain, &retval )

| Input: | (VARIANT_BOOL) chain | TRUE if you want entire chain of entities offset, FALSE if you want only selected sketch entities offset |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the offset was successful |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

See also ModelDoc::SketchOffsetEntities.

Specifying TRUE to the chain Mode argument will offset the selected entity and any other entities that belong to the same contour or chain (Contiguous geometric entities like edges.).
