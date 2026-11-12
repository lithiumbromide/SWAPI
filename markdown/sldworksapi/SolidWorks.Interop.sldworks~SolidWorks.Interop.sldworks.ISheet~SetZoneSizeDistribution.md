---
title: "SetZoneSizeDistribution Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "SetZoneSizeDistribution"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetZoneSizeDistribution.html"
---

# SetZoneSizeDistribution Method (ISheet)

Sets the zone size distribution.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetZoneSizeDistribution( _
   ByVal Type As System.Integer, _
   ByVal Rows As System.Integer, _
   ByVal Column As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim Type As System.Integer
Dim Rows As System.Integer
Dim Column As System.Integer
Dim value As System.Boolean

value = instance.SetZoneSizeDistribution(Type, Rows, Column)
```

### C#

```csharp
System.bool SetZoneSizeDistribution(
   System.int Type,
   System.int Rows,
   System.int Column
)
```

### C++/CLI

```cpp
System.bool SetZoneSizeDistribution(
   System.int Type,
   System.int Rows,
   System.int Column
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of zone size distribution as defined by [swZoneSizeDistribution_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swZoneSizeDistribution_e.html)
- `Rows`: Number of zone rows; valid only if Type is swZoneSizeDistribution.swZoneSizeDistribution_EvenlySized
- `Column`: Number of zone columns; valid only if Type is swZoneSizeDistribution.swZoneSizeDistribution_EvenlySized

### Return Value

True if zone size distribution successfully set, false if not

## VBA Syntax

See [Sheet::SetZoneSizeDistribution](ms-its:sldworksapivb6.chm::/Sldworks~Sheet~SetZoneSizeDistribution.html).

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
