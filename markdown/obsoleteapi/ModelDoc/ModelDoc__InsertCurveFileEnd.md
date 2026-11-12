---
title: "ModelDoc::InsertCurveFileEnd"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertCurveFileEnd.htm"
---

# ModelDoc::InsertCurveFileEnd

This method is obsolete and has been superseded by [ModelDoc2::InsertCurveFileEnd](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertCurveFileEnd.htm).

Description

This method is the last method called in a set of related methods that can create a 3D-reference curve. This method also ends the 3D-curve creation.

Syntax (OLE Automation)

retval = ModelDoc.InsertCurveFileEnd ()

| Return: | (BOOL) retval | TRUE if curve is created successfully, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->InsertCurveFileEnd ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if curve is created successfully, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

ModelDoc::InsertCurveFileBegin and this method should enclose all of your calls to ModelDoc::InsertCurveFilePoint. For example:

Part.InsertCurveFileBegin

Part.InsertCurveFilePoint 0.3048, 0.6096, 0.9144

Part.InsertCurveFilePoint 0.6096, 0.9144, 1.2192

Part.InsertCurveFilePoint 0.9144, 1.2192, 1.524

Part.InsertCurveFilePoint 1.2192, 1.524, 1.8288

Part.InsertCurveFileEnd
