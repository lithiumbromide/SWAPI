---
title: "ModelDoc::GetEntityName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetEntityName.htm"
---

# ModelDoc::GetEntityName

This method is obsolete and has been superseded bysldworksAPI.chm::/ModelDoc2/ModelDoc2__GetEntityName.htmModelDoc2::GetEntityName.

Description

This method gets the name of the specified face, edge, or vertex.

Syntax (OLE Automation)

retval = ModelDoc.GetEntityName ( pEntity )

| Input: | (LPDISPATCH) pEntity | Dispatch pointer of the Entity object |
| --- | --- | --- |
| Return: | (BSTR) retval | Name of the entity |

Syntax (COM)

status = ModelDoc->IGetEntityName ( pEntity, &retval )

| Input: | (LPENTITY) pEntity | Pointer to the Entity object |
| --- | --- | --- |
| Output: | (BSTR) retval | Name of the entity |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
