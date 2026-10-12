---
title: "Component::GetTessTriStripNorms"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetTessTriStripNorms.htm"
---

# Component::GetTessTriStripNorms

This method is obsolete and has been superseded by [Component2::GetTessTriStripNorms](sldworksAPI.chm::/Component2/Component2__GetTessTriStripNorms.htm).

Description

This method gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this component.

Syntax (OLE Automation)

retval = Component.GetTessTriStripNorms ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing the tri-strip normals |
| --- | --- | --- |

Syntax (COM)

status = Component->IGetTessTriStripNorms ( retval )

| Output: | (float*) retval | Pointer to an array of floats (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Tessellation information is available only when the component is loaded as lightweight.

The format of the returned data is:

- DWORD FaceCount
- DWORD StripCount
- DWORD (VertexCount) x 3
- DWORD NumStrips
- DWORD [VertexPerStrip] where this is an array from 0 to (Numstrips-1)
- Float [Normals ] where this is an array of X,Y,Z normal components for each strip from 0 to (VertexPerStrip-1)

where

- FaceCount = number of faces on the body
- StripCount = total number of strips on the body
- VertexCount x 3 = total number of vertices; multiplied by three to cover X,Y, and Z
- NumStrips = number of strips on a particular face
- VertexPerStrip = an array containing the number of vertex points on particular face strip
- NormalComp = an array of X,Y,Z normal components for each vertex on the particular face strip
