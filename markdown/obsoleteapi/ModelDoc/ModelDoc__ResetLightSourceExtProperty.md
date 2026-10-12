---
title: "ModelDoc::ResetLightSourceExtProperty"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ResetLightSourceExtProperty.htm"
---

# ModelDoc::ResetLightSourceExtProperty

This method is obsolete and has been superseded by [ModelDoc2::ResetLightSourceExtProperty](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ResetLightSourceExtProperty.htm).

Description

This method resets the properties for a light source.

Syntax (OLE Automation)

void ModelDoc.ResetLightSourceExtProperty ( Id)

| Input: | (long) Id | ID of the light source |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->ResetLightSourceExtProperty ( Id )

| Input: | (long) Id | ID of the light source |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The light source ID range from 0 to n, where n = (the total number of light sources - 1). To get the total number of light sources, use ModelDoc::GetLightSourceCount.
