---
title: "GetSketchRegions Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSketchRegions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchRegions.html"
---

# GetSketchRegions Method (ISketch)

Gets the sketch regions in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchRegions() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Object

value = instance.GetSketchRegions()
```

### C#

```csharp
System.object GetSketchRegions()
```

### C++/CLI

```cpp
System.Object^ GetSketchRegions();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [sketch regions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRegion.html)

## VBA Syntax

See [Sketch::GetSketchRegions](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSketchRegions.html).

## Examples

[Get Sketch Regions (VBA)](Get_Sketch_Regions_Example_VB.htm)
[Get Sketch Regions (VB.NET)](Get_Sketch_Regions_Example_VBNET.htm)
[Get Sketch Regions (C#)](Get_Sketch_Regions_Example_CSharp.htm)

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSketchRegionCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchRegionCount.html)
[ISketch::IGetSketchRegions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchRegions.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
