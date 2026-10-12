---
title: "ModelDoc::AndSelectByMark"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AndSelectByMark.htm"
---

# ModelDoc::AndSelectByMark

This method is obsolete and has been superseded by [ModelDoc2::AndSelectByMark](../ModelDoc2/ModelDoc2__AndSelectByMark.htm).

Description

This method adds an object to the selections, or removes it if it is already selected. The selection is added with a mark as required by certain API functions that use multiple selections. For a full description of the arguments ,see ModelDoc::SelectByMark

Syntax (OLE Automation)

retval = ModelDoc.AndSelectByMark ( selID, selParams, x, y, z, mark)

| Input: | (BSTR) selID | ID of object |
| --- | --- | --- |
| Input: | (BSTR) selParams | Type name of object |
| Input: | (double) x | X selection location |
| Input: | (double) y | Z selection location |
| Input: | (double) z | Z selection location |
| Input: | (long) mark | Number you wish to use as a mark |
| Return: | (BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |

Syntax (COM)

status = ModelDoc->AndSelectByMark ( selID, selParams, x, y, z, mark, &retval )

| Input: | (BSTR) selID | ID of object |
| --- | --- | --- |
| Input: | (BSTR) selParams | Type name of object |
| Input: | (double) x | X selection location |
| Input: | (double) y | Z selection location |
| Input: | (double) z | Z selection location |
| Input: | (long) mark | Number you wish to use as a mark |
| Output: | (VARIANT_BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
