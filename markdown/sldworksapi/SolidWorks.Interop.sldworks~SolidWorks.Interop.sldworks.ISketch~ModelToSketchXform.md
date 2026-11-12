---
title: "ModelToSketchXform Property (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "ModelToSketchXform"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~ModelToSketchXform.html"
---

# ModelToSketchXform Property (ISketch)

Obsolete. Superseded by [ISketch::ModelToSketchTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~ModelToSketchTransform.html).

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property ModelToSketchXform As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Object

instance.ModelToSketchXform = value

value = instance.ModelToSketchXform
```

### C#

```csharp
System.object ModelToSketchXform {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ModelToSketchXform {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Sketch::ModelToSketchXform](ms-its:sldworksapivb6.chm::/sldworks~Sketch~ModelToSketchXform.html).

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
