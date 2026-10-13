---
title: "Feature::GetBody"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Feature/Feature__GetBody.htm"
---

# Feature::GetBody

This method is obsolete and has been superseded by [Feature::GetFaces](sldworksAPI.chm::/Feature/Feature__GetFaces.htm) and [Face2::GetBody](sldworksapi.chm::/Face2/Face2__GetBody.htm).

Description

For a reference feature or imported body, this method gets the body containing this feature.

Syntax (OLE Automation)

retval = Feature.GetBody ( )

| Return: | (LPDISPATCH) retval | Dispatch pointer to the body |
| --- | --- | --- |

Syntax (COM)

status = Feature->IGetBody ( &Body )

| Output: | (LPBODY) Body | Pointer to the body |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |
