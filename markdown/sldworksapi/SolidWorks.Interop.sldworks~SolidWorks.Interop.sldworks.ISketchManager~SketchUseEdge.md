---
title: "SketchUseEdge Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "SketchUseEdge"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchUseEdge.html"
---

# SketchUseEdge Method (ISketchManager)

Obsolete. Superseded by [ISketchManager::SketchUseEdge2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchUseEdge2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SketchUseEdge( _
   ByVal Chain As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim Chain As System.Boolean
Dim value As System.Boolean

value = instance.SketchUseEdge(Chain)
```

### C#

```csharp
System.bool SketchUseEdge(
   System.bool Chain
)
```

### C++/CLI

```cpp
System.bool SketchUseEdge(
   System.bool Chain
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Chain`: True if to convert the entire chain of entities, false to convert only the selected sketch entities (see **Remarks**)

### Return Value

True if the sketch entities are created, false if not

## VBA Syntax

See [SketchManager::SketchUseEdge](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~SketchUseEdge.html).

## Examples

[Insert Sheet Metal Edge Flange (VBA)](Insert_Sheet_Metal_Edge_Flange_Example_VB.htm)
[Offset Selected Edges in Active Sketch (VBA)](Offset_Selected_Edges_in_Active_Sketch_Example_VB.htm)

## Remarks

Specifying true for the Chain argument converts the selected entity and any other entities that belong to the same contour or chain (contiguous, geometric entities like edges) on a sketch plane.

To display all sketch relations symbols, set [IModelDoc2::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetUserPreferenceToggle.html) swViewSketchRelations to true, which can adversely affect performance. To hide all sketch relation symbols, set IModelDoc2::SetUserPreferenceToggle swViewSketchRelations to false, which can improve performance and was the default setting prior to SOLIDWORKS 2005.

See [IModelDoc2::SketchOffsetEntities2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SketchOffsetEntities2.html) method for similar functionality.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
