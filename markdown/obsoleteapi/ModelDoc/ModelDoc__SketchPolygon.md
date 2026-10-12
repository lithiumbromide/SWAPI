---
title: "ModelDoc::SketchPolygon"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchPolygon.htm"
---

# ModelDoc::SketchPolygon

This method is obsolete and has been superseded by [ModelDoc2::SketchPolygon](../ModelDoc2/ModelDoc2__SketchPolygon.htm).

Description

This method creates a polygon in the active sketch

Syntax (OLE Automation)

retval = ModelDoc.SketchPolygon ( xCenter, yCenter, xEdge, yEdge, nSides, bInscribed )

| Input: | (double) xCenter | X component of the polygon's center |
| --- | --- | --- |
| Input: | (double) yCenter | Y component of the polygon's center |
| Input: | (double) xEdge | X component of the first vertex on the polygon |
| Input: | (double) yEdge | Y component of the first vertex on the polygon |
| Input: | (int) nSides | Number of sides for the polygon |
| Input: | (BOOL) bInscribed | TRUE to show an inscribed construction circle, FALSE to show a circumscribed construction circle |
| Return: | (BOOL) retval | TRUE if the polygon is created, FALSE if not |

Syntax (COM)

status = ModelDoc->SketchPolygon ( double xCenter, double yCenter, double xEdge, double yEdge, int nSides, VARIANT_BOOL* retval )

| Input: | (double) xCenter | X component of the polygon's center |
| --- | --- | --- |
| Input: | (double) yCenter | Y component of the polygon's center |
| Input: | (double) xEdge | X component of the first vertex on the polygon |
| Input: | (double) yEdge | Y component of the first vertex on the polygon |
| Input: | (int) nSides | Number of sides for the polygon |
| Input: | (BOOL) bInscribed | TRUE to show an inscribed construction circle, FALSE to show a circumscribed construction circle |
| Output: | (VARIANT_BOOL) retval | TRUE if the polygon is created, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

After calling this method, the PropertyPage is left in edit mode for the polygon. To exit this PropertyPage and complete the operation ,call ModelDoc2::SetPickMode or ModelDoc2::ClearSelection or exit the sketch.
