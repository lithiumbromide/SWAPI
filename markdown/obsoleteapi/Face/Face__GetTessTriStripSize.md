---
title: "Face::GetTessTriStripSize"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetTessTriStripSize.htm"
---

# Face::GetTessTriStripSize

This method is obsolete and has been superseded by [Face2::GetTessTriStripSize](sldworksAPI.chm::/Face2/Face2__GetTessTriStripSize.htm).

Description

This method gets the necessary array size for allocation with Face::GetTessTriStrips.

Syntax (OLE Automation)

retval = Face.GetTessTriStripSize ()

| Return: | (long) retval | Size of the array returned by Face::GetTessTriStrips |
| --- | --- | --- |

Syntax (COM)

status = Face->GetTessTriStripSize ( &retval )

| Output: | (long) retval | Size of the array returned by Face::GetTessTriStrips |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value from this method is the number of floats returned by Face::GetTessTriStrips, which is (1 + NumStrips + 3 * VertexCount).
