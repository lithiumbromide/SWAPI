---
title: "ModelDoc::InsertCurveFilePoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertCurveFilePoint.htm"
---

# ModelDoc::InsertCurveFilePoint

This method is obsolete and has been superseded by [ModelDoc2::InsertCurveFilePoint](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertCurveFilePoint.htm).

Description

This method is one of the methods called in a set of methods that can create a 3D-reference curve. This method can set the curve points for the 3D-reference curve.

Syntax (OLE Automation)

retval = ModelDoc.InsertCurveFilePoint ( x, y, z)

| Input: | (double) x | X value for the point |
| --- | --- | --- |
| Input: | (double) y | Y value for the point |
| Input: | (double) z | Z value for the point |
| Return: | (BOOL) retval | TRUE if this call is successful, FALSE otherwise |

Syntax (COM)

status = ModelDoc->InsertCurveFilePoint ( x, y, z, &retval )

| Input: | (double) x | X value for the point |
| --- | --- | --- |
| Input: | (double) y | Y value for the point |
| Input: | (double) z | Z value for the point |
| Output: | (VARIANT_BOOL) retval | TRUE if this call is successful, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

ModelDoc::InsertCurveFileBegin and ModelDoc::InsertCurveFileEnd should enclose all of your calls to this method. For example:

Part.InsertCurveFileBegin

Part.InsertCurveFilePoint 0.3048, 0.6096, 0.9144

Part.InsertCurveFilePoint 0.6096, 0.9144, 1.2192

Part.InsertCurveFilePoint 0.9144, 1.2192, 1.524

Part.InsertCurveFilePoint 1.2192, 1.524, 1.8288

Part.InsertCurveFileEnd
