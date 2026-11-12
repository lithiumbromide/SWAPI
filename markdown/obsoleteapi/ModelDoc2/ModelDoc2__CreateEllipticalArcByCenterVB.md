---
title: "ModelDoc2::CreateEllipticalArcByCenterVB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateEllipticalArcByCenterVB.htm"
---

# ModelDoc2::CreateEllipticalArcByCenterVB

This method is obsolete and has been superseded by [SketchManager::CreateEllipticalArc](sldworksAPI.chm::/SketchManager/SketchManager__CreateEllipticalArc.htm).

Description

This method creates an elliptical arc trimmed between two points.

Syntax (OLE Automation)

retval = ModelDoc2.CreateEllipticalArcByCenterVB ( centerX, centerY, centerZ, majorX, majorY, majorZ, minorX, minorY, minorZ, startX, startY, startZ, endX, endY, endZ)

| Input: | (double) centerX | X values for the ellipse center point |
| --- | --- | --- |
| Input: | (double) centerY | Y values for the ellipse center point |
| Input: | (double) centerZ | Z values for the ellipse center point |
| Input: | (double) majorX | X values for a point on the ellipse and on the major axis |
| Input: | (double) majorY | Y values for a point on the ellipse and on the major axis |
| Input: | (double) majorZ | Z values for a point on the ellipse and on the major axis |
| Input: | (double) minorX | X values for a point on the ellipse and on the minor axis |
| Input: | (double) minorY | Y values for a point on the ellipse and on the minor axis |
| Input: | (double) minorZ | Z values for a point on the ellipse and on the minor axis |
| Input: | (double) startX | X values for CCW elliptical arc start point |
| Input: | (double) startY | Y values for CCW elliptical arc start point |
| Input: | (double) startZ | Z values for CCW elliptical arc start point |
| Input: | (double) endX | X values for CCW elliptical arc end point |
| Input: | (double) endY | Y values for CCW elliptical arc end point |
| Input: | (double) endZ | Z values for CCW elliptical arc end point |
| Return: | (BOOL) retval | TRUE if successfully created, FALSE otherwise |

Syntax (COM)

status = ModelDoc2->CreateEllipticalArcByCenterVB ( centerX, centerY, centerZ, majorX, majorY, majorZ, minorX, minorY, minorZ, startX, startY, startZ, endX, endY, endZ, &retval )

| Input: | (double) centerX | X values for the ellipse center point |
| --- | --- | --- |
| Input: | (double) centerY | Y values for the ellipse center point |
| Input: | (double) centerZ | Z values for the ellipse center point |
| Input: | (double) majorX | X values for a point on the ellipse and on the major axis |
| Input: | (double) majorY | Y values for a point on the ellipse and on the major axis |
| Input: | (double) majorZ | Z values for a point on the ellipse and on the major axis |
| Input: | (double) minorX | X values for a point on the ellipse and on the minor axis |
| Input: | (double) minorY | Y values for a point on the ellipse and on the minor axis |
| Input: | (double) minorZ | Z values for a point on the ellipse and on the minor axis |
| Input: | (double) startX | X values for CCW elliptical arc start point |
| Input: | (double) startY | Y values for CCW elliptical arc start point |
| Input: | (double) startZ | Z values for CCW elliptical arc start point |
| Input: | (double) endX | X values for CCW elliptical arc end point |
| Input: | (double) endY | Y values for CCW elliptical arc end point |
| Input: | (double) endZ | Z values for CCW elliptical arc end point |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully created, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Specify the start* and end* arguments in a counter-clockwise manner.
