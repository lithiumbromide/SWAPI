---
title: "SketchModifyRotate Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchModifyRotate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchModifyRotate.html"
---

# SketchModifyRotate Method (IModelDoc2)

Rotates the coordinate system of the active or selected sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchModifyRotate( _
   ByVal CenterX As System.Double, _
   ByVal CenterY As System.Double, _
   ByVal Angle As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim CenterX As System.Double
Dim CenterY As System.Double
Dim Angle As System.Double

instance.SketchModifyRotate(CenterX, CenterY, Angle)
```

### C#

```csharp
void SketchModifyRotate(
   System.double CenterX,
   System.double CenterY,
   System.double Angle
)
```

### C++/CLI

```cpp
void SketchModifyRotate(
   System.double CenterX,
   System.double CenterY,
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CenterX`: X point to rotate about
- `CenterY`: Y point to rotate about
- `Angle`: Angle of rotation

## VBA Syntax

See [ModelDoc2::SketchModifyRotate](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchModifyRotate.html).

## Examples

[Rotate, Scale, and Copy Sketch (C#)](Rotate_Scale_Copy_Sketch_Example_CSharp.htm)
[Rotate, Scale, and Copy Sketch (VB.NET)](Rotate_Scale_Copy_Sketch_Example_VBNET.htm)
[Rotate, Scale, and Copy Sketch (VBA)](Rotate_Scale_Copy_Sketch_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
