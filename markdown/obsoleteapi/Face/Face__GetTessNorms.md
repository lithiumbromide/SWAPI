---
title: "Face::GetTessNorms"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetTessNorms.htm"
---

# Face::GetTessNorms

This method is obsolete and has been superseded by [Face2::GetTessNorms](sldworksAPI.chm::/Face2/Face2__GetTessNorms.htm).

Description

This method returns the normal vector for each of the triangles that make up the shaded picture tessellation.

Syntax (OLE Automation)

retval = Face.GetTessNorms ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray (see below) |
| --- | --- | --- |

Syntax (COM)

status = Face->IGetTessNorms ( retval )

| Output: | (float*) retval | Pointer to an array of floats (see below) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value for this method is in the format:

float x, y, z - first point unit normal

float x, y, z - second point unit normal

float x, y, z - third point unit normal

where this data repeats itself for the set of triangles on this face.

The total size of the data is [ 9 x sizeof(float) x (number of triangles) ].
