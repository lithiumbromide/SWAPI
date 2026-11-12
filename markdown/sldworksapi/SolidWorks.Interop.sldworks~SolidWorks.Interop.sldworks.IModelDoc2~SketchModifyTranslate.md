---
title: "SketchModifyTranslate Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchModifyTranslate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchModifyTranslate.html"
---

# SketchModifyTranslate Method (IModelDoc2)

Translates the coordinate system of the active or selected sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchModifyTranslate( _
   ByVal StartX As System.Double, _
   ByVal StartY As System.Double, _
   ByVal EndX As System.Double, _
   ByVal EndY As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim StartX As System.Double
Dim StartY As System.Double
Dim EndX As System.Double
Dim EndY As System.Double

instance.SketchModifyTranslate(StartX, StartY, EndX, EndY)
```

### C#

```csharp
void SketchModifyTranslate(
   System.double StartX,
   System.double StartY,
   System.double EndX,
   System.double EndY
)
```

### C++/CLI

```cpp
void SketchModifyTranslate(
   System.double StartX,
   System.double StartY,
   System.double EndX,
   System.double EndY
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StartX`: X sketch value defining the from-position
- `StartY`: Y sketch value defining the from-position
- `EndX`: X sketch value defining the to-position
- `EndY`: Y sketch value defining the to-position

### Return Value

The sketch is translated from the XY start point position to the XY end point position.

## VBA Syntax

See [ModelDoc2::SketchModifyTranslate](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchModifyTranslate.html).

## Examples

[Translate Sketch (VBA)](Translate_Sketch_Example_VB.htm)
[Translate Sketch (VB.NET)](Translate_Sketch_Example_VBNET.htm)
[Translate Sketch (C#)](Translate_Sketch_Example_CSharp.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ToolsSketchTranslate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ToolsSketchTranslate.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
