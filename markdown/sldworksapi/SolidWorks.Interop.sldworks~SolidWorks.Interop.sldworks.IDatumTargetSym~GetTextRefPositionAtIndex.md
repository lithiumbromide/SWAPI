---
title: "GetTextRefPositionAtIndex Method (IDatumTargetSym)"
project: "SOLIDWORKS API Help"
interface: "IDatumTargetSym"
member: "GetTextRefPositionAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextRefPositionAtIndex.html"
---

# GetTextRefPositionAtIndex Method (IDatumTargetSym)

Gets the reference position of the specified text item in this datum target symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextRefPositionAtIndex( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTargetSym
Dim Index As System.Integer
Dim value As System.Integer

value = instance.GetTextRefPositionAtIndex(Index)
```

### C#

```csharp
System.int GetTextRefPositionAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetTextRefPositionAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the text; index begins at 0

### Return Value

Reference position as defined in [swTextPosition_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTextPosition_e.html)

## VBA Syntax

See [DatumTargetSym::GetTextRefPositionAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DatumTargetSym~GetTextRefPositionAtIndex.html).

## See Also

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.html)
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.html)
[IDatumTargetSym::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextAngleAtIndex.html)
[IDatumTargetSym::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextAtIndex.html)
[IDatumTargetSym::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextCount.html)
[IDatumTargetSym::GetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextHeightAtIndex.html)
[IDatumTargetSym::GetTextInvertAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextInvertAtIndex.html)
[IDatumTargetSym::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextPositionAtIndex.html)
[IDatumTargetSym::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~IGetTextPositionAtIndex.html)
