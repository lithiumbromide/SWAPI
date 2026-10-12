---
title: "SetInducedBendingMomentIncluded Method (ICWEdgeWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWEdgeWeldConnector"
member: "SetInducedBendingMomentIncluded"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~SetInducedBendingMomentIncluded.html"
---

# SetInducedBendingMomentIncluded Method (ICWEdgeWeldConnector)

Sets whether to include the induced bending moment due to asymmetry of the joint loading.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetInducedBendingMomentIncluded( _
   ByVal BIncluded As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWEdgeWeldConnector
Dim BIncluded As System.Boolean
Dim value As System.Integer

value = instance.SetInducedBendingMomentIncluded(BIncluded)
```

### C#

```csharp
System.int SetInducedBendingMomentIncluded(
   System.bool BIncluded
)
```

### C++/CLI

```cpp
System.int SetInducedBendingMomentIncluded(
   System.bool BIncluded
)
```

### Parameters

- `BIncluded`: True to include the induced bending moment, false to not

### Return Value

Error code as defined in [swsWeldResultErrorCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsWeldResultErrorCode_e.html)

## VBA Syntax

See [CWEdgeWeldConnector::SetInducedBendingMomentIncluded](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWEdgeWeldConnector~SetInducedBendingMomentIncluded.html).

## Examples

See the [ICWEdgeWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html) examples.

## Remarks

This method is valid only for single sided welds.

## See Also

[ICWEdgeWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html)
[ICWEdgeWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector_members.html)
[ICWEdgeWeldConnector::IsInducedBendingMomentIncluded Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~IsInducedBendingMomentIncluded.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
