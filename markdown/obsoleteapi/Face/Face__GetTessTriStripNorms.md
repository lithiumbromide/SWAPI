---
title: "Face::GetTessTriStripNorms"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetTessTriStripNorms.htm"
---

# Face::GetTessTriStripNorms

This method is obsolete and has been superseded by [Face2::GetTessTriStripNorms](sldworksAPI.chm::/Face2/Face2__GetTessTriStripNorms.htm).

Description

This method gives the normal vector for each of the triangles which make up the shaded picture tessellation for this face.

Syntax (OLE Automation)

retval = Face.GetTessTriStripNorms ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing the tristrip normals |
| --- | --- | --- |

Syntax (COM)

status = Face->IGetTessTriStripNorms ( retval )

| Output: | (float*) retval | Pointer to an array of floats (see below) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The format of the return data is:

DWORD NumStrips

DWORD [VertexPerStrip] where this is an array from 0 to (Numstrips-1)

Float [Normals ] where this is an array of X,Y,Z normal components for each strip from 0 to (VertexPerStrip-1)

where:

NumStrips = number of strips on a particular face

VertexPerStrip = an array containing the number of vertex points on particular face strip

NormalComp = an array of X,Y,Z normal components for each vertex on the particular face strip
