---
title: "IModelToSketchXform Property (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "IModelToSketchXform"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IModelToSketchXform.html"
---

# IModelToSketchXform Property (ISketch)

Obsolete. Superseded by [ISketch::ModelToSketchTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~ModelToSketchTransform.html).

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IModelToSketchXform As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Double

value = instance.IModelToSketchXform
```

### C#

```csharp
System.double IModelToSketchXform {get;}
```

### C++/CLI

```cpp
property System.double IModelToSketchXform {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Sketch::IModelToSketchXform](ms-its:sldworksapivb6.chm::/sldworks~Sketch~IModelToSketchXform.html).

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
