---
title: "SetZoneSizeRegion Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "SetZoneSizeRegion"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetZoneSizeRegion.html"
---

# SetZoneSizeRegion Method (ISheet)

Sets the type of zone size region.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetZoneSizeRegion( _
   ByVal RegionType As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim RegionType As System.Integer
Dim value As System.Boolean

value = instance.SetZoneSizeRegion(RegionType)
```

### C#

```csharp
System.bool SetZoneSizeRegion(
   System.int RegionType
)
```

### C++/CLI

```cpp
System.bool SetZoneSizeRegion(
   System.int RegionType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RegionType`: Type of zone size region as defined by [swRegionType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRegionType_e.html)

### Return Value

True of zone size region successfully set, false if not

## VBA Syntax

See [Sheet::SetZoneSizeRegion](ms-its:sldworksapivb6.chm::/Sldworks~Sheet~SetZoneSizeRegion.html).

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
