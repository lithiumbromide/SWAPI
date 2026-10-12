---
title: "AutoSolve Property (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "AutoSolve"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AutoSolve.html"
---

# AutoSolve Property (ISketchManager)

Gets or sets whether SOLIDWORKS automatically solves the sketch geometry of the part while creating it.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoSolve As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim value As System.Boolean

instance.AutoSolve = value

value = instance.AutoSolve
```

### C#

```csharp
System.bool AutoSolve {get; set;}
```

### C++/CLI

```cpp
property System.bool AutoSolve {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if automatic solve is on, false if off

## VBA Syntax

See [SketchManager::AutoSolve](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~AutoSolve.html).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketch::GetAutomaticSolve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetAutomaticSolve.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
