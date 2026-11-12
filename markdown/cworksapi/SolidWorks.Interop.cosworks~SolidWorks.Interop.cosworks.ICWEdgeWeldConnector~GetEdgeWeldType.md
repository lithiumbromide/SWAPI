---
title: "GetEdgeWeldType Method (ICWEdgeWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWEdgeWeldConnector"
member: "GetEdgeWeldType"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~GetEdgeWeldType.html"
---

# GetEdgeWeldType Method (ICWEdgeWeldConnector)

Gets the weld type of this edge weld connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgeWeldType( _
   ByRef ErrorCode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWEdgeWeldConnector
Dim ErrorCode As System.Integer
Dim value As System.Integer

value = instance.GetEdgeWeldType(ErrorCode)
```

### C#

```csharp
System.int GetEdgeWeldType(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.int GetEdgeWeldType(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Error code as defined in [swsWeldResultErrorCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsWeldResultErrorCode_e.html)

### Return Value

Weld type as defined in [swsEdgeWeldConnectorTypes_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsEdgeWeldConnectorTypes_e.html)

## VBA Syntax

See [CWEdgeWeldConnector::GetEdgeWeldType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWEdgeWeldConnector~GetEdgeWeldType.html).

## Examples

See the [ICWEdgeWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html) examples.

## See Also

[ICWEdgeWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html)
[ICWEdgeWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector_members.html)
[ICWEdgeWeldConnector::SetEdgeWeldType Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~SetEdgeWeldType.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
