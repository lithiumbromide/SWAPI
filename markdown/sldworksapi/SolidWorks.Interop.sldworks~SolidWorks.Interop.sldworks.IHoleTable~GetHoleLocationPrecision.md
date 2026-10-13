---
title: "GetHoleLocationPrecision Method (IHoleTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleTable"
member: "GetHoleLocationPrecision"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~GetHoleLocationPrecision.html"
---

# GetHoleLocationPrecision Method (IHoleTable)

Gets the precision to use for location values for this hole table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHoleLocationPrecision() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTable
Dim value As System.Integer

value = instance.GetHoleLocationPrecision()
```

### C#

```csharp
System.int GetHoleLocationPrecision()
```

### C++/CLI

```cpp
System.int GetHoleLocationPrecision();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Precision to use for location values

## VBA Syntax

See [HoleTable::GetHoleLocationPrecision](ms-its:sldworksapivb6.chm::/sldworks~HoleTable~GetHoleLocationPrecision.html).

## See Also

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html)
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html)
[IHoleTable::GetHoleLocationUseDocPrecision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~GetHoleLocationUseDocPrecision.html)
[IHoleTable::SetHoleLocationPrecision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~SetHoleLocationPrecision.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
