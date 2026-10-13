---
title: "CropViewJaggedShapeIntensity Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "CropViewJaggedShapeIntensity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewJaggedShapeIntensity.html"
---

# CropViewJaggedShapeIntensity Property (IView)

Gets or sets the shape intensity of the jagged outline in this cropped drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Property CropViewJaggedShapeIntensity As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

instance.CropViewJaggedShapeIntensity = value

value = instance.CropViewJaggedShapeIntensity
```

### C#

```csharp
System.int CropViewJaggedShapeIntensity {get; set;}
```

### C++/CLI

```cpp
property System.int CropViewJaggedShapeIntensity {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Shape intensity of the jagged outline; valid range is 1 (most) to 5 (least) (see **Remarks**)

## VBA Syntax

See [View::CropViewJaggedShapeIntensity](ms-its:sldworksapivb6.chm::/sldworks~View~CropViewJaggedShapeIntensity.html).

## Examples

[Crop Drawing View Using Jagged Outline (C#)](Crop_Drawing_View_Using_Jagged_Outline_Example_CSharp.htm)
[Crop Drawing View Using Jagged Outline (VB.NET)](Crop_Drawing_View_Using_Jagged_Outline_Example_VBNET.htm)
[Crop Drawing View Using Jagged Outline (VBA)](Crop_Drawing_View_Using_Jagged_Outline_Example_VB.htm)

## Remarks

Call [IView::IsCropped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsCropped.html) to find out if this drawing view is cropped.

IView::CropViewJaggedShapeIntensity is only available when [IView::CropViewJaggedOutline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewJaggedOutline.html) is true and [IView::CropViewNoOutline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewNoOutline.html) is false.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::Crop2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Crop2.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
