---
title: "SketchManager Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchManager"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchManager.html"
---

# SketchManager Property (IModelDoc2)

Gets the sketch manager, which allows access to sketch-creation routines.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SketchManager As SketchManager
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As SketchManager

value = instance.SketchManager
```

### C#

```csharp
SketchManager SketchManager {get;}
```

### C++/CLI

```cpp
property SketchManager^ SketchManager {
   SketchManager^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Sketch manager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)

## VBA Syntax

See [ModelDoc2::SketchManager](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchManager.html).

## Examples

[Dynamically Mirror Sketch Entities (VBA)](Dynamically_Mirror_Sketch_Entities_Example_VB.htm)
[Get Sketch Entities (VBA)](Get_Sketch_Entities_Example_VB.htm)
[Offset Selected Edges in Active Sketch (VBA)](Offset_Selected_Edges_in_Active_Sketch_Example_VB.htm)
[Insert and Resize Sketch Slot (C#)](Insert_and_Resize_Sketch_Slot_Example_CSharp.htm)
[Insert and Resize Sketch Slot (VB.NET)](Insert_and_Resize_Sketch_Slot_Example_VBNET.htm)
[Insert and Resize Sketch Slot (VBA)](Insert_and_Resize_Sketch_Slot_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
