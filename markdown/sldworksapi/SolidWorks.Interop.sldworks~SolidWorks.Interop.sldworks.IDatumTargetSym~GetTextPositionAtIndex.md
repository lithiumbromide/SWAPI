---
title: "GetTextPositionAtIndex Method (IDatumTargetSym)"
project: "SOLIDWORKS API Help"
interface: "IDatumTargetSym"
member: "GetTextPositionAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextPositionAtIndex.html"
---

# GetTextPositionAtIndex Method (IDatumTargetSym)

Gets the offset for the text item relative to the text point of the note.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextPositionAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTargetSym
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetTextPositionAtIndex(Index)
```

### C#

```csharp
System.object GetTextPositionAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetTextPositionAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the text index begins at 0

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [DatumTargetSym::GetTextPositionAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DatumTargetSym~GetTextPositionAtIndex.html).

## Remarks

The return value is the following array of doubles:

**[** `textPtX, textPtY, textPtZ` **]**

where these text position values are actually offset values from the origin of this datum target symbol.

## See Also

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.html)
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.html)
[IDatumTargetSym::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextAngleAtIndex.html)
[IDatumTargetSym::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextAtIndex.html)
[IDatumTargetSym::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextCount.html)
[IDatumTargetSym::GetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextHeightAtIndex.html)
[IDatumTargetSym::GetTextInvertAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextInvertAtIndex.html)
[IDatumTargetSym::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextRefPositionAtIndex.html)
[IDatumTargetSym::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~IGetTextPositionAtIndex.html)
