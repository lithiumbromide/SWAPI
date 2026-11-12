---
title: "IsWeldOrientation Method (ICWEdgeWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWEdgeWeldConnector"
member: "IsWeldOrientation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~IsWeldOrientation.html"
---

# IsWeldOrientation Method (ICWEdgeWeldConnector)

Gets whether to show the location of the weld with respect to the shell surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsWeldOrientation( _
   ByRef ErrorCode As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWEdgeWeldConnector
Dim ErrorCode As System.Integer
Dim value As System.Boolean

value = instance.IsWeldOrientation(ErrorCode)
```

### C#

```csharp
System.bool IsWeldOrientation(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.bool IsWeldOrientation(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Error code as defined in [swsWeldResultErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsWeldResultErrorCode_e.html)

### Return Value

True to show the location of the weld with respect to the shell surface, false to not

## VBA Syntax

See [CWEdgeWeldConnector::IsWeldOrientation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWEdgeWeldConnector~IsWeldOrientation.html).

## Examples

See the [ICWEdgeWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html) examples.

## Remarks

This method is valid only for single sided welds.

## See Also

[ICWEdgeWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html)
[ICWEdgeWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector_members.html)
[ICWEdgeWeldConnector::SetWeldOrientation Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~SetWeldOrientation.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
