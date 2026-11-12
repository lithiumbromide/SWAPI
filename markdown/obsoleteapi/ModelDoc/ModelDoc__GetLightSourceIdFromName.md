---
title: "ModelDoc::GetLightSourceIdFromName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetLightSourceIdFromName.htm"
---

# ModelDoc::GetLightSourceIdFromName

This method is obsolete and has been superseded by [ModelDoc2::GetLightSourceIdFromName](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetLightSourceIdFromName.htm).

Description

This method gets the ID of the name of the specified light source. The name specified should be the internal light source name. This is the name that is not visible to the user.

Syntax (OLE Automation)

retval = ModelDoc.GetLightSourceIdFromName ( lightName)

| Input: | (BSTR) lightName | Internal name of the desired light source |
| --- | --- | --- |
| Return: | (long) retval | Light source ID for the specified light source |

Syntax (COM)

status = ModelDoc->GetLightSourceIdFromName ( lightName, &retval )

| Input: | (BSTR) lightName | Internal name of the desired light source |
| --- | --- | --- |
| Output: | (long) retval | Light source ID for the specified light source |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The light source ID ranges from 0 to n, where n = (the total number of light sources - 1). To get the total number of light sources, use ModelDoc::GetLightSourceCount.
