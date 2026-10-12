---
title: "ModelDoc::InsertScale"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertScale.htm"
---

# ModelDoc::InsertScale

This method is obsolete and has been superseded by [ModelDoc2::InsertScale](../ModelDoc2/ModelDoc2__InsertScale.htm).

Description

This method applies a scaling factor to the model.

Syntax (OLE Automation)

void ModelDoc.InsertScale ( scaleFactor_x, scaleFactor_y, scaleFactor_z, isUniform, scaleType )

| Input: | (double) scaleFactor_x | X component of the scale factor |
| --- | --- | --- |
| Input: | (double) scaleFactor_y | Y component of the scale factor |
| Input: | (double) scaleFactor_z | Z component of the scale factor |
| Input: | (BOOL) isUniform | TRUE if the scaling should be uniform, FALSE otherwise. |
| Input: | (int) scaleType | Type of scale as defined in swScaleType_e |

Syntax (COM)

status = ModelDoc->InsertScale ( scaleFactor_x, scaleFactor_y, scaleFactor_z, isUniform, scaleType )

| Input: | (double) scaleFactor_x | X component of the scale factor |
| --- | --- | --- |
| Input: | (double) scaleFactor_y | Y component of the scale factor |
| Input: | (double) scaleFactor_z | Z component of the scale factor |
| Input: | (BOOL) isUniform | TRUE if the scaling should be uniform, FALSE otherwise |
| Input: | (int) scaleType | Type of scale as defined in swScaleType_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If isUniform is TRUE, then scaleFactor_x is used as the uniform scaling factor. If isUniform is FALSE, then all three scaling factors are used.
