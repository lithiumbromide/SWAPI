---
title: "PartDoc::CreateFeatureFromBody2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__CreateFeatureFromBody2.htm"
---

# PartDoc::CreateFeatureFromBody2

This method is obsolete and has been superseded by [PartDoc::CreateFeatureFromBody3](sldworksAPI.chm::/PartDoc/PartDoc__CreateFeatureFromBody3.htm).

Description

This method creates a new feature from the specified temporary body.

Syntax (OLE Automation)

retval = PartDoc.CreateFeatureFromBody2 ( pBody, makeRefSurface )

| Input: | (LPDISPATCH) pBody | Dispatch pointer to the temporary body object |
| --- | --- | --- |
| Input: | (BOOL) makeRefSurface | If the body cannot be knitted to a solid or if a solid body already exists in this model, then TRUE creates a reference surface feature |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created feature or NULL if the operation fails |

Syntax (COM)

status = PartDoc->ICreateFeatureFromBody2 ( pBody, makeRefSurface, &retval )

| Input: | (LPBODY) pBody | Pointer to the temporary body object |
| --- | --- | --- |
| Input: | (BOOL) makeRefSurface | If the body cannot be knitted to a solid or if a solid body already exists in this model, then TRUE creates a reference surface feature |
| Output: | (LPFEATURE) retval | Pointer to a Dispatch object, the newly created feature or NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is intended to be the final call in a knitting operation. The body that results from your knitting efforts, can be converted into an imported body feature in the SolidWorks model. This is not limited to Body objects obtained from knitting operations.
