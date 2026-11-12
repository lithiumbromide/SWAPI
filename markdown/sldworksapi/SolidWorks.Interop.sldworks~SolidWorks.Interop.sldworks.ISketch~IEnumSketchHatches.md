---
title: "IEnumSketchHatches Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "IEnumSketchHatches"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchHatches.html"
---

# IEnumSketchHatches Method (ISketch)

Gets the sketch hatches enumeration in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function IEnumSketchHatches() As EnumSketchHatches
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As EnumSketchHatches

value = instance.IEnumSketchHatches()
```

### C#

```csharp
EnumSketchHatches IEnumSketchHatches()
```

### C++/CLI

```cpp
EnumSketchHatches^ IEnumSketchHatches();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Sketch hatches enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumSketchHatches.html)

## VBA Syntax

See [Sketch::IEnumSketchHatches](ms-its:sldworksapivb6.chm::/sldworks~Sketch~IEnumSketchHatches.html).

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketchHatch::GetSketchHatches Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchHatches.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
