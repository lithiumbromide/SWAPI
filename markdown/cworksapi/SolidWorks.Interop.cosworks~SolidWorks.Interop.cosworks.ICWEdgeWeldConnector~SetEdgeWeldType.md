---
title: "SetEdgeWeldType Method (ICWEdgeWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWEdgeWeldConnector"
member: "SetEdgeWeldType"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~SetEdgeWeldType.html"
---

# SetEdgeWeldType Method (ICWEdgeWeldConnector)

Sets the weld type of this edge weld connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetEdgeWeldType( _
   ByVal NOption As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWEdgeWeldConnector
Dim NOption As System.Integer
Dim value As System.Integer

value = instance.SetEdgeWeldType(NOption)
```

### C#

```csharp
System.int SetEdgeWeldType(
   System.int NOption
)
```

### C++/CLI

```cpp
System.int SetEdgeWeldType(
   System.int NOption
)
```

### Parameters

- `NOption`: Weld type as defined in [swsEdgeWeldConnectorTypes_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsEdgeWeldConnectorTypes_e.html)

### Return Value

Error code as defined in [swsWeldResultErrorCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsWeldResultErrorCode_e.html)

## VBA Syntax

See [CWEdgeWeldConnector::SetEdgeWeldType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWEdgeWeldConnector~SetEdgeWeldType.html).

## Examples

See the [ICWEdgeWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html) examples.

## See Also

[ICWEdgeWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html)
[ICWEdgeWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector_members.html)
[ICWEdgeWeldConnector::GetEdgeWeldType Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~GetEdgeWeldType.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
