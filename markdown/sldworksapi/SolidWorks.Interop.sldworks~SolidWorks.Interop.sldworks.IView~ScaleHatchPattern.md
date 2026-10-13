---
title: "ScaleHatchPattern Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "ScaleHatchPattern"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleHatchPattern.html"
---

# ScaleHatchPattern Property (IView)

Gets or sets whether to scale the hatch pattern to the drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Property ScaleHatchPattern As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

instance.ScaleHatchPattern = value

value = instance.ScaleHatchPattern
```

### C#

```csharp
System.bool ScaleHatchPattern {get; set;}
```

### C++/CLI

```cpp
property System.bool ScaleHatchPattern {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to scale the hatch pattern to the drawing view, false to not

## VBA Syntax

See [View::ScaleHatchPattern](ms-its:sldworksapivb6.chm::/sldworks~View~ScaleHatchPattern.html).

## Examples

[Get Area Hatch Data (C#)](Get_Area_Hatch_Data_Example_CSharp.htm)
[Get Area Hatch Data (VB.NET)](Get_Area_Hatch_Data_Example_VBNET.htm)
[Get Area Hatch Data (VBA)](Get_Area_Hatch_Data_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetFaceHatchCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatchCount.html)
[IView::GetFaceHatches Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatches.html)
[IModelDoc2::InsertHatchedFace Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertHatchedFace.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
