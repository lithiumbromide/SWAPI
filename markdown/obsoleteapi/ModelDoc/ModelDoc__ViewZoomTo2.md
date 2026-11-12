---
title: "ModelDoc::ViewZoomTo2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ViewZoomTo2.htm"
---

# ModelDoc::ViewZoomTo2

This method is obsolete and has been superseded by [ModelDoc2::ViewZoomTo2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ViewZoomTo2.htm).

Description

This method zooms to a specified region.

Syntax (OLE Automation)

void ModelDoc.ViewZoomTo2 ( x1, y1, z1, x2, y2, z2)

| Input: | (double) x1 | X value for the lower-left point of the zoom area |
| --- | --- | --- |
| Input: | (double) y1 | Y value for the lower-left point of the zoom area |
| Input: | (double) z1 | Z value for the lower-left point of the zoom area |
| Input: | (double) x2 | X value for the upper-right point of the zoom area |
| Input: | (double) y2 | Y value for the upper-right point of the zoom area |
| Input: | (double) z2 | Z value for the upper-right point of the zoom area |

Syntax (COM)

status = ModelDoc->ViewZoomTo2 ( x1, y1, z1, x2, y2, z2 )

| Input: | (double) x1 | X value for the lower-left point of the zoom area |
| --- | --- | --- |
| Input: | (double) y1 | Y value for the lower-left point of the zoom area |
| Input: | (double) z1 | Z value for the lower-left point of the zoom area |
| Input: | (double) x2 | X value for the upper-right point of the zoom area |
| Input: | (double) y2 | Y value for the upper-right point of the zoom area |
| Input: | (double) z2 | Z value for the upper-right point of the zoom area |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
