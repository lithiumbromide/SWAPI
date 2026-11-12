---
title: "SetTargetArea Method (IDatumTargetSym)"
project: "SOLIDWORKS API Help"
interface: "IDatumTargetSym"
member: "SetTargetArea"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetTargetArea.html"
---

# SetTargetArea Method (IDatumTargetSym)

Sets the datum target area style and size.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTargetArea( _
   ByVal Shape As System.Integer, _
   ByVal Size1 As System.String, _
   ByVal Size2 As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTargetSym
Dim Shape As System.Integer
Dim Size1 As System.String
Dim Size2 As System.String
Dim value As System.Boolean

value = instance.SetTargetArea(Shape, Size1, Size2)
```

### C#

```csharp
System.bool SetTargetArea(
   System.int Shape,
   System.string Size1,
   System.string Size2
)
```

### C++/CLI

```cpp
System.bool SetTargetArea(
   System.int Shape,
   System.String^ Size1,
   System.String^ Size2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Shape`: Target area shape or style as defined in [swDatumTargetAreaShape_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDatumTargetAreaShape_e.html)
- `Size1`: Target area diameter or width (see **Remarks**)
- `Size2`: Target area height (see Remarks)

### Return Value

True if the target area parameters were set successfully, false if they were not

## VBA Syntax

See [DatumTargetSym::SetTargetArea](ms-its:sldworksapivb6.chm::/sldworks~DatumTargetSym~SetTargetArea.html).

## Remarks

| If the target area style for this symbol is... | Then... |
| --- | --- |
| Point | There is one size value, which might be empty. Retrieve the text using an index value of 0. SOLIDWORKS displays the text in the upper half of the symbol, preceded by a diameter character. |
| Circle | There is one size value. Retrieve the text using an index value of 0. SOLIDWORKS displays the text in the upper half of the symbol, preceded by a diameter character. |
| Rectangle | There are two size values. Retrieve the text using an index value of 0 and 1. SOLIDWORKS displays the texts in the upper half of the symbol, separated by an x character. |

If the specified target area style is not one of the values in swDatumTargetAreaShape_e, SOLIDWORKS does not modify the symbol, and the returns false.

Use [IDatumTargetSym::GetTargetShape](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym~GetTargetShape.html) to get the target area style. Use [IDatumTargetSym::GetTargetAreaSize](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym~GetTargetAreaSize.html) to get the target area size.

To see the model or drawing changes, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw your window.

## See Also

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.html)
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
