---
title: "ModelDoc::AddLightToScene"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddLightToScene.htm"
---

# ModelDoc::AddLightToScene

This method is obsolete and has been superseded by [ModelDoc2::AddLightToScene](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AddLightToScene.htm).

Description

This method adds a light source to a scene.

Syntax (OLE Automation)

retval = ModelDoc.AddLightToScene ( lpszNewValue)

| Input: | (BSTR) lpszNewValue | Name to be used for the light |
| --- | --- | --- |
| Return: | (long) retval | ID of the light |

Syntax (COM)

status = ModelDoc->AddLightToScene ( lpszNewValue, &retval )

| Input: | (BSTR) lpszNewValue | Name to be used for the light |
| --- | --- | --- |
| Output: | (long) retval | ID of the light |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
