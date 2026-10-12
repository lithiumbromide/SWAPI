---
title: "GetLineThickness Method (IDrawingComponent)"
project: "SOLIDWORKS API Help"
interface: "IDrawingComponent"
member: "GetLineThickness"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetLineThickness.html"
---

# GetLineThickness Method (IDrawingComponent)

Gets the line thickness for the drawing component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineThickness( _
   ByVal LineFontOption As System.Integer, _
   ByRef Thickness As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingComponent
Dim LineFontOption As System.Integer
Dim Thickness As System.Double
Dim value As System.Integer

value = instance.GetLineThickness(LineFontOption, Thickness)
```

### C#

```csharp
System.int GetLineThickness(
   System.int LineFontOption,
   out System.double Thickness
)
```

### C++/CLI

```cpp
System.int GetLineThickness(
   System.int LineFontOption,
   [Out] System.double Thickness
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LineFontOption`: Line font style of the component as defined in [swDrawingComponentLineFontOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingComponentLineFontOption_e.html)
- `Thickness`: Thickness of line

### Return Value

Line weight style as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)

## VBA Syntax

See [DrawingComponent::GetLineThickness](ms-its:sldworksapivb6.chm::/sldworks~DrawingComponent~GetLineThickness.html).

## Examples

[Get Components in Drawing View (C#)](Get_Components_in_Drawing_View_Example_CSharp.htm)
[Get Components in Drawing View (VB.NET)](Get_Components_in_Drawing_View_Example_VBNET.htm)
[Get Components in Drawing View (VBA)](Get_Components_in_Drawing_View_Example_VB.htm)

## See Also

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.html)
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.html)
[IDrawingComponent::SetLineThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~SetLineThickness.html)
[IDrawingComponent::GetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetLineStyle.html)
[IDrawingComponent::SetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~SetLineStyle.html)
[IDrawingComponent::UseDocumentDefaults Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~UseDocumentDefaults.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
