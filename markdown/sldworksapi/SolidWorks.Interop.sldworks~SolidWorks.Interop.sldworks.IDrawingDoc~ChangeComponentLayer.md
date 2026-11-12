---
title: "ChangeComponentLayer Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "ChangeComponentLayer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ChangeComponentLayer.html"
---

# ChangeComponentLayer Method (IDrawingDoc)

Puts the selected components on the specified layer.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ChangeComponentLayer( _
   ByVal Layername As System.String, _
   ByVal AllViews As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Layername As System.String
Dim AllViews As System.Boolean

instance.ChangeComponentLayer(Layername, AllViews)
```

### C#

```csharp
void ChangeComponentLayer(
   System.string Layername,
   System.bool AllViews
)
```

### C++/CLI

```cpp
void ChangeComponentLayer(
   System.String^ Layername,
   System.bool AllViews
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Layername`: Name of layer for components
- `AllViews`: True changes the component layer for all views in the drawing, false changes only the selected view

## VBA Syntax

See [DrawingDoc::ChangeComponentLayer](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~ChangeComponentLayer.html).

## Examples

[Create Layer for Selected View (VBA)](Create_Layer_for_Selected_View_Example_VB.htm)

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::OnComponentProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~OnComponentProperties.html)
[IDrawingDoc::ResolveOutOfDateLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ResolveOutOfDateLightWeightComponents.html)
[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
