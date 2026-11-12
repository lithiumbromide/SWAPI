---
title: "SetHoleLocationPrecision Method (IHoleTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleTable"
member: "SetHoleLocationPrecision"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~SetHoleLocationPrecision.html"
---

# SetHoleLocationPrecision Method (IHoleTable)

Sets the precision to use for location values for this hole table.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetHoleLocationPrecision( _
   ByVal UseDoc As System.Boolean, _
   ByVal Precision As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTable
Dim UseDoc As System.Boolean
Dim Precision As System.Integer
Dim value As System.Boolean

value = instance.SetHoleLocationPrecision(UseDoc, Precision)
```

### C#

```csharp
System.bool SetHoleLocationPrecision(
   System.bool UseDoc,
   System.int Precision
)
```

### C++/CLI

```cpp
System.bool SetHoleLocationPrecision(
   System.bool UseDoc,
   System.int Precision
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDoc`: True to set the location for this hole table using the document's precision, false
  to not
- `Precision`: Precision to use for location values if UseDoc set to false

### Return Value

True if precision is set, false if not

## VBA Syntax

See [HoleTable::SetHoleLocationPrecision](ms-its:sldworksapivb6.chm::/sldworks~HoleTable~SetHoleLocationPrecision.html).

## See Also

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html)
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html)
[IHoleTable::GetHoleLocationPrecision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~GetHoleLocationPrecision.html)
[IHoleTable::GetHoleLocationUseDocPrecision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~GetHoleLocationUseDocPrecision.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
