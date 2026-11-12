---
title: "ModelDoc::InsertBOMBalloon2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertBOMBalloon2.htm"
---

# ModelDoc::InsertBOMBalloon2

This method is obsolete and has been superseded by [ModelDoc2::InsertBOMBalloon2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertBOMBalloon2.htm).

Description

This method inserts a BOM balloon based on the selected object. The selected object can be an edge, silhouette, face, or vertex.

Syntax (OLE Automation)

retval = ModelDoc.InsertBOMBalloon2 ( style, size, upperTextStyle, upperText, lowerTextStyle, lowerText )

| Input: | (long) style | Balloon style as defined in swBalloonStyle_e |
| --- | --- | --- |
| Input: | (long) size | Balloon Size as defined in swBalloonFit_e |
| Input: | (long) upperTextStyle | Text style for the upper text of the balloon |
| Input: | (BSTR) upperText | Text string to be placed in the upper text of the balloon |
| Input: | (long) lowerTextStyle | Text style for the lower text of the balloon |
| Input: | (BSTR) lowerText | Text string to be placed in the lower text of the balloon |
| Return: | (LPDISPATCH) retval | Pointer to the newly created Note object |

Syntax (COM)

status = ModelDoc->IInsertBOMBalloon2 ( style, size, upperTextStyle, upperText, lowerTextStyle, lowerText, &retval)

| Input: | (long) style | Balloon style as defined in swBalloonStyle_e |
| --- | --- | --- |
| Input: | (long) size | Balloon Size as defined in swBalloonFit_e |
| Input: | (long) upperTextStyle | Text style for the upper text of the balloon |
| Input: | (BSTR) upperText | Text string to be placed in the upper text of the balloon |
| Input: | (long) lowerTextStyle | Text style for the lower text of the balloon |
| Input: | (BSTR) lowerText | Text string to be placed in the lower text of the balloon |
| Output: | (LPNOTE) retval | Pointer to the newly created Note object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
