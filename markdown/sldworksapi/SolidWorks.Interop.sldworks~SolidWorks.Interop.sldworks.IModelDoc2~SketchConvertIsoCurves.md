---
title: "SketchConvertIsoCurves Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchConvertIsoCurves"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConvertIsoCurves.html"
---

# SketchConvertIsoCurves Method (IModelDoc2)

Converts ISO-parametric curves on a selected surface into a sketch entity.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchConvertIsoCurves( _
   ByVal PercentRatio As System.Double, _
   ByVal VORuDir As System.Boolean, _
   ByVal DoConstrain As System.Boolean, _
   ByVal SkipHoles As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim PercentRatio As System.Double
Dim VORuDir As System.Boolean
Dim DoConstrain As System.Boolean
Dim SkipHoles As System.Boolean

instance.SketchConvertIsoCurves(PercentRatio, VORuDir, DoConstrain, SkipHoles)
```

### C#

```csharp
void SketchConvertIsoCurves(
   System.double PercentRatio,
   System.bool VORuDir,
   System.bool DoConstrain,
   System.bool SkipHoles
)
```

### C++/CLI

```cpp
void SketchConvertIsoCurves(
   System.double PercentRatio,
   System.bool VORuDir,
   System.bool DoConstrain,
   System.bool SkipHoles
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PercentRatio`: Value for percent ratio
- `VORuDir`: True for V direction, false for UDirection
- `DoConstrain`: True if you want to constrain these new sketch entities, false if not
- `SkipHoles`: True if you want to skip the holes in this surface, false if not

## VBA Syntax

See [ModelDoc2::SketchConvertIsoCurves](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchConvertIsoCurves.html).

## Examples

[Divide Surface into 3D Sketches (VBA)](Divide_Surface_into_3D_Sketches_Example_VB.htm)
[Convert Curves into 3D Sketches (C#)](Convert_Curves_into_3D_Sketches_Example_CSharp.htm)
[Convert Curves into 3D Sketches (VB.NET)](Convert_Curves_into_3D_Sketches_Example_VBNET.htm)
[Convert Curves into 3D Sketches (VBA)](Convert_Curves_into_3D_Sketches_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
