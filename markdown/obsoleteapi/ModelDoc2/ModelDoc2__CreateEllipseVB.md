---
title: "ModelDoc2::CreateEllipseVB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateEllipseVB.htm"
---

# ModelDoc2::CreateEllipseVB

This method is obsolete and has been superseded by [ModelDoc2::CreateEllipse2](ModelDoc2__CreateEllipse2.htm).

Description

This method creates an ellipse.

Syntax (OLE Automation)

retval = ModelDoc2.CreateEllipseVB ( centerX, centerY, centerZ, majorX, majorY, majorZ, minorX, minorY, minorZ)

| Input: | (double) centerX | X values for the ellipse centerpoint |
| --- | --- | --- |
| Input: | (double) centerY | Y values for the ellipse centerpoint |
| Input: | (double) centerZ | Z values for the ellipse centerpoint |
| Input: | (double) majorX | X values for a point on the ellipse and on the major axis |
| Input: | (double) majorY | Y values for a point on the ellipse and on the major axis |
| Input: | (double) majorZ | Z values for a point on the ellipse and on the major axis |
| Input: | (double) minorX | X values for a point on the ellipse and on the minor axis |
| Input: | (double) minorY | Y values for a point on the ellipse and on the minor axis |
| Input: | (double) minorZ | Z values for a point on the ellipse and on the minor axis |
| Return: | (BOOL) retval | TRUE if successfully created, FALSE if not |

Syntax (COM)

status = ModelDoc2->CreateEllipseVB ( centerX, centerY, centerZ, majorX, majorY, majorZ, minorX, minorY, minorZ, &retval )

| Input: | (double) centerX | X values for the ellipse centerpoint |
| --- | --- | --- |
| Input: | (double) centerY | Y values for the ellipse centerpoint |
| Input: | (double) centerZ | Z values for the ellipse centerpoint |
| Input: | (double) majorX | X values for a point on the ellipse and on the major axis |
| Input: | (double) majorY | Y values for a point on the ellipse and on the major axis |
| Input: | (double) majorZ | Z values for a point on the ellipse and on the major axis |
| Input: | (double) minorX | X values for a point on the ellipse and on the minor axis |
| Input: | (double) minorY | Y values for a point on the ellipse and on the minor axis |
| Input: | (double) minorZ | Z values for a point on the ellipse and on the minor axis |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully created, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
