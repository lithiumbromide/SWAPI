---
title: "GetFirstFace Method (ICWEdgeWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWEdgeWeldConnector"
member: "GetFirstFace"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~GetFirstFace.html"
---

# GetFirstFace Method (ICWEdgeWeldConnector)

Gets the array of faces in Face Set1.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstFace( _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWEdgeWeldConnector
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetFirstFace(ErrorCode)
```

### C#

```csharp
System.object GetFirstFace(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetFirstFace(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Error code as defined in [swsWeldResultErrorCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsWeldResultErrorCode_e.html)

### Return Value

Face Set1 array

## VBA Syntax

See [CWEdgeWeldConnector::GetFirstFace](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWEdgeWeldConnector~GetFirstFace.html).

## Examples

See the [ICWEdgeWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html) examples.

## Remarks

The faces returned by this method are related to the Face Set2 faces returned by [ICWEdgeWeldConnector::GetSecondFace](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWEdgeWeldConnector~GetSecondFace.html) as follows:

| If ICWEdgeWeldConnector::GetEdgeWeldType is swsEdgeWeldConnectorTypes_e ... | Then the faces in Face Set1 and Face Set2 are... |
| --- | --- |
| swsEdgeWeldConnectorFilletDoubleSided or swsEdgeWeldConnectorFilletSingleSided | Perpendicular |
| swsEdgeWeldConnectorGrooveDoubleSided or swsEdgeWeldConnectorGrooveSingleSided | Parallel |

## See Also

[ICWEdgeWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html)
[ICWEdgeWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector_members.html)
[ICWEdgeWeldConnector::GetEdgeList Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~GetEdgeList.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
