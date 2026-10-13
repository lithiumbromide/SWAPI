---
title: "ModelDoc::GetCoordinateSystemXformByName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetCoordinateSystemXformByName.htm"
---

# ModelDoc::GetCoordinateSystemXformByName

This method is obsolete and has been superseded by [ModelDoc2::GetCoordinateSystemXformByName](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetCoordinateSystemXformByName.htm).

Description

This method gets the transform of the specified coordinate system.

Syntax (OLE Automation)

retval = ModelDoc.GetCoordinateSystemXformByName( nameIn )

| Input: | (BSTR) nameIn | N ame of the coordinate system |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT containing a SafeArray of 16 doubles |

Syntax (COM)

status = ModelDoc->IGetCoordinateSystemXformByName( nameIn, xform )

| Input: | (BSTR) nameIn | Name of the coordinate system |
| --- | --- | --- |
| Output: | (double*) xform | P ointer to an array of 16 doubles |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The transform is returned as an array of 16 elements. The first 9 are elements of 3x3 matrix, the next 3 define translation, the next 1 is scaling. The last 3 elements are unused.
