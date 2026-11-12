---
title: "GetSketchPictureCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetSketchPictureCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSketchPictureCount.html"
---

# GetSketchPictureCount Method (IView)

Gets the number of sketch pictures imported to this view when a drawing is created from a part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchPictureCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetSketchPictureCount()
```

### C#

```csharp
System.int GetSketchPictureCount()
```

### C++/CLI

```cpp
System.int GetSketchPictureCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of sketch pictures in the view

## VBA Syntax

See [View::GetSketchPictureCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetSketchPictureCount.html).

## Remarks

Only sketch pictures orthogonal to this view are counted.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetSketchPictures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSketchPictures.html)
[IView::IGetSketchPictures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSketchPictures.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
