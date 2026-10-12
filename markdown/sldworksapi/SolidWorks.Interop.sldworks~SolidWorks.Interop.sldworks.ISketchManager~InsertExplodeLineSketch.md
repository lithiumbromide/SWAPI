---
title: "InsertExplodeLineSketch Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "InsertExplodeLineSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertExplodeLineSketch.html"
---

# InsertExplodeLineSketch Method (ISketchManager)

Inserts or closes an explode line sketch in an exploded view.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertExplodeLineSketch() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim value As System.Boolean

value = instance.InsertExplodeLineSketch()
```

### C#

```csharp
System.bool InsertExplodeLineSketch()
```

### C++/CLI

```cpp
System.bool InsertExplodeLineSketch();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the explode line sketch is inserted or closed, false if not

## VBA Syntax

See [SketchManager::InsertExplodeLineSketch](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~InsertExplodeLineSketch.html).

## Examples

[Insert Explode Line Sketch and Route Line (VB.NET)](Insert_Exploded_Line_Sketch_and_Route_Line_Example_VBNET.htm)
[Insert Explode Line Sketch and Route Line (VBA)](Insert_Exploded_Line_Sketch_and_Route_Line_Example_VB.htm)
[Insert Explode Line Sketch and Jog Line (VB.NET)](Insert_Explode_Line_Sketch_and_Jog_Line_Example_VBNET.htm)
[Insert Explode Line Sketch and Jog Line (VBA)](Insert_Explode_Line_Sketch_and_Jog_Line_Example_VB.htm)
[Insert Explode Line Sketch and Jog Line (C#)](Insert_Explode_Line_Sketch_and_Jog_Line_Example_CSharp.htm)
[Insert Explode Line Sketch and Route Line (C#)](Insert_Exploded_Line_Sketch_and_Route_Line_Example_CSharp.htm)

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[IAssemblyDoc::AutoExplode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoExplode.html)
[ISketch::InsertRouteLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~InsertRouteLine.html)
[ISketchManager::Insert3DSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Insert3DSketch.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
