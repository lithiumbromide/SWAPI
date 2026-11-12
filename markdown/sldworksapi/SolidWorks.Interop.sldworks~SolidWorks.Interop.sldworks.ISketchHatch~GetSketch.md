---
title: "GetSketch Method (ISketchHatch)"
project: "SOLIDWORKS API Help"
interface: "ISketchHatch"
member: "GetSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~GetSketch.html"
---

# GetSketch Method (ISketchHatch)

Gets the sketch for the current sketch hatch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketch() As Sketch
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchHatch
Dim value As Sketch

value = instance.GetSketch()
```

### C#

```csharp
Sketch GetSketch()
```

### C++/CLI

```cpp
Sketch^ GetSketch();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

## VBA Syntax

See [SketchHatch::GetSketch](ms-its:sldworksapivb6.chm::/sldworks~SketchHatch~GetSketch.html).

## Remarks

You can use the [ISketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html) interface for extracting information about geometry in the sketch.

## See Also

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
