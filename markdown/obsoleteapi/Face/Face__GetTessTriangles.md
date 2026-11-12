---
title: "Face::GetTessTriangles"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetTessTriangles.htm"
---

# Face::GetTessTriangles

This method is obsolete and has been superseded by [Face2::GetTessTriangles](sldworksAPI.chm::/Face2/Face2__GetTessTriangles.htm).

Description

This method returns the triangles that make up the shaded picture tessellation for this face.

Syntax (OLE Automation)

retval = Face.GetTessTriangles ( noConversion)

| Input: | (BOOL) noConversion | TRUE prohibits conversion to user units from system units, FALSE does not |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray (see below) |

Syntax (COM)

status = Face->IGetTessTriangles ( noConversion, retval )

| Input: | (VARIANT_BOOL) noConversion | TRUE prohibits conversion to user units from system units, FALSE does not |
| --- | --- | --- |
| Output: | (float*) retval | Pointer to array of floats (see below) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

These triangles are intended for graphics display purposes and do not represent a tessellation that can be used, for example, by a machining application. If you need the level of accuracy associated with a machining product, traverse the body faces and extract the topology and geometry data to create your own faceting.

The format of the returned data is:

float x, y, z - first point in meters

float x, y, z - second point in meters

float x, y, z - third point in meters

where this data repeats itself for the set of triangles on this face.

The total size of the data is [ 9 x sizeof(float ) x (number of triangles) ].
