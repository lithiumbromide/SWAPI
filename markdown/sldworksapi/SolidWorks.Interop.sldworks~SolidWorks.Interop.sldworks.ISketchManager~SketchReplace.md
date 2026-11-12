---
title: "SketchReplace Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "SketchReplace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchReplace.html"
---

# SketchReplace Method (ISketchManager)

Obsolete. Superseded by [ISketchManager::SketchReplace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchReplace2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SketchReplace( _
   ByVal MakeConstruction As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim MakeConstruction As System.Boolean
Dim value As System.Boolean

value = instance.SketchReplace(MakeConstruction)
```

### C#

```csharp
System.bool SketchReplace(
   System.bool MakeConstruction
)
```

### C++/CLI

```cpp
System.bool SketchReplace(
   System.bool MakeConstruction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MakeConstruction`: True to convert the replaced sketch entity to construction geometry, false to not

### Return Value

True if the the sketch entity is successfully replaced, false if not

## VBA Syntax

See [SketchManager::SketchReplace](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~SketchReplace.html).

## Remarks

Before calling this method, call [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with Append set to true to select each of the following entities:

1. Sketch entity to be replaced.
2. Replacement sketch entity that does not reference downstream geometry or have references outside of the sketch.

After calling this method, call [ISketchManager::InsertSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~InsertSketch.html) to rebuild the model with the replacement sketch.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
