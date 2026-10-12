---
title: "SetCustomColor Method (IColorTable)"
project: "SOLIDWORKS API Help"
interface: "IColorTable"
member: "SetCustomColor"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~SetCustomColor.html"
---

# SetCustomColor Method (IColorTable)

Sets a custom color.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCustomColor( _
   ByVal Index As System.Integer, _
   ByVal ColorRef As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IColorTable
Dim Index As System.Integer
Dim ColorRef As System.Integer
Dim value As System.Boolean

value = instance.SetCustomColor(Index, ColorRef)
```

### C#

```csharp
System.bool SetCustomColor(
   System.int Index,
   System.int ColorRef
)
```

### C++/CLI

```cpp
System.bool SetCustomColor(
   System.int Index,
   System.int ColorRef
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the custom color to set
- `ColorRef`: COLORREF value

### Return Value

True if successful, false if not

## VBA Syntax

See [ColorTable::SetCustomColor](ms-its:sldworksapivb6.chm::/sldworks~ColorTable~SetCustomColor.html).

## See Also

[IColorTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable.html)
[IColorTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable_members.html)
[IColorTable::GetCustomColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCustomColors.html)
[IColorTable::IGetCustomColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~IGetCustomColors.html)
[IColorTable::GetCustomColorCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCustomColorCount.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
