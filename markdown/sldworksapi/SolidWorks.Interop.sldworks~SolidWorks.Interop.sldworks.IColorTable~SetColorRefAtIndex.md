---
title: "SetColorRefAtIndex Method (IColorTable)"
project: "SOLIDWORKS API Help"
interface: "IColorTable"
member: "SetColorRefAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~SetColorRefAtIndex.html"
---

# SetColorRefAtIndex Method (IColorTable)

Sets the specified color value within the color table.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetColorRefAtIndex( _
   ByVal Index As System.Integer, _
   ByVal ColorRef As System.Integer, _
   ByVal ApplyTo As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IColorTable
Dim Index As System.Integer
Dim ColorRef As System.Integer
Dim ApplyTo As System.Integer

instance.SetColorRefAtIndex(Index, ColorRef, ApplyTo)
```

### C#

```csharp
void SetColorRefAtIndex(
   System.int Index,
   System.int ColorRef,
   System.int ApplyTo
)
```

### C++/CLI

```cpp
void SetColorRefAtIndex(
   System.int Index,
   System.int ColorRef,
   System.int ApplyTo
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index value within the color table you want to modify
- `ColorRef`: COLORREF value
- `ApplyTo`: Not used; specify 0

## VBA Syntax

See [ColorTable::SetColorRefAtIndex](ms-its:sldworksapivb6.chm::/sldworks~ColorTable~SetColorRefAtIndex.html).

## See Also

[IColorTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable.html)
[IColorTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable_members.html)
[IColorTable::GetColorRefAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetColorRefAtIndex.html)

## Availability

SOLIDWORKS 99, datecode 1999207
