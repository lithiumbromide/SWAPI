---
title: "IGetLineSegmentCount Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "IGetLineSegmentCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetLineSegmentCount.html"
---

# IGetLineSegmentCount Method (IDrSection)

Gets the number of line segments making up this section line.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLineSegmentCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Integer

value = instance.IGetLineSegmentCount()
```

### C#

```csharp
System.int IGetLineSegmentCount()
```

### C++/CLI

```cpp
System.int IGetLineSegmentCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of line segments in this section line

## VBA Syntax

See [DrSection::IGetLineSegmentCount](ms-its:sldworksapivb6.chm::/sldworks~DrSection~IGetLineSegmentCount.html).

## Remarks

Use this method to determine the size of the array you need to allocate for the output of [IDrSection::IGetLineInfo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection~IGetLineInfo.html). The size of the array to allocate is (6 * the value returned by this method).

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::GetLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetLineInfo.html)
[IDrSection::ISetLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ISetLineInfo.html)
[IDrSection::SetLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetLineInfo.html)
[IView::GetSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLines.html)
[IView::EnumSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumSectionLines.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
