---
title: "ModelDoc2::AndSelect"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__AndSelect.htm"
---

# ModelDoc2::AndSelect

This method is obsolete and has been superseded by [ModelDocExtension::SelectByID](../ModelDocExtension/ModelDocExtension__SelectByID.htm).

Description

This method adds the object to the selection list.

Syntax (OLE Automation)

ModelDoc2.AndSelect ( selID, selParams, x, y, z )

| Input: | (BSTR) selID | Object ID |
| --- | --- | --- |
| Input: | (BSTR) selParams | Type name of object |
| Input: | (double) x | X coordinate of selection |
| Input: | (double) y | Y coordinate of selection |
| Input: | (double) z | Z coordinate of selection |

Syntax (COM)

status = ModelDoc2->AndSelect ( selID, selParams, x, y, z )

| Input: | (BSTR) selID | Object ID |
| --- | --- | --- |
| Input: | (BSTR) selParams | Type name of object |
| Input: | (double) x | X coordinate of selection |
| Input: | (double) y | Y coordinate of selection |
| Input: | (double) z | Z coordinate of selection |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
