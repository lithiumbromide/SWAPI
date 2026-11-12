---
title: "ModelDoc::Create3PointArc"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__Create3PointArc.htm"
---

# ModelDoc::Create3PointArc

This method is obsolete and has been superseded by [ModelDoc2::Create3PointArc](../ModelDoc2/ModelDoc2__Create3PointArc.htm).

Description

This method creates a 3-point arc.

Syntax (OLE Automation)

retval = ModelDoc.Create3PointArc ( p1x, p1y, p1z, p2x, p2y, p2z, p3x, p3y, p3z)

| Input: | (double) p1x | X value of point 1 |
| --- | --- | --- |
| Input: | (double) p1y | Y value of point 1 |
| Input: | (double) p1z | Z value of point 1 |
| Input: | (double) p2x | X value of point 2 |
| Input: | (double) p2y | Y value of point 2 |
| Input: | (double) p2z | Z value of point 2 |
| Input: | (double) p3x | X value of point 3 |
| Input: | (double) p3y | Y value of point 3 |
| Input: | (double) p3z | Z value of point 3 |
| Return: | (BOOL) retval | TRUE if successfully created, FALSE otherwise |

Syntax (COM)

status = ModelDoc->Create3PointArc ( p1x, p1y, p1z, p2x, p2y, p2z, p3x, p3y, p3z, &retval )

| Input: | (double) p1x | X value of point 1 |
| --- | --- | --- |
| Input: | (double) p1y | Y value of point 1 |
| Input: | (double) p1z | Z value of point 1 |
| Input: | (double) p2x | X value of point 2 |
| Input: | (double) p2y | Y value of point 2 |
| Input: | (double) p2z | Z value of point 2 |
| Input: | (double) p3x | X value of point 3 |
| Input: | (double) p3y | Y value of point 3 |
| Input: | (double) p3z | Z value of point 3 |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully created, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
