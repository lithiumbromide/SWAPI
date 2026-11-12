---
title: "EditBalloonProperties Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "EditBalloonProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditBalloonProperties.html"
---

# EditBalloonProperties Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::EditBalloonProperties2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~EditBalloonProperties2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function EditBalloonProperties( _
   ByVal Style As System.Integer, _
   ByVal Size As System.Integer, _
   ByVal UpperTextStyle As System.Integer, _
   ByVal UpperText As System.String, _
   ByVal LowerTextStyle As System.Integer, _
   ByVal LowerText As System.String, _
   ByVal CustomSize As System.Double, _
   ByVal ShowQuantity As System.Boolean, _
   ByVal QuantityPlacement As System.Short, _
   ByVal QuantityDenotationText As System.String _
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
Dim value As System.Object

value = instance.EditBalloonProperties(Style, Size, UpperTextStyle, UpperText, LowerTextStyle, LowerText, CustomSize, ShowQuantity, QuantityPlacement, QuantityDenotationText)
```

### C#

```csharp
System.object EditBalloonProperties(
   System.int Style,
   System.int Size,
   System.int UpperTextStyle,
   System.string UpperText,
   System.int LowerTextStyle,
   System.string LowerText,
   System.double CustomSize,
   System.bool ShowQuantity,
   System.short QuantityPlacement,
   System.string QuantityDenotationText
)
```

### C++/CLI

```cpp
System.Object^ EditBalloonProperties(
   System.int Style,
   System.int Size,
   System.int UpperTextStyle,
   System.String^ UpperText,
   System.int LowerTextStyle,
   System.String^ LowerText,
   System.double CustomSize,
   System.bool ShowQuantity,
   System.short QuantityPlacement,
   System.String^ QuantityDenotationText
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Style`: Style of balloon as defined in [swBalloonStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonStyle_e.html)
- `Size`: Balloon size as defined in [swBalloonFit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html)
- `UpperTextStyle`: Upper text style as defined in [swBalloonTextContent_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html)
- `UpperText`: Text for the upper text in the balloon
- `LowerTextStyle`: Lower text style as defined in [swBalloonTextContent_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html); valid for balloons only and Style must be set to swBS_SplitCirc
- `LowerText`: Text for the lower text in the balloon; valid for balloons only and Style must be set to swBS_SplitCirc
- `CustomSize`: User-defined size of the balloon; Size must be set to swBF_UserDef
- `ShowQuantity`: True to show quantity, false to not
- `QuantityPlacement`: Placement of quantity value:

  - 0 = Left
  - 1 = Right
  - 2 = Top
  - 3 = Bottom
- `QuantityDenotationText`: Denotation text for quantity

### Return Value

[Note](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)

## VBA Syntax

See [ModelDocExtension::EditBalloonProperties](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~EditBalloonProperties.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[INote::SetBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBalloon.html)
[INote::SetBomBalloonText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBomBalloonText.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
