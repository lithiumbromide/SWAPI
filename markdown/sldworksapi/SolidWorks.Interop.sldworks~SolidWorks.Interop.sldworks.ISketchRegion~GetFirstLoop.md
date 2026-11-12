---
title: "GetFirstLoop Method (ISketchRegion)"
project: "SOLIDWORKS API Help"
interface: "ISketchRegion"
member: "GetFirstLoop"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion~GetFirstLoop.html"
---

# GetFirstLoop Method (ISketchRegion)

Gets the first loop in this sketch region.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstLoop() As Loop2
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRegion
Dim value As Loop2

value = instance.GetFirstLoop()
```

### C#

```csharp
Loop2 GetFirstLoop()
```

### C++/CLI

```cpp
Loop2^ GetFirstLoop();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [loop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html)

## VBA Syntax

See [SketchRegion::GetFirstLoop](ms-its:sldworksapivb6.chm::/sldworks~SketchRegion~GetFirstLoop.html).

## Examples

[Get Sketch Regions (VBA)](Get_Sketch_Regions_Example_VB.htm)
[Get Sketch Regions (VB.NET)](Get_Sketch_Regions_Example_VBNET.htm)
[Get Sketch Regions (C#)](Get_Sketch_Regions_Example_CSharp.htm)

## See Also

[ISketchRegion Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion.html)
[ISketchRegion Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion_members.html)

## Availability

SOLIDWORKS 2009 FCS, Release Number 17.0
