---
title: "Face::GetTessTriangleCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetTessTriangleCount.htm"
---

# Face::GetTessTriangleCount

This method is obsolete and has been superseded by [Face2::GetTessTriangleCount](sldworksAPI.chm::/Face2/Face2__GetTessTriangleCount.htm).

Description

This method returns the number of triangles that make up the shaded picture tessellation for this face.

Syntax (OLE Automation)

retval = Face.GetTessTriangleCount ()

| Return: | (long) retval | Triangle count |
| --- | --- | --- |

Syntax (COM)

status = Face->GetTessTriangleCount ( &retval )

| Output: | (long) retval | Triangle count |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |
