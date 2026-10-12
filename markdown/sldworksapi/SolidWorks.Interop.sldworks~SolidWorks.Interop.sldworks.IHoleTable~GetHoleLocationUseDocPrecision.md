---
title: "GetHoleLocationUseDocPrecision Method (IHoleTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleTable"
member: "GetHoleLocationUseDocPrecision"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~GetHoleLocationUseDocPrecision.html"
---

# GetHoleLocationUseDocPrecision Method (IHoleTable)

Gets whether to display the location of this hole table using the document's location precision.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHoleLocationUseDocPrecision() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTable
Dim value As System.Boolean

value = instance.GetHoleLocationUseDocPrecision()
```

### C#

```csharp
System.bool GetHoleLocationUseDocPrecision()
```

### C++/CLI

```cpp
System.bool GetHoleLocationUseDocPrecision();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True to display the location of this hole table using the document's location precision, false to not

## VBA Syntax

See [HoleTable::GetHoleLocationUseDocPrecision](ms-its:sldworksapivb6.chm::/sldworks~HoleTable~GetHoleLocationUseDocPrecision.html).

## See Also

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html)
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html)
[IHoleTable::GetHoleLocationPrecision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~GetHoleLocationPrecision.html)
[IHoleTable::SetHoleLocationPrecision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~SetHoleLocationPrecision.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
