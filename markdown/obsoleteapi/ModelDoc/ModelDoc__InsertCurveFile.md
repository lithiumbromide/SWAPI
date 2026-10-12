---
title: "ModelDoc::InsertCurveFile"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertCurveFile.htm"
---

# ModelDoc::InsertCurveFile

This method is obsolete and has been superseded by [ModelDoc2::InsertCurveFile](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertCurveFile.htm).

Description

This method creates a 3D-reference curve. This reference curve goes through the points in the specified file.

Syntax (OLE Automation)

retval = ModelDoc.InsertCurveFile ( fileName)

| Input: | (BSTR) fileName | Filename containing the point data |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the curve is created successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc->InsertCurveFile ( fileName, &retval )

| Input: | (BSTR) fileName | Filename containing the point data |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the curve is created successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The points in the specified input file can have the X, Y, Z values separated by commas, spaces, or tabs, and there should be one point per line.
