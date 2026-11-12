---
title: "Insert3DSketch Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "Insert3DSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Insert3DSketch.html"
---

# Insert3DSketch Method (ISketchManager)

Inserts a new 3D sketch in a model or closes the active sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Insert3DSketch( _
   ByVal UpdateEditRebuild As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim UpdateEditRebuild As System.Boolean

instance.Insert3DSketch(UpdateEditRebuild)
```

### C#

```csharp
void Insert3DSketch(
   System.bool UpdateEditRebuild
)
```

### C++/CLI

```cpp
void Insert3DSketch(
   System.bool UpdateEditRebuild
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UpdateEditRebuild`: True if you want to edit and rebuild, false if not

## VBA Syntax

See [SketchManager::Insert3DSketch](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~Insert3DSketch.html).

## Examples

[Insert Explode Line Sketch and Jog Line (VB.NET)](Insert_Explode_Line_Sketch_and_Jog_Line_Example_VBNET.htm)
[Insert Explode Line Sketch and Jog Line (VBA)](Insert_Explode_Line_Sketch_and_Jog_Line_Example_VB.htm)
[Insert Explode Line Sketch and Jog Line (C#)](Insert_Explode_Line_Sketch_and_Jog_Line_Example_CSharp.htm)

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::AddToDB Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddToDB.html)
[ISketchManager::CreateSketchPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSketchPlane.html)
[ISketchManager::DisplayWhenAdded Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~DisplayWhenAdded.html)
[ISketchManager::InsertExplodeLineSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertExplodeLineSketch.html)
[ISketchSegment::JogLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~JogLine.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
