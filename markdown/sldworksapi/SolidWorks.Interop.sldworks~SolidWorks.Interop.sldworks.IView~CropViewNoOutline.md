---
title: "CropViewNoOutline Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "CropViewNoOutline"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewNoOutline.html"
---

# CropViewNoOutline Property (IView)

Gets or sets whether to show an outline in this cropped drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Property CropViewNoOutline As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

instance.CropViewNoOutline = value

value = instance.CropViewNoOutline
```

### C#

```csharp
System.bool CropViewNoOutline {get; set;}
```

### C++/CLI

```cpp
property System.bool CropViewNoOutline {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to not show an outline, false to show an outline

## VBA Syntax

See [View::CropViewNoOutline](ms-its:sldworksapivb6.chm::/sldworks~View~CropViewNoOutline.html).

## Examples

[Crop Drawing View Using Jagged Outline (C#)](Crop_Drawing_View_Using_Jagged_Outline_Example_CSharp.htm)
[Crop Drawing View Using Jagged Outline (VB.NET)](Crop_Drawing_View_Using_Jagged_Outline_Example_VBNET.htm)
[Crop Drawing View Using Jagged Outline (VBA)](Crop_Drawing_View_Using_Jagged_Outline_Example_VB.htm)

## Remarks

Call [IView::IsCropped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsCropped.html) to find out if this drawing view is cropped.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::Crop2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Crop2.html)
[IView::CropViewJaggedOutline Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewJaggedOutline.html)
[IView::CropViewJaggedShapeIntensity Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewJaggedShapeIntensity.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
