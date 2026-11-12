---
title: "SketchUseEdge2 Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "SketchUseEdge2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchUseEdge2.html"
---

# SketchUseEdge2 Method (ISketchManager)

Obsolete. Superseded by [ISketchManager::SketchUseEdge3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchUseEdge3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SketchUseEdge2( _
   ByVal Chain As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim Chain As System.Boolean
Dim value As System.Boolean

value = instance.SketchUseEdge2(Chain)
```

### C#

```csharp
System.bool SketchUseEdge2(
   System.bool Chain
)
```

### C++/CLI

```cpp
System.bool SketchUseEdge2(
   System.bool Chain
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Chain`: True to convert the entire chain of sketch entities, false to convert only the selected sketch entities (see **Remarks**)

### Return Value

True if the sketch entities are created, false if not

## VBA Syntax

See [SketchManager::SketchUseEdge2](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~SketchUseEdge2.html).

## Examples

[Convert Faces' Edges to Sketch Entities (VB.NET)](Convert_Faces_Edges_to_Sketch_Entities_Example_VBNET.htm)
[Convert Faces' Edges to Sketch Entities (VBA)](Convert_Faces_Edges_to_Sketch_Entities_Example_VB.htm)

## Remarks

Specifying true for the Chain argument creates the selected sketch entity and any other sketch entities that belong to the same contour or chain (contiguous geometric sketch entities like sketch edges) on a sketch plane.

To display all sketch relations symbols, set [IModelDocExtension::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceToggle.html) swViewSketchRelations to true, which can adversely affect performance. To hide all sketch relation symbols, set IModelDocExtension::SetUserPreferenceToggle swViewSketchRelations to false, which can improve performance and was the default setting prior to SOLIDWORKS 2005.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[IModelDoc2::SketchOffsetEntities2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEntities2.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
