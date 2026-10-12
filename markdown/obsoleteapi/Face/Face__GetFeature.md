---
title: "Face::GetFeature"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetFeature.htm"
---

# Face::GetFeature

This method is obsolete and has been superseded by [Face2::GetFeature](sldworksAPI.chm::/Face2/Face2__GetFeature.htm).

Description

This method returns the feature which is the owner of the face.

Syntax (OLE Automation)

retval = Face.GetFeature ()

| Return: | (LPDISPATCH) retval | Dispatch pointer to the feature which is the owner of the face |
| --- | --- | --- |

Syntax (COM)

status = Face->IGetFeature ( &retval )

| Output: | (LPFEATURE) retval | Pointer to the feature which is the owner of the face |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |
