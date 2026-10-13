---
title: "GetSketchTextSegments Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSketchTextSegments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchTextSegments.html"
---

# GetSketchTextSegments Method (ISketch)

Gets the sketch segments that represent the selected text in the sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchTextSegments() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Object

value = instance.GetSketchTextSegments()
```

### C#

```csharp
System.object GetSketchTextSegments()
```

### C++/CLI

```cpp
System.Object^ GetSketchTextSegments();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) for the selected text in this sketch

## VBA Syntax

See [Sketch::GetSketchTextSegments](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSketchTextSegments.html).

## Examples

[Get Sketch Entities (VBA)](Get_Sketch_Entities_Example_VB.htm)
[Replace Sketch Text (VBA)](Replace_Sketch_Text_Example_VB.htm)

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::IEnumSketchTextSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchTextSegments.html)
[ISketch::GetSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSegments.html)
[ISketch::IEnumSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchSegments.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
