---
title: "ModelDoc::CreateCircularSketchStepAndRepeat"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateCircularSketchStepAndRepeat.htm"
---

# ModelDoc::CreateCircularSketchStepAndRepeat

This method is obsolete and has been superseded by [ModelDoc2::CreateCircularSketchStepAndRepeat](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreateCircularSketchStepAndRepeat.htm).

Description

This method creates circular sketch step and repeat.

Syntax (OLE Automation)

retval = ModelDoc.CreateCircularSketchStepAndRepeat ( arcRadius, arcAngle, patternNum, patternSpacing, patternRotate, deleteInstances )

| Input: | (double) arcRadius | Radius to be used in the circular sketch pattern |
| --- | --- | --- |
| Input: | (double) arcAngle | Angle relative to the sketch entities being patterned |
| Input: | (long) patternNum | Total number of instances, including the seed geometry |
| Input: | (double) patternSpacing | Spacing between pattern elements (in radians) |
| Input: | (BOOL) patternRotate | Rotate the pattern |
| Input: | (BSTR) deleteInstances | Instance numbers to delete passed as a string in the format: "( a ) ( b ) ( c ) " |
| Return: | (BOOL) retval | TRUE if the sketch pattern was created successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc->CreateCircularSketchStepAndRepeat ( arcRadius, arcAngle, patternNum, patternSpacing, patternRotate, deleteInstances, &retval )

| Input: | (double) arcRadius | Radius to be used in the circular sketch pattern |
| --- | --- | --- |
| Input: | (double) arcAngle | Angle relative to the sketch entities being patterned |
| Input: | (long) patternNum | Total number of instances, including the seed geometry |
| Input: | (double) patternSpacing | Spacing between pattern elements (in radians) |
| Input: | (VARIANT_BOOL) patternRotate | Rotate the pattern |
| Input: | (BSTR) deleteInstances | Instance numbers to delete passed as a string in the format: "( a ) ( b ) ( c ) " |
| Output: | (VARIANT_BOOL) retval | TRUE if the sketch pattern was created successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
