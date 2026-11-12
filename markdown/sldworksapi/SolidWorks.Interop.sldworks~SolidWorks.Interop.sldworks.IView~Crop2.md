---
title: "Crop2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "Crop2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Crop2.html"
---

# Crop2 Method (IView)

Crops this view using the selected closed sketch profile.

## Syntax

### Visual Basic (Declaration)

```vb
Function Crop2( _
   ByVal JaggedOutline As System.Boolean, _
   ByVal NoOutline As System.Boolean, _
   ByVal ShapeIntensity As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim JaggedOutline As System.Boolean
Dim NoOutline As System.Boolean
Dim ShapeIntensity As System.Integer
Dim value As System.Integer

value = instance.Crop2(JaggedOutline, NoOutline, ShapeIntensity)
```

### C#

```csharp
System.int Crop2(
   System.bool JaggedOutline,
   System.bool NoOutline,
   System.int ShapeIntensity
)
```

### C++/CLI

```cpp
System.int Crop2(
   System.bool JaggedOutline,
   System.bool NoOutline,
   System.int ShapeIntensity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `JaggedOutline`: True to use a jagged outline, false to not; only valid if NoOutline is false
- `NoOutline`: True to not show an outline, false to show an outline
- `ShapeIntensity`: Shape intensity of the jagged outline; valid range is 1 (most) to 5 (least); only valid if JaggedOutline is true

### Return Value

Crop view status as defined in [swCropViewErrors_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCropViewErrors_e.html)

## VBA Syntax

See [View::Crop2](ms-its:sldworksapivb6.chm::/sldworks~View~Crop2.html).

## Examples

[Crop Drawing View Using Jagged Outline (C#)](Crop_Drawing_View_Using_Jagged_Outline_Example_CSharp.htm)
[Crop Drawing View Using Jagged Outline (VB.NET)](Crop_Drawing_View_Using_Jagged_Outline_Example_VBNET.htm)
[Crop Drawing View Using Jagged Outline (VBA)](Crop_Drawing_View_Using_Jagged_Outline_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IsCropped Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsCropped.html)
[IView::CropViewJaggedOutline Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewJaggedOutline.html)
[IView::CropViewJaggedShapeIntensity Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewJaggedShapeIntensity.html)
[IView::CropViewNoOutline Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewNoOutline.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
