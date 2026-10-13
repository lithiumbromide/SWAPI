---
title: "GetSketchRegionCount Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSketchRegionCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchRegionCount.html"
---

# GetSketchRegionCount Method (ISketch)

Gets the number of sketch regions in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchRegionCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Integer

value = instance.GetSketchRegionCount()
```

### C#

```csharp
System.int GetSketchRegionCount()
```

### C++/CLI

```cpp
System.int GetSketchRegionCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of sketch regions

## VBA Syntax

See [Sketch::GetSketchRegionCount](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSketchRegionCount.html).

## Examples

[Get Sketch Regions (VBA)](Get_Sketch_Regions_Example_VB.htm)
[Get Sketch Regions (VB.NET)](Get_Sketch_Regions_Example_VBNET.htm)
[Get Sketch Regions (C#)](Get_Sketch_Regions_Example_CSharp.htm)

## Remarks

Call this method before calling [ISketch::IGetSketchRegions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetSketchRegions.html) to get the size of the array for that method.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketchRegion::GetSketchRegions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchRegions.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
