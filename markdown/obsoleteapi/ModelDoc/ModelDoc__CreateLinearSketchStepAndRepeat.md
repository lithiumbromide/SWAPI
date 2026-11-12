---
title: "ModelDoc::CreateLinearSketchStepAndRepeat"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateLinearSketchStepAndRepeat.htm"
---

# ModelDoc::CreateLinearSketchStepAndRepeat

This method is obsolete and has been superseded by [ModelDoc2::CreateLinearSketchStepAndRepeat](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreateLinearSketchStepAndRepeat.htm).

Description

This method creates linear sketch step-and-repeat.

Syntax (OLE Automation)

retval = ModelDoc.CreateLinearSketchStepAndRepeat ( num1, num2, spacing1, spacing2, angle1, angle2, deleteInstances )

| Input: | (long) num1 | Total number of instances along Direction1, including the seed |
| --- | --- | --- |
| Input: | (long) num2 | Total number of instances along Direction2, including the seed |
| Input: | (double) spacing1 | Spacing between elements along Direction1 |
| Input: | (double) spacing2 | Spacing between elements along Direction2 |
| Input: | (double) angle1 | Relative to the X axis, the angle for Direction1 |
| Input: | (double) angle2 | Relative to the X axis, the angle for Direction2 |
| Input: | (BSTR) deleteInstances | Instance numbers to delete passed as a string in the format: "( a ) ( b ) ( c ) " |
| Return: | (BOOL) retval | TRUE if the sketch pattern was created successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc->CreateLinearSketchStepAndRepeat (num1, num2, spacing1, spacing2, angle1, angle2, deleteInstances, &retval )

| Input: | (long) num1 | Total number of instances along Direction1, including the seed |
| --- | --- | --- |
| Input: | (long) num2 | Total number of instances along Direction2, including the seed |
| Input: | (double) spacing1 | Spacing between elements along Direction1 |
| Input: | (double) spacing2 | Spacing between elements along Direction2 |
| Input: | (double) angle1 | Relative to the X axis, the angle for Direction1 |
| Input: | (double) angle2 | Relative to the X axis, the angle for Direction2 |
| Input: | (BSTR) deleteInstances | Instance numbers to delete passed as a string in the format: "( a ) ( b ) ( c ) " |
| Output: | (VARIANT_BOOL) retval | TRUE if the sketch pattern was created successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

Remarks
