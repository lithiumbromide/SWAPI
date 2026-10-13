---
title: "RelationManager Property (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "RelationManager"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~RelationManager.html"
---

# RelationManager Property (ISketch)

Gets the sketch relation manager.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property RelationManager As SketchRelationManager
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As SketchRelationManager

value = instance.RelationManager
```

### C#

```csharp
SketchRelationManager RelationManager {get;}
```

### C++/CLI

```cpp
property SketchRelationManager^ RelationManager {
   SketchRelationManager^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Sketch relation manager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.html)

## VBA Syntax

See [Sketch::RelationManager](ms-its:sldworksapivb6.chm::/sldworks~Sketch~RelationManager.html).

## Examples

[Get Sketch Relations (VBA)](Get_Sketch_Relations_Example_VB.htm)
[Get Sketch Relations (VB.NET)](Get_Sketch_Relations_Example_VBNET.htm)
[Get Sketch Relations (C#)](Get_Sketch_Relations_Example_CSharp.htm)

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
