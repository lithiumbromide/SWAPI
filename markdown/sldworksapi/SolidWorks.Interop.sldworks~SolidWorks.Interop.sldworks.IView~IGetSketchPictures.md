---
title: "IGetSketchPictures Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetSketchPictures"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSketchPictures.html"
---

# IGetSketchPictures Method (IView)

Gets all of the sketch pictures imported to this view when a drawing is created from a part.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSketchPictures( _
   ByVal Count As System.Integer _
) As SketchPicture
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Count As System.Integer
Dim value As SketchPicture

value = instance.IGetSketchPictures(Count)
```

### C#

```csharp
SketchPicture IGetSketchPictures(
   System.int Count
)
```

### C++/CLI

```cpp
SketchPicture^ IGetSketchPictures(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of sketch pictures in this view

### Return Value

- in-process, unmanaged C++: Pointer to an array of [ISketchPicture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPicture.html)s
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

## Remarks

Use [IView::GetSketchPictureCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSketchPictureCount.html) to populate the Count parameter before calling this method. Only sketch pictures orthogonal to this view are returned.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetSketchPictures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSketchPictures.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
