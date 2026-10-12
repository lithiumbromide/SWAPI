---
title: "PartDoc::GetCorrespondingEntity"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__GetCorrespondingEntity.htm"
---

# PartDoc::GetCorrespondingEntity

This method is obsolete and has been superseded by [ModelDocExtension::GetCorrespondingEntity](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__GetCorrespondingEntity.htm).

Description

This method gets an entity for the corresponding assembly component entity.

Syntax (OLE Automation)

retval = PartDoc.GetCorrespondingEntity ( entity)

| Input: | (LPDISPATCH) entity | Pointer to Dispatch object of entity (vertex, face, or edge) |
| --- | --- | --- |
| Output: | (LPDISPATCH) *retval | Pointer to the corresponding entity in the context of a part document |

Syntax (COM)

status = PartDoc->IGetCorrespondingEntity ( pEntity, retval )

| Input: | (LPENTITY) pEntity | Pointer to Entity object of a vertex, face, or edge |
| --- | --- | --- |
| Output: | (LPENTITY) *retval | Pointer to the corresponding entity in the context of a part document |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
