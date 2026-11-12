---
title: "ReplaceFacesAndEdges Method (ICWEdgeWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWEdgeWeldConnector"
member: "ReplaceFacesAndEdges"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~ReplaceFacesAndEdges.html"
---

# ReplaceFacesAndEdges Method (ICWEdgeWeldConnector)

Replaces the current faces and edges in this edge weld connector with the specified faces and edges.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReplaceFacesAndEdges( _
   ByVal NEdgeWeldStyle As System.Integer, _
   ByVal DispFace1 As System.Object, _
   ByVal DispFace2 As System.Object, _
   ByVal Edges As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWEdgeWeldConnector
Dim NEdgeWeldStyle As System.Integer
Dim DispFace1 As System.Object
Dim DispFace2 As System.Object
Dim Edges As System.Object
Dim value As System.Integer

value = instance.ReplaceFacesAndEdges(NEdgeWeldStyle, DispFace1, DispFace2, Edges)
```

### C#

```csharp
System.int ReplaceFacesAndEdges(
   System.int NEdgeWeldStyle,
   System.object DispFace1,
   System.object DispFace2,
   System.object Edges
)
```

### C++/CLI

```cpp
System.int ReplaceFacesAndEdges(
   System.int NEdgeWeldStyle,
   System.Object^ DispFace1,
   System.Object^ DispFace2,
   System.Object^ Edges
)
```

### Parameters

- `NEdgeWeldStyle`: Type of edge weld connector as defined in [swsEdgeWeldConnectorTypes_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsEdgeWeldConnectorTypes_e.html)
- `DispFace1`: Face Set 1 array
- `DispFace2`: Face Set 2 array
- `Edges`: Array of edges between faces specified in DispFace1 and DispFace2

### Return Value

Error code as defined in [swsWeldResultErrorCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsWeldResultErrorCode_e.html)

## VBA Syntax

See [CWEdgeWeldConnector::ReplaceFacesAndEdges](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWEdgeWeldConnector~ReplaceFacesAndEdges.html).

## Examples

See the [ICWEdgeWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html) examples.

## See Also

[ICWEdgeWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html)
[ICWEdgeWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector_members.html)
[ICWEdgeWeldConnector::ReplaceFacesThenAutoGenerateTouchingEdges Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~ReplaceFacesThenAutoGenerateTouchingEdges.html)
[ICWEdgeWeldConnector::AddEdges Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~AddEdges.html)
[ICWEdgeWeldConnector::RemoveEdges Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~RemoveEdges.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
