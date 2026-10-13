---
title: "MakeSketchChain Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "MakeSketchChain"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchChain.html"
---

# MakeSketchChain Method (ISketchManager)

Creates a sketch path using the selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function MakeSketchChain() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim value As System.Boolean

value = instance.MakeSketchChain()
```

### C#

```csharp
System.bool MakeSketchChain()
```

### C++/CLI

```cpp
System.bool MakeSketchChain();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the a sketch path is created, false if not

## VBA Syntax

See [SketchManager::MakeSketchChain](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~MakeSketchChain.html).

## Examples

[Create Sketch Path (VBA)](Create_Sketch_Path_Example_VB.htm)
[Create Sketch Path (VB.NET)](Create_Sketch_Path_Example_VBNET.htm)
[Create Sketch Path (C#)](Create_Sketch_Path_Example_CSharp.htm)

## Remarks

This method is not valid:

- unless a sketch is in edit mode.
- for 3D sketches.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
