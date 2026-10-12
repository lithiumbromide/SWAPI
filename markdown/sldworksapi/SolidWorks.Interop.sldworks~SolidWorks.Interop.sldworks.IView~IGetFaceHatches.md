---
title: "IGetFaceHatches Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetFaceHatches"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFaceHatches.html"
---

# IGetFaceHatches Method (IView)

Gets the face hatches in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFaceHatches( _
   ByVal NumFacesHatches As System.Integer _
) As FaceHatch
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim NumFacesHatches As System.Integer
Dim value As FaceHatch

value = instance.IGetFaceHatches(NumFacesHatches)
```

### C#

```csharp
FaceHatch IGetFaceHatches(
   System.int NumFacesHatches
)
```

### C++/CLI

```cpp
FaceHatch^ IGetFaceHatches(
   System.int NumFacesHatches
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumFacesHatches`: Number of face hatches in the view

### Return Value

- in-process, unmanaged C++: Pointer to an array of [face hatches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFaceHatch.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

## Remarks

Call [IView::GetFaceHatchCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFaceHatchCount.html) before calling this method to get the value for NumFacesHatches.

To get the number of solid-fill hatches in a detail, broken, or crop view, use [IView::GetSolidHatchCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSolidHatchCount.html). To get solid hatches in detail, broken, or crop views, use [IView::GetSolidHatchInfo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSolidHatchInfo.html) or [IView::IGetSolidHatchInfo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetSolidHatchInfo.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetFaceHatches Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatches.html)
[IView::ScaleHatchPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleHatchPattern.html)
[IModelDoc2::InsertHatchedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertHatchedFace.html)
[IView::ScaleHatchPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleHatchPattern.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
