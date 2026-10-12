---
title: "SetText Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SetText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetText.html"
---

# SetText Method (IDisplayDimension)

Sets the text above the dimension line in a display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetText( _
   ByVal WhichText As System.Integer, _
   ByVal Text As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim WhichText As System.Integer
Dim Text As System.String

instance.SetText(WhichText, Text)
```

### C#

```csharp
void SetText(
   System.int WhichText,
   System.string Text
)
```

### C++/CLI

```cpp
void SetText(
   System.int WhichText,
   System.String^ Text
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichText`: Aspect of the text to get as defined in [swDimensionTextParts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionTextParts_e.html) (see **Remarks**)
- `Text`: Text to create above the dimension line

## VBA Syntax

See [DisplayDimension::SetText](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SetText.html).

## Examples

[Display Grid Bubble (VBA)](Display_Grid_Bubble_Example_VB.htm)

## Remarks

Use swDimensionTextParts_e.swDimensionTextAll to create or replace the entire dimension text. SOLIDWORKS places the input text in the prefix portion of the dimension text, clears the suffix and callout texts, and turns off the dimension value (see [IDisplayDimension::ShowDimensionValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~ShowDimensionValue.html)).

After using this method, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

**NOTE:** This method does not support [hole callouts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.html).

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetText.html)
[IDisplayDimension::SetLowerText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLowerText.html)
[IDisplayDimension::GetLowerText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetLowerText.html)
