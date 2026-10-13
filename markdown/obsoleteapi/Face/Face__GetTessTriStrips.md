---
title: "Face::GetTessTriStrips"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetTessTriStrips.htm"
---

# Face::GetTessTriStrips

This method is obsolete and has been superseded by [Face2::GetTessTriStrips](sldworksAPI.chm::/Face2/Face2__GetTessTriStrips.htm).

Description

This method returns the vertices that make up the shaded picture tessellation for this face.

Syntax (OLE Automation)

retval = Face.GetTessTriStrips ( noConversion)

| Input: | (BOOL) noConversion | TRUE prohibits conversion to user units from system units, FALSE does not |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray |

Syntax (COM)

status = Face->IGetTessTriStrips ( noConversion, retval )

| Input: | (VARIANT_BOOL) noConversion | TRUE prohibits conversion to user units from system units, FALSE does not |
| --- | --- | --- |
| Output: | (float*) retval | Pointer to an array of floats |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The vertices are all unique for that strip. A vertex that is shared by two tessellation triangles appears only once in the return value.

These triangles are intended for graphics display purposes and do not represent a tessellation that you can use, for example, with a machining application. If you need the level of accuracy associated with a machining product, traverse the body faces and extract the topology and geometry data to create your own faceting.

The format of the returned data is:

DWORD NumStrips

DWORD [VertexPerStrip]

Float [VertexPoints]

where:

NumStrips = Number of strips on a particular face

VertexPerStrip = Array from 0 to (Numstrips-1) containing the number of vertex points on particular face strip

VertexPoints = Array of X,Y,Z points for each vertex on the particular face strip from 0 to (VertexPerStrip-1)

Because the returned array elements are of type float (or single in VB) and NumStrips and the elements of VertexPerStrip are of type integer packed into the return array elements, you must unpack them before you can use them.

For example:

sa[0] = Number of strips in this face

sa[1] = Number of vertices in 1st strip of this face

sa[2] = Number of vertices in 2nd strip of this face

…

sa[ sa[0] ] = Number of vertices in last strip of this face

For each strip, i:

sa[ sa[0] + 1] = X value of 1st vertex in this strip of the face

sa[ sa[0] + 2] = Y value of 1st vertex in this strip of the face

sa[ sa[0] + 3] = Z value of 1st vertex in this strip of the face

sa[ sa[0] + 4] = X value of 2nd vertex in this strip of the face

…

sa[ sa[0] + (sa[ i ] x 3)] = Z value of last vertex in this strip of the face
