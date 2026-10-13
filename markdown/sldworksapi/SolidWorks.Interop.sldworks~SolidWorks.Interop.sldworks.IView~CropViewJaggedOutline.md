---
title: "CropViewJaggedOutline Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "CropViewJaggedOutline"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewJaggedOutline.html"
---

# CropViewJaggedOutline Property (IView)

Gets or sets whether to use a jagged outline in this cropped drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Property CropViewJaggedOutline As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

instance.CropViewJaggedOutline = value

value = instance.CropViewJaggedOutline
```

### C#

```csharp
System.bool CropViewJaggedOutline {get; set;}
```

### C++/CLI

```cpp
property System.bool CropViewJaggedOutline {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use a jagged outline, false to not (see **Remarks**)

## VBA Syntax

See [View::CropViewJaggedOutline](ms-its:sldworksapivb6.chm::/sldworks~View~CropViewJaggedOutline.html).

## Examples

[Crop Drawing View Using Jagged Outline (C#)](Crop_Drawing_View_Using_Jagged_Outline_Example_CSharp.htm)
[Crop Drawing View Using Jagged Outline (VB.NET)](Crop_Drawing_View_Using_Jagged_Outline_Example_VBNET.htm)
[Crop Drawing View Using Jagged Outline (VBA)](Crop_Drawing_View_Using_Jagged_Outline_Example_VB.htm)

## Remarks

Call [IView::IsCropped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsCropped.html) to find out if this drawing view is cropped.

IView::CropViewJaggedOutline is only available when [IView::CropViewNoOutline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewNoOutline.html) is false.

To set the intensity of the jagged outline, call [IView::CropViewJaggedShapeIntensity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewJaggedShapeIntensity.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::Crop2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Crop2.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
