---
title: "ModelDoc::AndSelectByID"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AndSelectByID.htm"
---

# ModelDoc::AndSelectByID

This method is obsolete and has been superseded by [ModelDoc2::AndSelectByID](../ModelDoc2/ModelDoc2__AndSelectByID.htm).

Description

This method adds an object to the list of selected items, or removes it if it is already selected. For a full description of selection and the arguments, see ModelDoc::SelectByID.

Syntax (OLE Automation)

retval = ModelDoc.AndSelectByID ( selID, selParams, x, y, z)

| Input: | (BSTR) selID | ID of object |
| --- | --- | --- |
| Input: | (BSTR) selParams | Type name of object (uppercase) |
| Input: | (double) x | X selection location |
| Input: | (double) y | Y selection location |
| Input: | (double) z | Z selection location |
| Return: | (BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |

Syntax (COM)

status = ModelDoc->AndSelectByID ( selID, selParams, x, y, z, &retval )

| Input: | (BSTR) selID | ID of object |
| --- | --- | --- |
| Input: | (BSTR) selParams | Type name of object (uppercase) |
| Input: | (double) x | X selection location |
| Input: | (double) y | Y selection location |
| Input: | (double) z | Z selection location |
| Output: | (VARIANT_BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For more details, refer to the ModelDoc::SelectByID documentation.
