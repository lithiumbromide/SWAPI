---
title: "ModelDoc::AutoInferToggle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AutoInferToggle.htm"
---

# ModelDoc::AutoInferToggle

This method is obsolete and has been superseded by [ModelDoc2::AutoInferToggle](../ModelDoc2/ModelDoc2__AutoInferToggle.htm).

Description

This method toggles autoinferencing mode.

Syntax (OLE Automation)

void ModelDoc.AutoInferToggle ( )

Syntax (COM)

status = ModelDoc->AutoInferToggle ( )

| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |
| --- | --- | --- |

Remarks

Inferencing mode can be seen when creating a sketch segment and you move the mouse over another sketch item. If inferencing is turned on, you see a dashed line from the current cursor position to the inferenced position on the existing sketch entity.
