---
title: "ModelDoc::AddLightSource"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddLightSource.htm"
---

# ModelDoc::AddLightSource

This method is obsolete and has been superseded by [ModelDoc2::AddLightSource](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AddLightSource.htm).

Description

This method adds a specific light source type to a scene with the specified names.

Syntax (OLE Automation)

retval = ModelDoc.AddLightSource ( idName, lTyp, userName)

| Input: | (BSTR) idName | New light source Id name |
| --- | --- | --- |
| Input: | (int) Type | New light source type |
| Input: | (BSTR) userName | New light source user name |
| Return: | (BOOL) retval | TRUE if the light source creation was successful, FALSE otherwise; creation will fail, for example, if the light source idName is not unique within this model |

Syntax (COM)

status = ModelDoc->AddLightSource ( idName, lTyp, userName, &retval )

| Input: | (BSTR) idName | New light source Id name |
| --- | --- | --- |
| Input: | (int) Type | New light source type |
| Input: | (BSTR) userName | New light source user name |
| Output: | (VARIANT_BOOL) retval | TRUE if the light source creation was successful, FALSE otherwise; creation will fail, for example, if the light source idName is not unique within this model |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
