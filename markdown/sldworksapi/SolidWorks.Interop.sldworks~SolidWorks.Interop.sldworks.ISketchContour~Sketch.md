---
title: "Sketch Property (ISketchContour)"
project: "SOLIDWORKS API Help"
interface: "ISketchContour"
member: "Sketch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~Sketch.html"
---

# Sketch Property (ISketchContour)

Gets the sketch for this sketch contour.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Sketch As Sketch
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchContour
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

See [SketchContour::Sketch](ms-its:sldworksapivb6.chm::/sldworks~SketchContour~Sketch.html).

## See Also

[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.html)
[ISketchContour Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
