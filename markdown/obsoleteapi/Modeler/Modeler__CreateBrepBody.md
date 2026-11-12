---
title: "Modeler::CreateBrepBody"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__CreateBrepBody.htm"
---

# Modeler::CreateBrepBody

This method is obsolete and has been superseded by [Modeler::CreateBrepBody3](sldworksAPI.chm::/Modeler/Modeler__CreateBrepBody3.htm).

Description

This method creates a body from brep data.

Syntax (OLE Automation)

retval = Modeler.CreateBrepBody ( type, nTopologies, topologies, edgeToleranceArray, vertexToleranceArray, pointArray, curveArray, surfaceArray, nRelations, parents, children, senses )

| Input: | (int) type | Type of body to create as defined in swTopology_e |
| --- | --- | --- |
| Input: | (int) nTopologies | Number of topological entities in the topologies argument |
| Input: | (VARIANT) topologies | Array of topologies (see swTopoEntity_e), one for each topological entity |
| Input: | (VARIANT) edgeToleranceArray | Array of tolerances for edges |
| Input: | (VARIANT) vertexToleranceArray | Array of tolerances for vertices |
| Input: | (VARIANT) pointArray | Array of coordinates of vertices (geometry for vertices) |
| Input: | (VARIANT) curveArray | Array of curves (geometry for edges) |
| Input: | (VARIANT) surfaceArray | Array of surfaces (geometry for faces) |
| Input: | (int) nRelations | Number of 1-to-1 relationships between topological entities |
| Input: | (VARIANT) parents | Array of parents, one in each relationship |
| Input: | (VARIANT) children | Array of children, one in each relationship |
| Input: | (VARIANT) senses | Array of senses in which child is used by parent in the relationship |
| Return: | (LPDISPATCH) retval | Dispatch pointer for the resulting body |

Syntax (COM)

This method is obsolete and has been superseded by [Modeler::ICreateBrepBody2](Modeler__ICreateBrepBody2.htm).

status = Modeler->ICreateBrepBody ( type, nTopologies, topologies, edgeTolArray, vertexTolArray, pointArray, curveArray, surfaceArray, nRelations, parents, children, senses, &retval )

| Input: | (int) type | Type of body to create as defined in swTopology_e |
| --- | --- | --- |
| Input: | (int) nTopologies | Number of topological entities in the topologies argument |
| Input: | (int*) topologies | Array of topologies (see swTopoEntity_e), one for each topological entity |
| Input: | (double*) edgeTolArray | Array of tolerances for edges |
| Input: | (double*) vertexTolArray | Array of tolerances for vertices |
| Input: | (double*) pointArray | Array of coordinates of vertices (geometry for vertices) |
| Input: | (LPCURVE*) curveArray | Array of curves (geometry for edges) |
| Input: | (LPSURFACE*) surfaceArray | Array of surfaces (geometry for faces) |
| Input: | (int) nRelations | Number of 1-to-1 relationships between topological entities |
| Input: | (int*) parents | Array of parents, one in each relationship |
| Input: | (int*) children | Array of children, one in each relationship |
| Input: | (int*) senses | Array of senses in which child is used by parent in the relationship |
| Output: | (LPBODY) retval | Pointer to the resulting body |
| Return: | (HRESULT) status | S_OK if Successful |

Remarks

If non-negative values are packed into the edgeTolArray and vertexTolArray arrays, then tolerances are applied to the corresponding edges or vertices. These arrays should be the same size as curveArray and pointArray, respectively. Otherwise, a default value of 1.0e-8 (modeler precision) is used.

NOTE: Modeler::SetInitKnitGapWidth does not affect this method.

Useful methods for creating geometry for the topological entities are:

- Body2::CreatePlanarSurface
- Body2::AddProfileArc
- Body2::AddProfileLine
- Body2::CreateRevolutionSurface

For example, to create a cone, find topological relationships and form relevant arrays. A complete solid cone consists of 8 topological entities:

There are 8 relations:

The topologies array:

| Index | Value |
| --- | --- |
| 0 | swTopoShell |
| 1 | swTopoFace |
| 2 | swTopoFace |
| 3 | swTopoLoop |
| 4 | swTopoEdge |
| 5 | swTopoLoop |
| 6 | swTopoLoop |
| 7 | swTopoVertex |

The set of arrays:

| index | parents | children | senses | relation |
| --- | --- | --- | --- | --- |
| 0 | 0 | 1 | 0 | shell to face |
| 1 | 0 | 2 | 0 | shell to face |
| 2 | 1 | 3 | 0 | face to loop |
| 3 | 3 | 4 | -1 | loop to edge |
| 4 | 2 | 5 | 0 | face to loop |
| 5 | 2 | 6 | 0 | face to loop |
| 6 | 5 | 4 | 1 | loop to edge |
| 7 | 6 | 7 | 0 | loop to vertex |

Values in the parents and children arrays correspond to the indices of the topology array.
