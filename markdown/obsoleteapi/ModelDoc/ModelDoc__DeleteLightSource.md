---
title: "ModelDoc::DeleteLightSource"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__DeleteLightSource.htm"
---

# ModelDoc::DeleteLightSource

This method is obsolete and has been superseded by [ModelDoc2::DeleteLightSource](sldworksAPI.chm::/ModelDoc2/ModelDoc2__DeleteLightSource.htm).

Description

This method deletes a light source.

Syntax (OLE Automation)

void ModelDoc.DeleteLightSource ( Id)

| Input: | (long) Id | ID of the light source |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->DeleteLightSource ( Id )

| Input: | (long) Id | ID of the light source |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The light source ID range is from 0 to n, where n = (the total number of light sources - 1). To get the total number of light sources, see ModelDoc::GetLightSourceCount.
