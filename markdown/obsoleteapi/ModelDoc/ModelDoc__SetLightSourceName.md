---
title: "ModelDoc::SetLightSourceName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetLightSourceName.htm"
---

# ModelDoc::SetLightSourceName

This method is obsolete and has been superseded by [ModelDoc2::SetLightSourceName](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetLightSourceName.htm).

Description

This method sets the light source name, as used internally by SolidWorks.

Syntax (OLE Automation)

retval = ModelDoc.SetLightSourceName ( id, newName)

| Input: | (long) id | ID of the light source whose name you want to set |
| --- | --- | --- |
| Input: | (BSTR) newName | Name to be given to the specified light source |
| Return: | (BOOL) retval | TRUE if the name was set successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SetLightSourceName ( id, newName, &retval )

| Input: | (long) id | ID of the light source whose name you want to set |
| --- | --- | --- |
| Input: | (BSTR) newName | Name to be given to the specified light source |
| Output: | (VARIANT_BOOL) retval | TRUE if the name was set successfully, FALSE otherwise |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The light source ID ranges from 0 to n, where n = (the total number of light sources - 1). To get the total number of light sources, use ModelDoc::GetLightSourceCount.
