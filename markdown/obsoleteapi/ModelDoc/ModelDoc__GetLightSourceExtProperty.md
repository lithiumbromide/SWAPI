---
title: "ModelDoc::GetLightSourceExtProperty"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetLightSourceExtProperty.htm"
---

# ModelDoc::GetLightSourceExtProperty

This method is obsolete and has been superseded by [ModelDoc2::GetLightSourceExtProperty](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetLightSourceExtProperty.htm).

Description

This method retrieves a float, string, or integer value stored for the light source. The VARIANT type returned is based on the how the data was placed. See ModelDoc::AddLightSourceExtProperty for reference.

Syntax (OLE Automation)

retval = ModelDoc.GetLightSourceExtProperty ( Id, PropertyId)

| Input: | (long) Id | ID of the light source |
| --- | --- | --- |
| Input: | (long) PropertyId | ID of the property extension |
| Return: | (VARIANT) retval | Value stored for the light source |

Syntax (COM)

status = ModelDoc->GetLightSourceExtProperty ( Id, PropertyId, &retval )

| Input: | (long) Id | ID of the light source |
| --- | --- | --- |
| Input: | (long) PropertyId | ID of the property extension |
| Output: | (VARIANT) retval | Value stored for the light source |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The light source ID ranges from 0 to n, where n = (the total number of light sources - 1). To get the total number of light sources, use ModelDoc::GetLightSourceCount.
