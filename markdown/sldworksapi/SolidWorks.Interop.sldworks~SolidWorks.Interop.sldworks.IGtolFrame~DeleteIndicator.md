---
title: "DeleteIndicator Method (IGtolFrame)"
project: "SOLIDWORKS API Help"
interface: "IGtolFrame"
member: "DeleteIndicator"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~DeleteIndicator.html"
---

# DeleteIndicator Method (IGtolFrame)

Deletes the tolerance indicator at the specified Gtol frame indicator index.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteIndicator( _
   ByVal IndicatorIndex As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtolFrame
Dim IndicatorIndex As System.Integer
Dim value As System.Boolean

value = instance.DeleteIndicator(IndicatorIndex)
```

### C#

```csharp
System.bool DeleteIndicator(
   System.int IndicatorIndex
)
```

### C++/CLI

```cpp
System.bool DeleteIndicator(
   System.int IndicatorIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IndicatorIndex`: One-based index of tolerance indicator to delete from the frame

### Return Value

True if tolerance indicator successfully deleted, false if not

## VBA Syntax

See [GtolFrame::DeleteIndicator](ms-its:sldworksapivb6.chm::/sldworks~GtolFrame~DeleteIndicator.html).

## Examples

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html) examples.

## Remarks

Before calling this method, use [IGtolFrame:GetIndicatorCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~GetIndicatorCount.html) to determine IndicatorIndex.

## See Also

[IGtolFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html)
[IGtolFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
