---
title: "SetWeldOrientation Method (ICWEdgeWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWEdgeWeldConnector"
member: "SetWeldOrientation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~SetWeldOrientation.html"
---

# SetWeldOrientation Method (ICWEdgeWeldConnector)

Sets the position of the weld with respect to the shell surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetWeldOrientation( _
   ByVal BOrientation As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWEdgeWeldConnector
Dim BOrientation As System.Boolean
Dim value As System.Integer

value = instance.SetWeldOrientation(BOrientation)
```

### C#

```csharp
System.int SetWeldOrientation(
   System.bool BOrientation
)
```

### C++/CLI

```cpp
System.int SetWeldOrientation(
   System.bool BOrientation
)
```

### Parameters

- `BOrientation`: True to weld on Side 1, false to weld on Side 2

### Return Value

Error code as defined in [swsWeldResultErrorCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsWeldResultErrorCode_e.html)

## VBA Syntax

See [CWEdgeWeldConnector::SetWeldOrientation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWEdgeWeldConnector~SetWeldOrientation.html).

## Examples

See the [ICWEdgeWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html) examples.

## Remarks

This method is valid only for single sided welds.

## See Also

[ICWEdgeWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector.html)
[ICWEdgeWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector_members.html)
[ICWEdgeWeldConnector::IsWeldOrientation Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWEdgeWeldConnector~IsWeldOrientation.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
