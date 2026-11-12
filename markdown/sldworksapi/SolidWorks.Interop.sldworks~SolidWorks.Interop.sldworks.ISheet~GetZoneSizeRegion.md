---
title: "GetZoneSizeRegion Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "GetZoneSizeRegion"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetZoneSizeRegion.html"
---

# GetZoneSizeRegion Method (ISheet)

Gets the type of zone size region.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetZoneSizeRegion() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim value As System.Integer

value = instance.GetZoneSizeRegion()
```

### C#

```csharp
System.int GetZoneSizeRegion()
```

### C++/CLI

```cpp
System.int GetZoneSizeRegion();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of zone size region as defined by [swRegionType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRegionType_e.html)

## VBA Syntax

See [Sheet::GetZoneSizeRegion](ms-its:sldworksapivb6.chm::/Sldworks~Sheet~GetZoneSizeRegion.html).

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
