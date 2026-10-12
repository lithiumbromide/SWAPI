---
title: "ModelDoc2::GetCoordinateSystemXformByName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetCoordinateSystemXformByName.htm"
---

# ModelDoc2::GetCoordinateSystemXformByName

This method is obsolete and has been superseded by [ModelDocExtension::GetCoordinateSystemTransformByName](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__GetCoordinateSystemTransformByName.htm).

Description

This method returns the inverse transform of the specified coordinate system.

Syntax (OLE Automation)

retval = ModelDoc2.GetCoordinateSystemXformByName( nameIn )

| Input: | (BSTR) nameIn | N ame of the coordinate system |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT containing a SafeArray of 16 doubles (see Remarks ) |

Syntax (COM)

status = ModelDoc2->IGetCoordinateSystemXformByName( nameIn, xform )

| Input: | (BSTR) nameIn | Name of the coordinate system |
| --- | --- | --- |
| Output: | (double*) xform | Pointer to an array of 16 doubles (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The inverse transform is returned as an array of 16 elements:

- First 9 are elements of 3x3 matrix
- Next 3 define translation
- Next 1 is scaling
- Last 3 elements are not used
