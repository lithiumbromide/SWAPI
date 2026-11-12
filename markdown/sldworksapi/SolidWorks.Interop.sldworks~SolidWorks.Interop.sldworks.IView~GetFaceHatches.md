---
title: "GetFaceHatches Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFaceHatches"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatches.html"
---

# GetFaceHatches Method (IView)

Gets the face hatches in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFaceHatches() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetFaceHatches()
```

### C#

```csharp
System.object GetFaceHatches()
```

### C++/CLI

```cpp
System.Object^ GetFaceHatches();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Face hatches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFaceHatch.html) in the view

## VBA Syntax

See [View::GetFaceHatches](ms-its:sldworksapivb6.chm::/sldworks~View~GetFaceHatches.html).

## Examples

[Get Face Hatch Data (C#)](Get_Face_Hatch_Data_Example_CSharp.htm)
[Get Face Hatch Data (VB.NET)](Get_Face_Hatch_Data_Example_VBNET.htm)
[Get Face Hatch Data (VBA)](Get_Face_Hatch_Data_Example_VB.htm)

## Remarks

To get the number of solid hatches in a detail, broken, or crop view, use [IView::GetSolidHatchCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSolidHatchCount.html). To get solid hatches in detail, broken, or crop views, use [IView::GetSolidHatchInfo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSolidHatchInfo.html) or [IView::IGetSolidHatchInfo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetSolidHatchInfo.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetFaceHatchCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatchCount.html)
[IView::IGetFaceHatches Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFaceHatches.html)
[IView::ScaleHatchPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleHatchPattern.html)
[IModelDoc2::InsertHatchedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertHatchedFace.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
