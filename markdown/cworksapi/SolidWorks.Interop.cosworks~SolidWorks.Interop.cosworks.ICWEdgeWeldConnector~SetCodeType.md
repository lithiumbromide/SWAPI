---
title: "SetCodeType Method (ICWEdgeWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWEdgeWeldConnector"
member: "SetCodeType"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~SetCodeType.html"
---

# SetCodeType Method (ICWEdgeWeldConnector)

Sets the weld sizing standard for this edge weld connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCodeType( _
   ByVal NOption As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWEdgeWeldConnector
Dim NOption As System.Integer
Dim value As System.Integer

value = instance.SetCodeType(NOption)
```

### C#

```csharp
System.int SetCodeType(
   System.int NOption
)
```

### C++/CLI

```cpp
System.int SetCodeType(
   System.int NOption
)
```

### Parameters

- `NOption`: Weld sizing standard as defined in [swsEdgeWeldSolverCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsEdgeWeldSolverCode_e.html)

### Return Value

Error code as defined in [swsWeldResultErrorCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsWeldResultErrorCode_e.html)

## VBA Syntax

See [CWEdgeWeldConnector::SetCodeType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWEdgeWeldConnector~SetCodeType.html).

## Examples

See the [ICWEdgeWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html) examples.

## See Also

[ICWEdgeWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html)
[ICWEdgeWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector_members.html)
[ICWEdgeWeldConnector::GetCodeType Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~GetCodeType.html)
[ICWEdgeWeldConnector::GetWeldSizingSettingEuro Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~GetWeldSizingSettingEuro.html)
[ICWEdgeWeldConnector::GetWeldSizingSettingUS Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~GetWeldSizingSettingUS.html)
[ICWEdgeWeldConnector::SetWeldSizingSettingEuro Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~SetWeldSizingSettingEuro.html)
[ICWEdgeWeldConnector::SetWeldSizingSettingUS Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~SetWeldSizingSettingUS.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
