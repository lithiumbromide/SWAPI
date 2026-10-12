---
title: "ModelDoc::InsertCurveFileBegin"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertCurveFileBegin.htm"
---

# ModelDoc::InsertCurveFileBegin

This method is obsolete and has been superseded by [ModelDoc2::InsertCurveFileBegin](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertCurveFileBegin.htm).

Description

This method is the first method called in a set of related methods that can create a 3D-reference curve. This method should precede any calls to ModelDoc::InsertCurveFilePoint.

Syntax (OLE Automation)

void ModelDoc.InsertCurveFileBegin ()

Syntax (COM)

status = ModelDoc->InsertCurveFileBegin ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

This method and ModelDoc::InsertCurveFileEnd should enclose all of your calls to ModelDoc::InsertCurveFilePoint. For example:

Part.InsertCurveFileBegin

Part.InsertCurveFilePoint 0.3048, 0.6096, 0.9144

Part.InsertCurveFilePoint 0.6096, 0.9144, 1.2192

Part.InsertCurveFilePoint 0.9144, 1.2192, 1.524

Part.InsertCurveFilePoint 1.2192, 1.524, 1.8288

Part.InsertCurveFileEnd
