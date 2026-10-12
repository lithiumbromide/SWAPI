---
title: "EditBalloonProperties2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "EditBalloonProperties2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditBalloonProperties2.html"
---

# EditBalloonProperties2 Method (IModelDocExtension)

Edits the selected balloon's properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function EditBalloonProperties2( _
   ByVal Style As System.Integer, _
   ByVal Size As System.Integer, _
   ByVal UpperTextStyle As System.Integer, _
   ByVal UpperText As System.String, _
   ByVal LowerTextStyle As System.Integer, _
   ByVal LowerText As System.String, _
   ByVal CustomSize As System.Double, _
   ByVal ShowQuantity As System.Boolean, _
   ByVal QuantityPlacement As System.Short, _
   ByVal QuantityDenotationText As System.String, _
   ByVal QuantityDistance As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Style As System.Integer
Dim Size As System.Integer
Dim UpperTextStyle As System.Integer
Dim UpperText As System.String
Dim LowerTextStyle As System.Integer
Dim LowerText As System.String
Dim CustomSize As System.Double
Dim ShowQuantity As System.Boolean
Dim QuantityPlacement As System.Short
Dim QuantityDenotationText As System.String
Dim QuantityDistance As System.Double
Dim value As System.Object

value = instance.EditBalloonProperties2(Style, Size, UpperTextStyle, UpperText, LowerTextStyle, LowerText, CustomSize, ShowQuantity, QuantityPlacement, QuantityDenotationText, QuantityDistance)
```

### C#

```csharp
System.object EditBalloonProperties2(
   System.int Style,
   System.int Size,
   System.int UpperTextStyle,
   System.string UpperText,
   System.int LowerTextStyle,
   System.string LowerText,
   System.double CustomSize,
   System.bool ShowQuantity,
   System.short QuantityPlacement,
   System.string QuantityDenotationText,
   System.double QuantityDistance
)
```

### C++/CLI

```cpp
System.Object^ EditBalloonProperties2(
   System.int Style,
   System.int Size,
   System.int UpperTextStyle,
   System.String^ UpperText,
   System.int LowerTextStyle,
   System.String^ LowerText,
   System.double CustomSize,
   System.bool ShowQuantity,
   System.short QuantityPlacement,
   System.String^ QuantityDenotationText,
   System.double QuantityDistance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Style`: Style of balloon as defined in [swBalloonStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonStyle_e.html)
- `Size`: Balloon size as defined in [swBalloonFit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html)
- `UpperTextStyle`: Balloon text style as defined in [swBalloonTextContent_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html)
- `UpperText`: Text for the balloon; valid only if UpperTextStyle is one of the following:

  - swBalloonTextContent_e.swBalloonTextCustom
  - swBalloonTextContent_e.swBalloonTextCustomProperties
  - swBalloonTextContent_e.swBalloonTextCutListProperties
- `LowerTextStyle`: Lower text style as defined in [swBalloonTextContent_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html); valid only if Style is swBalloonStyle_e.swBS_SplitCirc
- `LowerText`: Text for the lower text in the balloon; valid only if Style is swBalloonStyle_e.swBS_SplitCirc and LowerTextStyle is one of the following:

  - swBalloonTextContent_e.swBalloonTextCustom
  - swBalloonTextContent_e.swBalloonTextCustomProperties
  - swBalloonTextContent_e.swBalloonTextCutListProperties
- `CustomSize`: User-defined size of the balloon; valid only if Size is swBalloonFit_e.swBF_UserDef
- `ShowQuantity`: True to show quantity, false to not
- `QuantityPlacement`: Placement of quantity value as defined in [swBalloonQuantityPlacement_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonQuantityPlacement_e.html); valid only if ShowQuantity is true
- `QuantityDenotationText`: Denotation text for quantity; valid only if ShowQuantity is true
- `QuantityDistance`: Distance between the balloon and the quantity; valid only if ShowQuantity is true

### Return Value

[Note](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)

## VBA Syntax

See [ModelDocExtension::EditBalloonProperties2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~EditBalloonProperties2.html).

## Examples

[Edit Balloon (VBA)](Edit_Balloon_Example_VB.htm)
[Edit Balloon (VB.NET)](Edit_Balloon_Example_VBNET.htm)
[Edit Balloon (C#)](Edit_Balloon_Example_CSharp.htm)

## Remarks

Before calling this method, select the balloon annotation whose properties you want to edit.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[INote::SetBalloon Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBalloon.html)
[INote::SetBomBalloonText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBomBalloonText.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
