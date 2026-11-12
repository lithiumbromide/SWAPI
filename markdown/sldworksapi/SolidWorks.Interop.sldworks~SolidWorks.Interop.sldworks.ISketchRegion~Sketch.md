---
title: "Sketch Property (ISketchRegion)"
project: "SOLIDWORKS API Help"
interface: "ISketchRegion"
member: "Sketch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion~Sketch.html"
---

# Sketch Property (ISketchRegion)

Gets the sketch for this sketch region.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Sketch As Sketch
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRegion
Dim value As Sketch

value = instance.Sketch
```

### C#

```csharp
Sketch Sketch {get;}
```

### C++/CLI

```cpp
property Sketch^ Sketch {
   Sketch^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

## VBA Syntax

See [SketchRegion::Sketch](ms-its:sldworksapivb6.chm::/sldworks~SketchRegion~Sketch.html).

## See Also

[ISketchRegion Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion.html)
[ISketchRegion Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
