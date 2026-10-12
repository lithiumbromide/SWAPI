---
title: "UseDocumentDefaults Property (IDrawingComponent)"
project: "SOLIDWORKS API Help"
interface: "IDrawingComponent"
member: "UseDocumentDefaults"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~UseDocumentDefaults.html"
---

# UseDocumentDefaults Property (IDrawingComponent)

Gets or sets whether to use the document default settings for the component's line fonts.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseDocumentDefaults As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingComponent
Dim value As System.Boolean

instance.UseDocumentDefaults = value

value = instance.UseDocumentDefaults
```

### C#

```csharp
System.bool UseDocumentDefaults {get; set;}
```

### C++/CLI

```cpp
property System.bool UseDocumentDefaults {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the document default settings for the component's line fonts, false to use the selected settings

## VBA Syntax

See [DrawingComponent::UseDocumentDefaults](ms-its:sldworksapivb6.chm::/sldworks~DrawingComponent~UseDocumentDefaults.html).

## Examples

[Get Components in Drawing View (C#)](Get_Components_in_Drawing_View_Example_CSharp.htm)
[Get Components in Drawing View (VB.NET)](Get_Components_in_Drawing_View_Example_VBNET.htm)
[Get Components in Drawing View (VBA)](Get_Components_in_Drawing_View_Example_VB.htm)

## See Also

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.html)
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.html)
[IDrawingComponent::GetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetLineStyle.html)
[IDrawingComponent::GetLineThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetLineThickness.html)
[IDrawingComponent::SetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~SetLineStyle.html)
[IDrawingComponent::SetLineThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~SetLineThickness.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
