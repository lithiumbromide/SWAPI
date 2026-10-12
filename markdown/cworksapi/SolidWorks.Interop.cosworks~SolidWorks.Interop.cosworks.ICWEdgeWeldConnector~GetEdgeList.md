---
title: "GetEdgeList Method (ICWEdgeWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWEdgeWeldConnector"
member: "GetEdgeList"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~GetEdgeList.html"
---

# GetEdgeList Method (ICWEdgeWeldConnector)

Gets the array of intersecting edges in this edge weld connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgeList( _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWEdgeWeldConnector
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetEdgeList(ErrorCode)
```

### C#

```csharp
System.object GetEdgeList(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetEdgeList(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Error code as defined in [swsWeldResultErrorCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsWeldResultErrorCode_e.html)

### Return Value

Array of intersecting edges

## VBA Syntax

See [CWEdgeWeldConnector::GetEdgeList](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWEdgeWeldConnector~GetEdgeList.html).

## Examples

See the [ICWEdgeWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html) examples.

## Remarks

This method returns the edges that are between corresponding faces of the arrays returned by [ICWEdgeWeldConnector::GetFirstFace](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWEdgeWeldConnector~GetFirstFace.html) and [ICWEdgeWeldConnector::GetSecondFace](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWEdgeWeldConnector~GetSecondFace.html).

## See Also

[ICWEdgeWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html)
[ICWEdgeWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector_members.html)
[ICWEdgeWeldConnector::AddEdges Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~AddEdges.html)
[ICWEdgeWeldConnector::RemoveEdges Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~RemoveEdges.html)
[ICWEdgeWeldConnector::ReplaceFacesAndEdges Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~ReplaceFacesAndEdges.html)
[ICWEdgeWeldConnector::ReplaceFacesThenAutoGenerateTouchingEdges Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~ReplaceFacesThenAutoGenerateTouchingEdges.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
