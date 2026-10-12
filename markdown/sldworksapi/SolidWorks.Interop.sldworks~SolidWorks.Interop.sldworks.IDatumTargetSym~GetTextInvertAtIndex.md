---
title: "GetTextInvertAtIndex Method (IDatumTargetSym)"
project: "SOLIDWORKS API Help"
interface: "IDatumTargetSym"
member: "GetTextInvertAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextInvertAtIndex.html"
---

# GetTextInvertAtIndex Method (IDatumTargetSym)

Gets the invert flag for the specified text item.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextInvertAtIndex( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTargetSym
Dim Index As System.Integer
Dim value As System.Integer

value = instance.GetTextInvertAtIndex(Index)
```

### C#

```csharp
System.int GetTextInvertAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetTextInvertAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the text; index begins at 0

### Return Value

Invert flag

## VBA Syntax

See [DatumTargetSym::GetTextInvertAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DatumTargetSym~GetTextInvertAtIndex.html).

## Remarks

The invert flag specifies whether the text is mirrored (reflected) about the X axis. SOLIDWORKS Design applies reflection after text rotation.

## See Also

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.html)
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.html)
[IDatumTargetSym::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextAngleAtIndex.html)
[IDatumTargetSym::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextAtIndex.html)
[IDatumTargetSym::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextCount.html)
[IDatumTargetSym::GetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextHeightAtIndex.html)
[IDatumTargetSym::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextPositionAtIndex.html)
[IDatumTargetSym::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextRefPositionAtIndex.html)
[IDatumTargetSym::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~IGetTextPositionAtIndex.html)
