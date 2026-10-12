---
title: "ModelDoc::CreateEllipseVB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateEllipseVB.htm"
---

# ModelDoc::CreateEllipseVB

This method is obsolete and has been superseded by [ModelDoc::CreateEllipse2](../ModelDoc2/ModelDoc2__CreateEllipse2.htm).

Description

This method creates an ellipse.

Syntax (OLE Automation)

retval = ModelDoc.CreateEllipseVB ( centerX, centerY, centerZ, majorX, majorY, majorZ, minorX, minorY, minorZ)

| Input: | (double) centerX | X value for the ellipse center point |
| --- | --- | --- |
| Input: | (double) centerY | Y value for the ellipse center point |
| Input: | (double) centerZ | Z value for the ellipse center point |
| Input: | (double) majorX | X value for a point on the ellipse and on the major axis |
| Input: | (double) majorY | Y value for a point on the ellipse and on the major axis |
| Input: | (double) majorZ | Z value for a point on the ellipse and on the major axis |
| Input: | (double) minorX | X value for a point on the ellipse and on the minor axis |
| Input: | (double) minorY | Y value for a point on the ellipse and on the minor axis |
| Input: | (double) minorZ | Z value for a point on the ellipse and on the minor axis |
| Return: | (BOOL) retval | TRUE if successfully created, FALSE otherwise. |

Syntax (COM)

status = ModelDoc->CreateEllipseVB ( centerX, centerY, centerZ, majorX, majorY, majorZ, minorX, minorY, minorZ, &retval )

| Input: | (double) centerX | X value for the ellipse center point |
| --- | --- | --- |
| Input: | (double) centerY | Y value for the ellipse center point |
| Input: | (double) centerZ | Z value for the ellipse center point |
| Input: | (double) majorX | X value for a point on the ellipse and on the major axis |
| Input: | (double) majorY | Y value for a point on the ellipse and on the major axis |
| Input: | (double) majorZ | Z value for a point on the ellipse and on the major axis |
| Input: | (double) minorX | X value for a point on the ellipse and on the minor axis |
| Input: | (double) minorY | Y value for a point on the ellipse and on the minor axis |
| Input: | (double) minorZ | Z value for a point on the ellipse and on the minor axis |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully created, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
