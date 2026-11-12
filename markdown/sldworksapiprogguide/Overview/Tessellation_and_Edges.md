---
title: "Tessellation and Edges"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Tessellation_and_Edges.htm"
---

# Tessellation and Edges

A couple of approaches are available for finding tessellations for edges.

- Get the range of the curve and tessellate the curve along that range.

- or -

- Use [IFace2::GetTessTriStripEdges](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFace2~GetTessTriStripEdges.html) to get the indices into the tessellation that represents the edges of the face.

The first approach gives you better control over the edge. The second approach gives you a tight boundary if you are rendering edges and faces at the same time.
