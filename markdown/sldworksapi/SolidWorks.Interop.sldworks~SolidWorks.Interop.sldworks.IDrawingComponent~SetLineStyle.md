---
title: "SetLineStyle Method (IDrawingComponent)"
project: "SOLIDWORKS API Help"
interface: "IDrawingComponent"
member: "SetLineStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~SetLineStyle.html"
---

# SetLineStyle Method (IDrawingComponent)

Sets the line style for the drawing component.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetLineStyle( _
   ByVal LineFontOption As System.Integer, _
   ByVal Style As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingComponent
Dim LineFontOption As System.Integer
Dim Style As System.Integer

instance.SetLineStyle(LineFontOption, Style)
```

### C#

```csharp
void SetLineStyle(
   System.int LineFontOption,
   System.int Style
)
```

### C++/CLI

```cpp
void SetLineStyle(
   System.int LineFontOption,
   System.int Style
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LineFontOption`: Line font style of the component as defined in [swDrawingComponentLineFontOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingComponentLineFontOption_e.html)
- `Style`: Line style as defined in [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html)

## VBA Syntax

See [DrawingComponent::SetLineStyle](ms-its:sldworksapivb6.chm::/sldworks~DrawingComponent~SetLineStyle.html).

## Examples

[Get Components in Drawing View (C#)](Get_Components_in_Drawing_View_Example_CSharp.htm)
[Get Components in Drawing View (VB.NET)](Get_Components_in_Drawing_View_Example_VBNET.htm)
[Get Components in Drawing View (VBA)](Get_Components_in_Drawing_View_Example_VB.htm)

## See Also

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.html)
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.html)
[IDrawingComponent::GetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetLineStyle.html)
[IDrawingComponent::GetLineThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetLineThickness.html)
[IDrawingComponent::SetLineThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~SetLineThickness.html)
[IDrawingComponent::UseDocumentDefaults Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~UseDocumentDefaults.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
