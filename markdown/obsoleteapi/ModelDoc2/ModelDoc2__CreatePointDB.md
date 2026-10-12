---
title: "ModelDoc2::CreatePointDB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreatePointDB.htm"
---

# ModelDoc2::CreatePointDB

This method is obsolete and has been superseded by [ModelDoc2::CreatePoint2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreatePoint2.htm).

IMPORTANT: This method ignores the z value when adding a point to a 3D sketch. Thus, update your code to use the more current method, ModelDoc2::CreatePoint2.

Description

This method creates a point.

Syntax (OLE Automation)

retval = ModelDoc2.CreatePointDB ( x, y, z )

| Input: | (double) x | x coordinate of the point |
| --- | --- | --- |
| Input: | (double) y | y coordinate of the point |
| Input: | (double) z | z coordinate of the point |
| Output: | (VARIANT_BOOL) retval | 1 = success, 0 = failure |

Syntax (COM)

status = ModelDoc2->CreatePointDB ( x, y, z, &retval )

| Input: | (double) x | x coordinate of the point |
| --- | --- | --- |
| Input: | (double) y | y coordinate of the point |
| Input: | (double) z | z coordinate of the point |
| Output: | (VARIANT_BOOL) retval | 1 = success, 0 = failure |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
