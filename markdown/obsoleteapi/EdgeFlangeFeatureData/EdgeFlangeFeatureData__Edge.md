---
title: "EdgeFlangeFeatureData::Edge"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/EdgeFlangeFeatureData/EdgeFlangeFeatureData__Edge.htm"
---

# EdgeFlangeFeatureData::Edge

This property is obsolete and has been superseded by [EdgeFlangeFeatureData::Edges](..\Edge\sldworksAPI.chm::\EdgeFlangeFeatureData\EdgeFlangeFeatureData__Edges.htm), [EdgeFlangeFeatureData::IGetEdges](..\Edge\sldworksAPI.chm::\EdgeFlangeFeatureData\EdgeFlangeFeatureData__IGetEdges.htm), and [EdgeFlangeFeatureData::ISetEdges](..\Edge\sldworksAPI.chm::\EdgeFlangeFeatureData\EdgeFlangeFeatureData__ISetEdges.htm).

Description

This property gets or sets the edge for this edge flange feature.

Syntax (OLE Automation)

edge = EdgeFlangeFeatureData.Edge (VB Get property)

EdgeFlangeFeatureData.Edge = edge (VB Set property)

edge = EdgeFlangeFeatureData.GetEdge ( ) (C++ Get property)

EdgeFlangeFeatureData.SetEdge ( edge ) (C++ Set property)

| Property: | (LPDISPATCH) edge | Dispatch pointer to the edge |
| --- | --- | --- |

Syntax (COM)

status = EdgeFlangeFeatureData->get_Edge ( &edge )

status = EdgeFlangeFeatureData->put_Edge ( edge )

| Property: | (LPDISPATCH) edge | Pointer to the edge |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

See Accessing Selections that Define Features for details on using this property.
