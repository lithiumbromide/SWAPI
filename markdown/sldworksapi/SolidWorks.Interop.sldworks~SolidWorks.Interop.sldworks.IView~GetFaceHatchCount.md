---
title: "GetFaceHatchCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFaceHatchCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatchCount.html"
---

# GetFaceHatchCount Method (IView)

Gets the number of face hatches in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFaceHatchCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetFaceHatchCount()
```

### C#

```csharp
System.int GetFaceHatchCount()
```

### C++/CLI

```cpp
System.int GetFaceHatchCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of faces hatches in the view

## VBA Syntax

See [View::GetFaceHatchCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetFaceHatchCount.html).

## Examples

[Get Crosshatches on the View (VBA)](Get_Crosshatches_on_View_Example_VB.htm)

## Remarks

Call this method before calling [IView::IGetFaceHatches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetFaceHatches.html) to get the size of the array for that method.

To get the number of solid hatches in a detail, broken, or crop view, use [IView::GetSolidHatchCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSolidHatchCount.html). To get solid hatches in detail, broken, or crop views, use [IView::GetSolidHatchInfo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSolidHatchInfo.html) or [IView::IGetSolidHatchInfo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetSolidHatchInfo.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetFaceHatches Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatches.html)
[IView::IGetFaceHatches Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFaceHatches.html)
[IView::ScaleHatchPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleHatchPattern.html)
[IModelDoc2::InsertHatchedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertHatchedFace.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
