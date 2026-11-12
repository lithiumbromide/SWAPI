---
title: "SetLineThickness Method (IDrawingComponent)"
project: "SOLIDWORKS API Help"
interface: "IDrawingComponent"
member: "SetLineThickness"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~SetLineThickness.html"
---

# SetLineThickness Method (IDrawingComponent)

Sets the line thickness for the drawing component.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetLineThickness( _
   ByVal LineFontOption As System.Integer, _
   ByVal LineWeights As System.Integer, _
   ByVal Thickness As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingComponent
Dim LineFontOption As System.Integer
Dim LineWeights As System.Integer
Dim Thickness As System.Double

instance.SetLineThickness(LineFontOption, LineWeights, Thickness)
```

### C#

```csharp
void SetLineThickness(
   System.int LineFontOption,
   System.int LineWeights,
   System.double Thickness
)
```

### C++/CLI

```cpp
void SetLineThickness(
   System.int LineFontOption,
   System.int LineWeights,
   System.double Thickness
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LineFontOption`: Line font style of the component as defined in [swDrawingComponentLineFontOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingComponentLineFontOption_e.html)
- `LineWeights`: Line weight style as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)
- `Thickness`: Thickness of line; only valid if LineWeights set to swLW_CUSTOM

## VBA Syntax

See [DrawingComponent::SetLineThickness](ms-its:sldworksapivb6.chm::/sldworks~DrawingComponent~SetLineThickness.html).

## Examples

[Get Components in Drawing View (C#)](Get_Components_in_Drawing_View_Example_CSharp.htm)
[Get Components in Drawing View (VB.NET)](Get_Components_in_Drawing_View_Example_VBNET.htm)
[Get Components in Drawing View (VBA)](Get_Components_in_Drawing_View_Example_VB.htm)

## See Also

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.html)
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.html)
[IDrawingComponent::GetLineThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetLineThickness.html)
[IDrawingComponent::GetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetLineStyle.html)
[IDrawingComponent::SetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~SetLineStyle.html)
[IDrawingComponent::UseDocumentDefaults Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~UseDocumentDefaults.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
