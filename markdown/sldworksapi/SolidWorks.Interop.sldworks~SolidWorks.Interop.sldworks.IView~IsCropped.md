---
title: "IsCropped Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IsCropped"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsCropped.html"
---

# IsCropped Method (IView)

Get whether this drawing view is cropped.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsCropped() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

value = instance.IsCropped()
```

### C#

```csharp
System.bool IsCropped()
```

### C++/CLI

```cpp
System.bool IsCropped();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the drawing view is cropped, false if not

## VBA Syntax

See [View::IsCropped](ms-its:sldworksapivb6.chm::/sldworks~View~IsCropped.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::Crop2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Crop2.html)
[IView::CropViewJaggedOutline Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewJaggedOutline.html)
[IView::CropViewJaggedShapeIntensity Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewJaggedShapeIntensity.html)
[IView::CropViewNoOutline Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewNoOutline.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
