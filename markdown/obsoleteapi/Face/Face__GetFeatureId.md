---
title: "Face::GetFeatureId"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetFeatureId.htm"
---

# Face::GetFeatureId

This method is obsolete and has been superseded by [Face2::GetFeatureId](sldworksAPI.chm::/Face2/Face2__GetFeatureId.htm).

Description

This method finds the order number for the feature that is the owner of the face.

Syntax (OLE Automation)

retval = Face.GetFeatureId ()

| Return: | (long) retval | Order number of the feature that is the owner of the face |
| --- | --- | --- |

Syntax (COM)

status = Face->GetFeatureId ( &retval )

| Output: | (long) retval | Order number of the feature that is the owner of the face |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |
