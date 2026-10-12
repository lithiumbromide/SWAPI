---
title: "InsertDatumTargetSymbol3 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "InsertDatumTargetSymbol3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertDatumTargetSymbol3.html"
---

# InsertDatumTargetSymbol3 Method (IModelDocExtension)

Creates a datum target symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertDatumTargetSymbol3( _
   ByVal Datum1 As System.String, _
   ByVal Datum2 As System.String, _
   ByVal Datum3 As System.String, _
   ByVal AreaStyle As System.Integer, _
   ByVal AreaOutside As System.Boolean, _
   ByVal Value1 As System.Double, _
   ByVal Value2 As System.Double, _
   ByVal ValueStr1 As System.String, _
   ByVal ValueStr2 As System.String, _
   ByVal ArrowsSmart As System.Boolean, _
   ByVal ArrowStyle As System.Integer, _
   ByVal LeaderLineStyle As System.Integer, _
   ByVal LeaderBent As System.Boolean, _
   ByVal ShowArea As System.Boolean, _
   ByVal ShowSymbol As System.Boolean, _
   ByVal MoveableDatumStyle As System.Integer _
) As DatumTargetSym
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Datum1 As System.String
Dim Datum2 As System.String
Dim Datum3 As System.String
Dim AreaStyle As System.Integer
Dim AreaOutside As System.Boolean
Dim Value1 As System.Double
Dim Value2 As System.Double
Dim ValueStr1 As System.String
Dim ValueStr2 As System.String
Dim ArrowsSmart As System.Boolean
Dim ArrowStyle As System.Integer
Dim LeaderLineStyle As System.Integer
Dim LeaderBent As System.Boolean
Dim ShowArea As System.Boolean
Dim ShowSymbol As System.Boolean
Dim MoveableDatumStyle As System.Integer
Dim value As DatumTargetSym

value = instance.InsertDatumTargetSymbol3(Datum1, Datum2, Datum3, AreaStyle, AreaOutside, Value1, Value2, ValueStr1, ValueStr2, ArrowsSmart, ArrowStyle, LeaderLineStyle, LeaderBent, ShowArea, ShowSymbol, MoveableDatumStyle)
```

### C#

```csharp
DatumTargetSym InsertDatumTargetSymbol3(
   System.string Datum1,
   System.string Datum2,
   System.string Datum3,
   System.int AreaStyle,
   System.bool AreaOutside,
   System.double Value1,
   System.double Value2,
   System.string ValueStr1,
   System.string ValueStr2,
   System.bool ArrowsSmart,
   System.int ArrowStyle,
   System.int LeaderLineStyle,
   System.bool LeaderBent,
   System.bool ShowArea,
   System.bool ShowSymbol,
   System.int MoveableDatumStyle
)
```

### C++/CLI

```cpp
DatumTargetSym^ InsertDatumTargetSymbol3(
   System.String^ Datum1,
   System.String^ Datum2,
   System.String^ Datum3,
   System.int AreaStyle,
   System.bool AreaOutside,
   System.double Value1,
   System.double Value2,
   System.String^ ValueStr1,
   System.String^ ValueStr2,
   System.bool ArrowsSmart,
   System.int ArrowStyle,
   System.int LeaderLineStyle,
   System.bool LeaderBent,
   System.bool ShowArea,
   System.bool ShowSymbol,
   System.int MoveableDatumStyle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Datum1`: Datum reference string 1
- `Datum2`: Datum reference string 2
- `Datum3`: Datum reference string 3
- `AreaStyle`: - 0 = point
  - 1 = circle
  - 2 = rectangle
- `AreaOutside`: True to display the target area outside, false to not
- `Value1`: Numeric datum target area diameter or width
- `Value2`: Numeric datum target area height
- `ValueStr1`: Value for datum target area diameter or width
- `ValueStr2`: Value for datum target area height
- `ArrowsSmart`: True to use smart arrows, false to not
- `ArrowStyle`: Arrowhead style as defined by [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)
- `LeaderLineStyle`: Leaderline style as defined by [swLeaderStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderStyle_e.html)
- `LeaderBent`: True to create a bent leader line, false to not
- `ShowArea`: True to show the target area, false to not
- `ShowSymbol`: True to display the target symbol, false to not
- `MoveableDatumStyle`: Moveable datum target symbol style as defined in [swMoveableDatumStyle_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMoveableDatumStyle_e.html)

### Return Value

[Datum target symbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym.html)

## VBA Syntax

See [ModelDocExtension::InsertDatumTargetSymbol3](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~InsertDatumTargetSymbol3.html).

## Examples

[Insert and Modify Datum Target Symbol (VBA)](Insert_and_Modify_Datum_Target_Symbol_Example_VB.htm)
[Insert and Modify Datum Target Symbol (VB.NET)](Insert_and_Modify_Datum_Target_Symbol_Example_VBNET.htm)
[Insert and Modify Datum Target Symbol (C#)](Insert_and_Modify_Datum_Target_Symbol_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
