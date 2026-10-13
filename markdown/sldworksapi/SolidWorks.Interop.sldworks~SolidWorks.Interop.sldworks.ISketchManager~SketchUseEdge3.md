---
title: "SketchUseEdge3 Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "SketchUseEdge3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchUseEdge3.html"
---

# SketchUseEdge3 Method (ISketchManager)

Creates sketch entities on a sketch plane by projecting selected edges, loops, faces, curves, and external sketch contours.

## Syntax

### Visual Basic (Declaration)

```vb
Function SketchUseEdge3( _
   ByVal Chain As System.Boolean, _
   ByVal InnerLoops As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim Chain As System.Boolean
Dim InnerLoops As System.Boolean
Dim value As System.Boolean

value = instance.SketchUseEdge3(Chain, InnerLoops)
```

### C#

```csharp
System.bool SketchUseEdge3(
   System.bool Chain,
   System.bool InnerLoops
)
```

### C++/CLI

```cpp
System.bool SketchUseEdge3(
   System.bool Chain,
   System.bool InnerLoops
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Chain`: True to convert an entire chain of sketch entities, false to convert only the selected sketch entities (see **Remarks**)
- `InnerLoops`: True to convert the inner loops of the selected faces to sketch entities, false to not

### Return Value

True if the sketch entities are created, false if not

## VBA Syntax

See [SketchManager::SketchUseEdge3](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~SketchUseEdge3.html).

## Examples

[Convert Edges and Inner Loops of Face to Sketch Entities (C#)](Convert_Edges_and_Inner_Loops_of_Face_to_Sketch_Entities_Example_CSharp.htm)
[Convert Edges and Inner Loops of Face to Sketch Entities (VB.NET)](Convert_Edges_and_Inner_Loops_of_Face_to_Sketch_Entities_Example_VBNET.htm)
[Convert Edges and Inner Loops of Face to Sketch Entities (VBA)](Convert_Edges_and_Inner_Loops_of_Face_to_Sketch_Entities_Example_VB.htm)

## Remarks

Specifying true for the Chain argument creates the selected sketch entity and any other sketch entities that belong to the same sketch contour or chain (contiguous geometric entities like sketch edges) on the sketch plane.

To display all sketch relations symbols, set [IModelDocExtension::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceToggle.html) swViewSketchRelations to true, which can adversely affect performance. To hide all sketch relation symbols, set IModelDocExtension::SetUserPreferenceToggle swViewSketchRelations to false, which can improve performance and was the default setting prior to SOLIDWORKS 2005.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[IModelDoc2::SketchOffsetEntities2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEntities2.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
