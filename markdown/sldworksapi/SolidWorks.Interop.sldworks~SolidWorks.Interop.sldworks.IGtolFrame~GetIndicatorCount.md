---
title: "GetIndicatorCount Method (IGtolFrame)"
project: "SOLIDWORKS API Help"
interface: "IGtolFrame"
member: "GetIndicatorCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~GetIndicatorCount.html"
---

# GetIndicatorCount Method (IGtolFrame)

Gets the number of indicators in this Gtol frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIndicatorCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IGtolFrame
Dim value As System.Integer

value = instance.GetIndicatorCount()
```

### C#

```csharp
System.int GetIndicatorCount()
```

### C++/CLI

```cpp
System.int GetIndicatorCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of indicators in this Gtol frame

## VBA Syntax

See [GtolFrame::GetIndicatorCount](ms-its:sldworksapivb6.chm::/sldworks~GtolFrame~GetIndicatorCount.html).

## Examples

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html) examples.

## Remarks

Use this method to determine IndicatorIndex parameters before calling:

- [IGtolFrame::DeleteIndicator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~DeleteIndicator.html)
- [IGtolFrame::GetIndicator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~GetIndicator.html)
- [IGtolFrame::SetIndicator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~SetIndicator.html)

## See Also

[IGtolFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html)
[IGtolFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
