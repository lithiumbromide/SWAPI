---
title: "ModelDoc2::SetInferenceMode"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SetInferenceMode.htm"
---

# ModelDoc2::SetInferenceMode

This method is obsolete and has been superseded by [SketchManager::InferenceMode](sldworksAPI.chm::/SketchManager/SketchManager__InferenceMode.htm).

Description

This method sets whether the sketch inference mode is turned off or not. This affects sketch entity snapping and inferring constraints to other geometry during creation.

Syntax (OLE Automation)

void ModelDoc2.SetInferenceMode ( inferenceMode )

| Input: | (BOOL) inferenceMode | TRUE to enable sketch inference mode, FALSE to disable it |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->SetInferenceMode ( inferenceMode )

| Input: | (VARIANT_BOOL) inferenceMode | TRUE to enable sketch inference mode, FALSE to disable it |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

| Setting inference mode to... | Allows... |
| --- | --- |
| TRUE | Inferencing during sketch operations, subject to other settings that may disable inferencing such as ModelDoc2::AutoInferToggle, ModelDoc2::SetAddToDB, and DrawingDoc::StartDrawing. |
| FALSE | Faster sketching without inferencing, similar to ModelDoc2::SetAddToDB, except that using this method does not disable undo operations. |
