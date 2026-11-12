---
title: "ModelDoc::SetInferenceMode"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetInferenceMode.htm"
---

# ModelDoc::SetInferenceMode

This method is obsolete and has been superseded by [ModelDoc2::SetInferenceMode](../ModelDoc2/ModelDoc2__SetInferenceMode.htm).

Description

This method sets whether the sketch inference mode for this ModelDoc is turned off or not. This affects sketch entity snapping or infering constraints to other geometry during creation.

Syntax (OLE Automation)

void ModelDoc.SetInferenceMode ( inferenceMode )

| Input: | (BOOL) inferenceMode | TRUE to enable sketch inference mode, FALSE to disable it |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->SetInferenceMode ( inferenceMode )

| Input: | (VARIANT_BOOL) inferenceMode | TRUE to enable sketch inference mode, FALSE to disable it |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Setting the inference mode to FALSE allows faster sketching without inferencing, similar to ModelDoc::SetAddToDB, except that using this method does not disable Undo operations.

Setting the inference mode to TRUE allows inferencing during sketch operations, subject to other settings that may disable inferencing, such as ModelDoc::AutoInferToggle, ModelDoc::SetAddToDB, and DrawingDoc::StartDrawing.
