---
title: "IsInducedBendingMomentIncluded Method (ICWEdgeWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWEdgeWeldConnector"
member: "IsInducedBendingMomentIncluded"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~IsInducedBendingMomentIncluded.html"
---

# IsInducedBendingMomentIncluded Method (ICWEdgeWeldConnector)

Gets whether to include the induced bending moment due to asymmetry of the joint loading.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsInducedBendingMomentIncluded( _
   ByRef ErrorCode As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWEdgeWeldConnector
Dim ErrorCode As System.Integer
Dim value As System.Boolean

value = instance.IsInducedBendingMomentIncluded(ErrorCode)
```

### C#

```csharp
System.bool IsInducedBendingMomentIncluded(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.bool IsInducedBendingMomentIncluded(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Error code as defined in [swsWeldResultErrorCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsWeldResultErrorCode_e.html)

### Return Value

True to include the induced bending moment, false to not

## VBA Syntax

See [CWEdgeWeldConnector::IsInducedBendingMomentIncluded](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWEdgeWeldConnector~IsInducedBendingMomentIncluded.html).

## Examples

See the [ICWEdgeWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html) examples.

## Remarks

This method is valid only for single sided welds.

## See Also

[ICWEdgeWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html)
[ICWEdgeWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector_members.html)
[ICWEdgeWeldConnector::SetInducedBendingMomentIncluded Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~SetInducedBendingMomentIncluded.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
