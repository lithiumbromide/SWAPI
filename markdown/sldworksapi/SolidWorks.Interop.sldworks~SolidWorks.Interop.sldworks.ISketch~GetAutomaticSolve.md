---
title: "GetAutomaticSolve Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetAutomaticSolve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetAutomaticSolve.html"
---

# GetAutomaticSolve Method (ISketch)

Checks whether the computation to solve the sketch geometry of the part as modifications are automatically performed.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAutomaticSolve() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Boolean

value = instance.GetAutomaticSolve()
```

### C#

```csharp
System.bool GetAutomaticSolve()
```

### C++/CLI

```cpp
System.bool GetAutomaticSolve();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if automatic solving is on, false if off

## VBA Syntax

See [Sketch::GetAutomaticSolve](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetAutomaticSolve.html).

## Remarks

This method can be controlled with [ISketch::SetAutomaticSolve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~SetAutomaticSolve.html).

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketchManager::AutoSolve Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AutoSolve.html)
