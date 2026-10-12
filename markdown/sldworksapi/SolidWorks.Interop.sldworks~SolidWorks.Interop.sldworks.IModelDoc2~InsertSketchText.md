---
title: "InsertSketchText Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertSketchText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchText.html"
---

# InsertSketchText Method (IModelDoc2)

Inserts sketch text.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSketchText( _
   ByVal Ptx As System.Double, _
   ByVal Pty As System.Double, _
   ByVal Ptz As System.Double, _
   ByVal Text As System.String, _
   ByVal Alignment As System.Integer, _
   ByVal FlipDirection As System.Integer, _
   ByVal HorizontalMirror As System.Integer, _
   ByVal WidthFactor As System.Integer, _
   ByVal SpaceBetweenChars As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Ptx As System.Double
Dim Pty As System.Double
Dim Ptz As System.Double
Dim Text As System.String
Dim Alignment As System.Integer
Dim FlipDirection As System.Integer
Dim HorizontalMirror As System.Integer
Dim WidthFactor As System.Integer
Dim SpaceBetweenChars As System.Integer
Dim value As System.Object

value = instance.InsertSketchText(Ptx, Pty, Ptz, Text, Alignment, FlipDirection, HorizontalMirror, WidthFactor, SpaceBetweenChars)
```

### C#

```csharp
System.object InsertSketchText(
   System.double Ptx,
   System.double Pty,
   System.double Ptz,
   System.string Text,
   System.int Alignment,
   System.int FlipDirection,
   System.int HorizontalMirror,
   System.int WidthFactor,
   System.int SpaceBetweenChars
)
```

### C++/CLI

```cpp
System.Object^ InsertSketchText(
   System.double Ptx,
   System.double Pty,
   System.double Ptz,
   System.String^ Text,
   System.int Alignment,
   System.int FlipDirection,
   System.int HorizontalMirror,
   System.int WidthFactor,
   System.int SpaceBetweenChars
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ptx`: X coordinate of starting point of text block
- `Pty`: Y coordinate of starting point of text block
- `Ptz`: Z coordinate of starting point of text block
- `Text`: Text to insert (see **Remarks**)
- `Alignment`: - 0 = Left
  - 1 = Center
  - 2 = Right
  - 3 = Fully justified

  (see **Remarks**)
- `FlipDirection`: 1 to flip text vertically about the selected entity, 0 to not (see **Remarks**)
- `HorizontalMirror`: 1 to flip text horizontally, 0 to not
- `WidthFactor`: 6 <= Percentage by which to evenly widen each character in the text block < = 1667
- `SpaceBetweenChars`: 1 <= Percentage of space between each character in the text block <= 10000; valid only if Alignment != 3

### Return Value

[Sketch text](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchText.html)

## VBA Syntax

See [ModelDoc2::InsertSketchText](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertSketchText.html).

## Examples

[Insert Text At Angle (VBA)](Insert_Text_at_Angle_Example_VB.htm)
[Align Text With Line (VBA)](Align_Text_with_Line_Eample_VB.htm)
[Insert Sketch Text and Hole (VBA)](Insert_Sketch_Text_and_Hole_Example_VB.htm)
[Insert Sketch Text and Hole (VB.NET)](Insert_Sketch_Text_and_Hole_Example_VBNET.htm)
[Insert Sketch Text and Hole (C#)](Insert_Sketch_Text_and_Hole_Example_CSharp.htm)

## Remarks

Alignment and FlipDirection are valid only when a curve, edge, or sketch segment is selected. Text appears along the selected entity. If an entity is not selected, Text appears horizontally starting at the origin. [Select](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) the curve, edge, or sketch segment with Mark = 1.

See the SOLIDWORKS Design user**-interface help > Sketching > Sketch Entities > Sketch Text > SketchText PropertyManager** topic for more information about this functionality.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::DissolveSketchText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DissolveSketchText.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
