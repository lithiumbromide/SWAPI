---
title: "ModelDoc::SketchRectangle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchRectangle.htm"
---

# ModelDoc::SketchRectangle

This method is obsolete and has been superseded by [ModelDoc2::SketchRectangle](../ModelDoc2/ModelDoc2__SketchRectangle.htm).

Description

This method creates a rectangle.

Syntax (OLE Automation)

void ModelDoc.SketchRectangle ( val1, val2, z1, val3, val4, z2, val5)

| Input: | (double) val1 | Upper-left x value in meters |
| --- | --- | --- |
| Input: | (double) val2 | Upper-left y value in meters |
| Input: | (double) z1 | Upper-left z value in meters |
| Input: | (double) val3 | Lower-right x value in meters |
| Input: | (double) val4 | Lower-right y value in meters |
| Input: | (double) z2 | Lower-right z value in meters |
| Input: | (BOOL) val5 | Not used |

Syntax (COM)

status = ModelDoc->SketchRectangle ( val1, val2, z1, val3, val4, z2, val5 )

| Input: | (double) val1 | Upper-left x value in meters |
| --- | --- | --- |
| Input: | (double) val2 | Upper-left y value in meters |
| Input: | (double) z1 | Upper-left z value in meters |
| Input: | (double) val3 | Lower-right x value in meters |
| Input: | (double) val4 | Lower-right y value in meters |
| Input: | (double) z2 | Lower-right z value in meters |
| Input: | (VARIANT_BOOL) val5 | Not used |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
