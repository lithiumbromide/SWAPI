---
title: "GetZoneSizeDistribution Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "GetZoneSizeDistribution"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetZoneSizeDistribution.html"
---

# GetZoneSizeDistribution Method (ISheet)

Gets the zone size distribution.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetZoneSizeDistribution( _
   ByRef Rows As System.Integer, _
   ByRef Columns As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim Rows As System.Integer
Dim Columns As System.Integer
Dim value As System.Integer

value = instance.GetZoneSizeDistribution(Rows, Columns)
```

### C#

```csharp
System.int GetZoneSizeDistribution(
   out System.int Rows,
   out System.int Columns
)
```

### C++/CLI

```cpp
System.int GetZoneSizeDistribution(
   [Out] System.int Rows,
   [Out] System.int Columns
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Rows`: Zone rows; Nothing or null if the zone size distribution is swZoneSizeDistribution_e.swZoneSizeDistribution_50mmFromCenter
- `Columns`: Zone columns; Nothing or null if the zone size distribution is swZoneSizeDistribution_e.swZoneSizeDistribution_50mmFromCenter

### Return Value

Zone size distribution as defined by [swZoneSizeDistribution_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swZoneSizeDistribution_e.html)

## VBA Syntax

See [Sheet::GetZoneSizeDistribution](ms-its:sldworksapivb6.chm::/Sldworks~Sheet~GetZoneSizeDistribution.html).

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
