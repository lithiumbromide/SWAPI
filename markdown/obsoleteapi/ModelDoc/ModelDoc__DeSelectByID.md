---
title: "ModelDoc::DeSelectByID"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__DeSelectByID.htm"
---

# ModelDoc::DeSelectByID

This method is obsolete and has been superseded by [ModelDoc2::DeSelectByID](sldworksAPI.chm::/ModelDoc2/ModelDoc2__DeSelectByID.htm).

Description

This method removes an already selected object from the selection list.

Syntax (OLE Automation)

retval = ModelDoc.DeSelectByID ( selID, selParams, x, y, z)

| Input: | (BSTR) selID | ID of object |
| --- | --- | --- |
| Input: | (BSTR) selParams | Type name of object (uppercase) |
| Input: | (double) x | X selection location |
| Input: | (double) y | Z selection location |
| Input: | (double) z | Z selection location |
| Return: | (BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |

Syntax (COM)

status = ModelDoc->DeSelectByID ( selID, selParams, x, y, z, &retval )

| Input: | (BSTR) selID | ID of object |
| --- | --- | --- |
| Input: | (BSTR) selParams | Type name of object (uppercase) |
| Input: | (double) x | X selection location |
| Input: | (double) y | Z selection location |
| Input: | (double) z | Z selection location |
| Output: | (VARIANT_BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
