---
title: "SketchModifyScale Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchModifyScale"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchModifyScale.html"
---

# SketchModifyScale Method (IModelDoc2)

Scales the active or selected sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function SketchModifyScale( _
   ByVal ScaleFactor As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ScaleFactor As System.Double
Dim value As System.Boolean

value = instance.SketchModifyScale(ScaleFactor)
```

### C#

```csharp
System.bool SketchModifyScale(
   System.double ScaleFactor
)
```

### C++/CLI

```cpp
System.bool SketchModifyScale(
   System.double ScaleFactor
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ScaleFactor`: Amount by which to scale sketch

### Return Value

True if successful, false if not

## VBA Syntax

See [ModelDoc2::SketchModifyScale](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchModifyScale.html).

## Examples

[Rotate, Scale, and Copy Sketch (C#)](Rotate_Scale_Copy_Sketch_Example_CSharp.htm)
[Rotate, Scale, and Copy Sketch (VB.NET)](Rotate_Scale_Copy_Sketch_Example_VBNET.htm)
[Rotate, Scale, and Copy Sketch (VBA)](Rotate_Scale_Copy_Sketch_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ToolsSketchScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ToolsSketchScale.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
