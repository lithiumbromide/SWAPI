---
title: "RemoveEdges Method (ICWEdgeWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWEdgeWeldConnector"
member: "RemoveEdges"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~RemoveEdges.html"
---

# RemoveEdges Method (ICWEdgeWeldConnector)

Removes the specified edges from this edge weld connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveEdges( _
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

value = instance.RemoveEdges(NEdgeWeldStyle, Edges)
```

### C#

```csharp
System.int RemoveEdges(
   System.int NEdgeWeldStyle,
   System.object Edges
)
```

### C++/CLI

```cpp
System.int RemoveEdges(
   System.int NEdgeWeldStyle,
   System.Object^ Edges
)
```

### Parameters

- `NEdgeWeldStyle`: Type of edge weld as defined in [swsEdgeWeldConnectorTypes_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsEdgeWeldConnectorTypes_e.html)
- `Edges`: Array of edges to remove

### Return Value

Error code as defined in [swsWeldResultErrorCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsWeldResultErrorCode_e.html)

## VBA Syntax

See [CWEdgeWeldConnector::RemoveEdges](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWEdgeWeldConnector~RemoveEdges.html).

## Examples

See the [ICWEdgeWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html) examples.

## See Also

[ICWEdgeWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html)
[ICWEdgeWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector_members.html)
[ICWEdgeWeldConnector::AddEdges Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~AddEdges.html)
[ICWEdgeWeldConnector::ReplaceFacesAndEdges Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~ReplaceFacesAndEdges.html)
[ICWEdgeWeldConnector::ReplaceFacesThenAutoGenerateTouchingEdges Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~ReplaceFacesThenAutoGenerateTouchingEdges.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
