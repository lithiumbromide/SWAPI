---
title: "BlockToSketchTransform Property (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "BlockToSketchTransform"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~BlockToSketchTransform.html"
---

# BlockToSketchTransform Property (ISketchBlockInstance)

Gets the MathTransform required to transform coordinates from the sketch block space to the host sketch space.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BlockToSketchTransform As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim value As MathTransform

value = instance.BlockToSketchTransform
```

### C#

```csharp
MathTransform BlockToSketchTransform {get;}
```

### C++/CLI

```cpp
property MathTransform^ BlockToSketchTransform {
   MathTransform^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Math transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [SketchBlockInstance::BlockToSketchTransform](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~BlockToSketchTransform.html).

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)
[ISketchBlockInstance::GetSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetSketch.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
