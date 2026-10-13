---
title: "SketchModifyFlip Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchModifyFlip"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchModifyFlip.html"
---

# SketchModifyFlip Method (IModelDoc2)

Flips the the active or selected sketch about the specified coordinate system axis.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchModifyFlip( _
   ByVal AxisFlag As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim AxisFlag As System.Integer

instance.SketchModifyFlip(AxisFlag)
```

### C#

```csharp
void SketchModifyFlip(
   System.int AxisFlag
)
```

### C++/CLI

```cpp
void SketchModifyFlip(
   System.int AxisFlag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AxisFlag`: Axis about which to flip the sketch:

  - X = 1
  - Y = 2

## VBA Syntax

See [ModelDoc2::SketchModifyFlip](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchModifyFlip.html).

## Examples

[Flip Sketch (VBA)](Flip_Sketch_Example_VB.htm)
[Flip Sketch (VB.NET)](Flip_Sketch_Example_VBNET.htm)
[Flip Sketch (C#)](Flip_Sketch_Example_CSharp.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
