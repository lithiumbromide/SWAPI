---
title: "ModelDoc2::AutoInferToggle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__AutoInferToggle.htm"
---

# ModelDoc2::AutoInferToggle

This method is obsolete and has been superseded by [SketchManager::AutoInference](sldworksAPI.chm::/SketchManager/SketchManager__AutoInference.htm).

Description

This method toggles automatic inferencing mode.

Syntax (OLE Automation)

void ModelDoc2.AutoInferToggle ( )

Syntax (COM)

status = ModelDoc2->AutoInferToggle ( )

| Return: | (HRESULT)status | S_OK if successfu |
| --- | --- | --- |

Remarks

Inferencing mode can be seen when creating a sketch segment and you mouse moves past another sketch item. If inferencing is turned on, you see a dashed line from the current cursor position to the inferenced position on the existing sketch entity.
