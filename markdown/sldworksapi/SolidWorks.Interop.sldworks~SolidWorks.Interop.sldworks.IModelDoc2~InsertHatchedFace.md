---
title: "InsertHatchedFace Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertHatchedFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertHatchedFace.html"
---

# InsertHatchedFace Method (IModelDoc2)

Hatches the selected faces or closed sketch segments in a drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertHatchedFace()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.InsertHatchedFace()
```

### C#

```csharp
void InsertHatchedFace()
```

### C++/CLI

```cpp
void InsertHatchedFace();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::InsertHatchedFace](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertHatchedFace.html).

## Examples

[Insert Hatch (VBA)](Insert_Hatch_Example_VB.htm)
[Get Area Hatch Data (VBA)](Get_Area_Hatch_Data_Example_VB.htm)
[Get Area Hatch Data (VB.NET)](Get_Area_Hatch_Data_Example_VBNET.htm)
[Get Area Hatch Data (C#)](Get_Area_Hatch_Data_Example_CSharp.htm)

## Remarks

This method supports hatching of drawings only; it does not support hatching of parts or assemblies.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IView::GetFaceHatchCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatchCount.html)
[IView::GetFaceHatches Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatches.html)
[IView::IGetFaceHatches Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFaceHatches.html)
[IView::ScaleHatchPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleHatchPattern.html)
[IFaceHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.html)
[ISketchManager::CreateRegionHatch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateRegionHatch.html)
[ISketchManager::CreateBoundaryHatch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateBoundaryHatch.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
