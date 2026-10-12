---
title: "IEnumSketchTextSegments Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "IEnumSketchTextSegments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchTextSegments.html"
---

# IEnumSketchTextSegments Method (ISketch)

Gets the sketch segments enumeration for the selected text in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function IEnumSketchTextSegments() As EnumSketchSegments
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As EnumSketchSegments

value = instance.IEnumSketchTextSegments()
```

### C#

```csharp
EnumSketchSegments IEnumSketchTextSegments()
```

### C++/CLI

```cpp
EnumSketchSegments^ IEnumSketchTextSegments();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Sketch segments enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumSketchSegments.html)

## VBA Syntax

See [Sketch::IEnumSketchTextSegments](ms-its:sldworksapivb6.chm::/sldworks~Sketch~IEnumSketchTextSegments.html).

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSketchTextSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchTextSegments.html)
[ISketch::GetSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSegments.html)
[ISketch::IEnumSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchSegments.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
