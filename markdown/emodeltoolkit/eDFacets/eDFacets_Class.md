---
title: "eDFacets Class"
project: ""
interface: "eDFacets"
member: ""
kind: "class"
source: "emodeltoolkit/eDFacets/eDFacets_Class.htm"
---

# eDFacets Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Represents one or more set of planar polygonal facets.

#### Header file code

```vb
class eDFacets
{
public:

eDFacetsType facetstype;

int nvertices;

eDPt3d * vertexdata; //length = nvertices

int nfacetdata;

int * facetdata; //length = nfacetdata

eDPt3d * vertexnormaldata; //length = nvertices, optional

eDColorRGB * vertexcolors; //length = nvertices, optional

int ntexturecoords;

int ntextureparams;

float * texturecoords; //length = ntexturecoords x ntextureparams, optional

eDFacets();

};
```
