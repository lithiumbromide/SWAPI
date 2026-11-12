---
title: "InsertSketch Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "InsertSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketch.html"
---

# InsertSketch Method (ISketchManager)

Inserts a new sketch in the current part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertSketch( _
   ByVal UpdateEditRebuild As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim UpdateEditRebuild As System.Boolean

instance.InsertSketch(UpdateEditRebuild)
```

### C#

```csharp
void InsertSketch(
   System.bool UpdateEditRebuild
)
```

### C++/CLI

```cpp
void InsertSketch(
   System.bool UpdateEditRebuild
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UpdateEditRebuild`: True to rebuild the part with any changes made to the sketch and exit sketch mode, false to not

## VBA Syntax

See [SketchManager::InsertSketch](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~InsertSketch.html).

## Examples

[Insert Sheet Metal Edge Flange (VBA)](Insert_Sheet_Metal_Edge_Flange_Example_VB.htm)
[Create Equation-driven Curve (C#)](Create_Equation-driven_Curve_Example_CSharp.htm)
[Create Equation-driven Curve (VB.NET)](Create_Equation-driven_Curve_Example_VBNET.htm)
[Create Equation-driven Curve (VBA)](Create_Equation-driven_Curve_Example_VB.htm)
[Insert and Resize Sketch Slot (C#)](Insert_and_Resize_Sketch_Slot_Example_CSharp.htm)
[Insert and Resize Sketch Slot (VB.NET)](Insert_and_Resize_Sketch_Slot_Example_VBNET.htm)
[Insert and Resize Sketch Slot (VBA)](Insert_and_Resize_Sketch_Slot_Example_VB.htm)

## Remarks

This method does not support drawing documents.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
