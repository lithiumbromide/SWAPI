---
title: "GetSketchPictures Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetSketchPictures"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSketchPictures.html"
---

# GetSketchPictures Method (IView)

Gets all of the sketch pictures imported to this view when a drawing is created from a part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchPictures() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetSketchPictures()
```

### C#

```csharp
System.object GetSketchPictures()
```

### C++/CLI

```cpp
System.Object^ GetSketchPictures();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [ISketchPictures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPicture.html)

## VBA Syntax

See [View::GetSketchPictures](ms-its:sldworksapivb6.chm::/sldworks~View~GetSketchPictures.html).

## Remarks

Only sketch pictures orthogonal to this view are returned.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetSketchPictures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSketchPictures.html)
[IView::GetSketchPictureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSketchPictureCount.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
