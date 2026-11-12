---
title: "GetTextHeightAtIndex Method (IDatumTargetSym)"
project: "SOLIDWORKS API Help"
interface: "IDatumTargetSym"
member: "GetTextHeightAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextHeightAtIndex.html"
---

# GetTextHeightAtIndex Method (IDatumTargetSym)

Gets the height of the text for the specified text in this datum target symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextHeightAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTargetSym
Dim Index As System.Integer
Dim value As System.Double

value = instance.GetTextHeightAtIndex(Index)
```

### C#

```csharp
System.double GetTextHeightAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double GetTextHeightAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the text; index begins at 0

### Return Value

Height of the text for the specified text in meters

## VBA Syntax

See [DatumTargetSym::GetTextHeightAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DatumTargetSym~GetTextHeightAtIndex.html).

## See Also

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.html)
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.html)
[IDatumTargetSym::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextAngleAtIndex.html)
[IDatumTargetSym::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextAtIndex.html)
[IDatumTargetSym::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextCount.html)
[IDatumTargetSym::GetTextInvertAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextInvertAtIndex.html)
[IDatumTargetSym::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextPositionAtIndex.html)
[IDatumTargetSym::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextRefPositionAtIndex.html)
[IDatumTargetSym::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~IGetTextPositionAtIndex.html)
