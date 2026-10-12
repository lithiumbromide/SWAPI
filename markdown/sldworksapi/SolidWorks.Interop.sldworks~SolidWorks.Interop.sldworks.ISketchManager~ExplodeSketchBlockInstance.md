---
title: "ExplodeSketchBlockInstance Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "ExplodeSketchBlockInstance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ExplodeSketchBlockInstance.html"
---

# ExplodeSketchBlockInstance Method (ISketchManager)

Explodes the specified block instance.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ExplodeSketchBlockInstance( _
   ByVal LpSketchBlockInstance As SketchBlockInstance _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim LpSketchBlockInstance As SketchBlockInstance

instance.ExplodeSketchBlockInstance(LpSketchBlockInstance)
```

### C#

```csharp
void ExplodeSketchBlockInstance(
   SketchBlockInstance LpSketchBlockInstance
)
```

### C++/CLI

```cpp
void ExplodeSketchBlockInstance(
   SketchBlockInstance^ LpSketchBlockInstance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LpSketchBlockInstance`: [Block instance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance.html) to explode

## VBA Syntax

See [SketchManager::ExplodeSketchBlockInstance](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~ExplodeSketchBlockInstance.html).

## Remarks

If this is the only or last block instance, then:

- All sketch entities in the block instances are copied to the owning sketch of the block instance.
- Source block definition is destroyed.

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
