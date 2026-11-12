---
title: "ModelDoc::LockLightToModel"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__LockLightToModel.htm"
---

# ModelDoc::LockLightToModel

This method is obsolete and has been superseded by [ModelDoc2::LockLightToModel](sldworksAPI.chm::/ModelDoc2/ModelDoc2__LockLightToModel.htm).

Description

This method fixes or unfixes the specified light.

Syntax (OLE Automation)

retval = ModelDoc.LockLightToModel ( lightId, fix )

| Input: | (long)lightId | Light ID |
| --- | --- | --- |
| Output: | (BOOL) fix | TRUE if the light is to be fixed, FALSE otherwise |
| Return: | (BOOL) retval | TRUE if change made successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc->LockLightToModel ( lightId, fix, &retval )

| Input: | (long)lightId | Light ID |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) fix | TRUE if the light is to be fixed, FALSE otherwise |
| Return: | (VARIANT_BOOL) retval | TRUE if change made successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
