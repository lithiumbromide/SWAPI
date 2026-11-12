---
title: "Face::IGetFacetData"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__IGetFacetData.htm"
---

# Face::IGetFacetData

This method is obsolete and has been superseded by [Face2::IGetFacetData](sldworksAPI.chm::/Face2/Face2__IGetFacetData.htm).

Description

This method provides direct access to the facet data of a face.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Face->IGetFacetData ( facetMesh, &nFacets, &nStrips, stripVertexNums, vertexCoords, normalCoords )

| Input: | (int)facetMesh | Mesh to be output (see below) |
| --- | --- | --- |
| Output: | (int)nFacets | Total number of facets overall |
| Output: | (int)nStrips | Number of strips overall |
| Output: | (int)*stripVertexNums | Array of nStrips integers containing the number of facet vertices in each facet strip |
| Output: | (float)*vertexCoords | Pointer to the vertex coordinates (see below) |
| Output: | (float)*normalCoords | Pointer to the normal coordinates (see below) |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This should provide performance benefits over the GetTess* routines.

Before calling this function, you should check whether the current facet information within SolidWorks is valid. This can be done using ModelDoc2::IsTessellationValid.

IGetFacetData provides direct access to facet data within SolidWorks. The values returned are pointers that access SolidWorks memory addresses. Therefore, memory has already been allocated by SolidWorks. This function will simply hand back the pointer values for you to access the data. This is done to avoid the overhead of copying data and to provide increased performance. This function is unique and unlike any other API currently available in SolidWorks because it exposes SolidWorks data directly to the calling application.

All arrays contain internal SolidWorks data and should not be modified or freed.

The facet data obtained from this function can be used until a RegenNotify is received or until [ModelDoc::IsTessellationValid](../ModelDoc/ModelDoc__IsTessellationValid.htm) returns FALSE. When a RegenNotify is received, you must recognize that the facet data is invalid and flag yourself to reacquire the facet data within one of the Repaint Notifications. In addition, if your application is drawing to the SolidWorks display using this facet data, then you should call [ModelDoc::IsTessellationValid](../ModelDoc/ModelDoc__IsTessellationValid.htm) before each use of the facet data.

Valid input values for the factMesh argument are as follows:

-1: Returns data for the facet mesh that SolidWorks is currently using

0: Returns the default SolidWorks mesh

1: Returns the reduced, less accurate mesh

The size of the vertexCoords and normalCoords arrays is equal to (N * 3) where N is:

N = stripVertexNums[ 0 ] + ... + stripVertexNums[ nStrips - 1 ]

The vertex data (e.g. vertex coords) is in the order:

Strip1Vertex1, Strip1Vertex2, ..., Strip1VertexM1, Strip2Vertex1, ...

Strip1VertexM1 is the last vertex in the first strip. M1 is therefore equal to stripVertexNums[0]
