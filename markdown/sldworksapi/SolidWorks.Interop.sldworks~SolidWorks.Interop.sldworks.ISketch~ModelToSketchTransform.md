---
title: "ModelToSketchTransform Property (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "ModelToSketchTransform"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~ModelToSketchTransform.html"
---

# ModelToSketchTransform Property (ISketch)

Gets the model-to-sketch transform for this sketch.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property ModelToSketchTransform As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As MathTransform

instance.ModelToSketchTransform = value

value = instance.ModelToSketchTransform
```

### C#

```csharp
MathTransform ModelToSketchTransform {get; set;}
```

### C++/CLI

```cpp
property MathTransform^ ModelToSketchTransform {
   MathTransform^ get();
   void set (    MathTransform^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Math transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [Sketch::ModelToSketchTransform](ms-its:sldworksapivb6.chm::/sldworks~Sketch~ModelToSketchTransform.html).

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[IModelDoc2::SketchSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchSplineByEqnParams.html)
[IModelDoc2::SketchSplineByEqnParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchSplineByEqnParams2.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
