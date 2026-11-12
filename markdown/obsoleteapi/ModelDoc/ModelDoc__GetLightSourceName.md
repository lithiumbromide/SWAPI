---
title: "ModelDoc::GetLightSourceName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetLightSourceName.htm"
---

# ModelDoc::GetLightSourceName

This method is obsolete and has been superseded by [ModelDoc2::GetLightSourceName](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetLightSourceName.htm).

Description

This method gets the light source name,as used internally by SolidWorks.

Syntax (OLE Automation)

retval = ModelDoc.GetLightSourceName ( id)

| Input: | (long) id | Light source ID |
| --- | --- | --- |
| Return: | (BSTR) retval | Name of the specified light source |

Syntax (COM)

status = ModelDoc->GetLightSourceName ( id, &retval )

| Input: | (long) id | Light source ID |
| --- | --- | --- |
| Output: | (BSTR) retval | Name of the specified light source |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The light source ID ranges from 0 to n, where n = (the total number of light sources - 1). To get the total number of light sources, use ModelDoc::GetLightSourceCount.
