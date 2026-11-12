---
title: "AddEdges Method (ICWEdgeWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWEdgeWeldConnector"
member: "AddEdges"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~AddEdges.html"
---

# AddEdges Method (ICWEdgeWeldConnector)

Adds the specified intersecting edges to this edge weld connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddEdges( _
   ByVal NEdgeWeldStyle As System.Integer, _
   ByVal Edges As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWEdgeWeldConnector
Dim NEdgeWeldStyle As System.Integer
Dim Edges As System.Object
Dim value As System.Integer

value = instance.AddEdges(NEdgeWeldStyle, Edges)
```

### C#

```csharp
System.int AddEdges(
   System.int NEdgeWeldStyle,
   System.object Edges
)
```

### C++/CLI

```cpp
System.int AddEdges(
   System.int NEdgeWeldStyle,
   System.Object^ Edges
)
```

### Parameters

- `NEdgeWeldStyle`: Type of edge weld as defined in [swsEdgeWeldConnectorTypes_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsEdgeWeldConnectorTypes_e.html)
- `Edges`: Array of edges (see **Remarks**)

### Return Value

Error code as defined in [swsWeldResultErrorCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsWeldResultErrorCode_e.html)

## VBA Syntax

See [CWEdgeWeldConnector::AddEdges](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWEdgeWeldConnector~AddEdges.html).

## Examples

See the [ICWEdgeWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html) examples.

## Remarks

Edges contains the edges that are between corresponding faces of the arrays returned by [ICWEdgeWeldConnector::GetFirstFace](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWEdgeWeldConnector~GetFirstFace.html) and [ICWEdgeWeldConnector::GetSecondFace](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWEdgeWeldConnector~GetSecondFace.html).

## See Also

[ICWEdgeWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html)
[ICWEdgeWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector_members.html)
[ICWEdgeWeldConnector::GetEdgeList Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~GetEdgeList.html)
[ICWEdgeWeldConnector::RemoveEdges Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~RemoveEdges.html)
[ICWEdgeWeldConnector::ReplaceFacesAndEdges Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~ReplaceFacesAndEdges.html)
[ICWEdgeWeldConnector::ReplaceFacesThenAutoGenerateTouchingEdges Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~ReplaceFacesThenAutoGenerateTouchingEdges.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
