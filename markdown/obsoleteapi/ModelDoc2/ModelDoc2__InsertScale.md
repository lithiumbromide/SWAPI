---
title: "ModelDoc2::InsertScale"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertScale.htm"
---

# ModelDoc2::InsertScale

This method is obsolete and has been superseded by [FeatureManager::InsertScale](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertScale.htm).

Description

This method applies a scaling factor to the model.

Syntax (OLE Automation)

void ModelDoc2.InsertScale ( scaleFactor_x, scaleFactor_y, scaleFactor_z, isUniform, scaleType )

| Input: | (double) scaleFactor_x | X component of the scale factor |
| --- | --- | --- |
| Input: | (double) scaleFactor_y | Y component of the scale factor |
| Input: | (double) scaleFactor_z | Z component of the scale factor |
| Input: | (BOOL) isUniform | TRUE if the scaling should be uniform, FALSE otherwise |
| Input: | (int) scaleType | Type of scale as defined in swScaleType_e |

Syntax (COM)

status = ModelDoc2->InsertScale ( scaleFactor_x, scaleFactor_y, scaleFactor_z, isUniform, scaleType )

| Input: | (double) scaleFactor_x | X component of the scale factor |
| --- | --- | --- |
| Input: | (double) scaleFactor_y | Y component of the scale factor |
| Input: | (double) scaleFactor_z | Z component of the scale factor |
| Input: | (BOOL) isUniform | TRUE if the scaling should be uniform, FALSE otherwise |
| Input: | (int) scaleType | Type of scale as defined in swScaleType_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

| If isUniform is... | Then... |
| --- | --- |
| TRUE | scaleFactor_x is used as the uniform scaling factor. |
| FALSE | all three scaling factors are used. |
