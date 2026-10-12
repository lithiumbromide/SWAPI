---
title: "ISketchRegion Interface"
project: "SOLIDWORKS API Help"
interface: "ISketchRegion"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion.html"
---

# ISketchRegion Interface

Provides access to sketch regions.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISketchRegion
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRegion
```

### C#

```csharp
public interface ISketchRegion
```

### C++/CLI

```cpp
public interface class ISketchRegion
```

## VBA Syntax

See [SketchRegion](ms-its:sldworksapivb6.chm::/sldworks~SketchRegion.html).

## Examples

[Determine If Sketch Contour or Sketch Region (VBA)](Determine_if_Sketch_Contour_or_Sketch_Region_Example_VB.htm)
[Get Sketch Regions (VBA)](Get_Sketch_Regions_Example_VB.htm)
[Get Sketch Regions (VB.NET)](Get_Sketch_Regions_Example_VBNET.htm)
[Get Sketch Regions (C#)](Get_Sketch_Regions_Example_CSharp.htm)

## Remarks

Sketch regions are white space on a sketch bordered by sketch entities or portions of sketch entities basically forming a face.

A centerline within a sketch creates sketch regions inside that sketch.

## Accessors

[IExtrudeFeatureData2::Contours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~Contours.html)

[IExtrudeFeatureData2::IGetContours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IGetContours.html)

[IRevolveFeatureData2::Contours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~Contours.html)

[IRevolveFeatureData2::IGetContours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IGetContours.html)

[ISketch::GetSketchRegions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchRegions.html) and [ISketch::IGetSketchRegions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetSketchRegions.html)

[ISplitLineFeatureData::Contours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~Contours.html)

[ISplitLineFeatureData::IGetContours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~IGetContours.html)

## Access Diagram

[SketchRegion](SWObjectModel.pdf#SketchRegion)

## See Also

[ISketchRegion Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
