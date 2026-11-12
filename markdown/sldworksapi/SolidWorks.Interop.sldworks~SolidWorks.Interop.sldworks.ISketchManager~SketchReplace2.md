---
title: "SketchReplace2 Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "SketchReplace2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchReplace2.html"
---

# SketchReplace2 Method (ISketchManager)

Replaces a sketch entity in a model with another sketch entity, preserving all references.

## Syntax

### Visual Basic (Declaration)

```vb
Function SketchReplace2( _
   ByVal MakeConstruction As System.Boolean, _
   ByVal MakeContour As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim MakeConstruction As System.Boolean
Dim MakeContour As System.Boolean
Dim value As System.Boolean

value = instance.SketchReplace2(MakeConstruction, MakeContour)
```

### C#

```csharp
System.bool SketchReplace2(
   System.bool MakeConstruction,
   System.bool MakeContour
)
```

### C++/CLI

```cpp
System.bool SketchReplace2(
   System.bool MakeConstruction,
   System.bool MakeContour
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MakeConstruction`: True to convert the replaced sketch entity to construction geometry, false to delete it
- `MakeContour`: True to make the replacement sketch entity a contour, false to not

### Return Value

True if the the sketch entity is successfully replaced, false if not

## VBA Syntax

See [SketchManager::SketchReplace2](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~SketchReplace2.html).

## Examples

[Replace Sketch Entity (VBA)](Replace_Sketch_Example_VB.htm)
[Replace Sketch Entity (VB.NET)](Replace_Sketch_Example_VBNET.htm)
[Replace Sketch Entity (C#)](Replace_Sketch_Example_CSharp.htm)

## Remarks

Before calling this method, call [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with Append set to true to select each of the following entities:

1. Sketch entity to be replaced.
2. Replacement sketch entity that does not reference downstream geometry or have references outside of the sketch.

After calling this method, call [ISketchManager::InsertSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~InsertSketch.html) to rebuild the model with the replacement sketch.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
