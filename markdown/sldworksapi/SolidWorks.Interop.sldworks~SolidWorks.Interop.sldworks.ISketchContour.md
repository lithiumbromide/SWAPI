---
title: "ISketchContour Interface"
project: "SOLIDWORKS API Help"
interface: "ISketchContour"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.html"
---

# ISketchContour Interface

Provides access to sketch contours.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISketchContour
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchContour
```

### C#

```csharp
public interface ISketchContour
```

### C++/CLI

```cpp
public interface class ISketchContour
```

## VBA Syntax

See [SketchContour](ms-its:sldworksapivb6.chm::/sldworks~SketchContour.html).

## Examples

[Get Sketch Contours (VBA)](Get_Sketch_Contours_Example_VB.htm)
[Create Extrude Feature Using Sketch Contours (C#)](Create_Extrude_Feature_Using_Sketch_Contours_Example_CSharp.htm)
[Create Extrude Feature Using Sketch Contours (VB.NET)](Create_Extrude_Feature_Using_Sketch_Contours_Example_VBNET.htm)
[Create Extrude Feature Using Sketch Contours (VBA)](Create_Extrude_Feature_Using_Sketch_Contours_Example_VB.htm)

## Remarks

Sketch contours are a collection of end-point connected sketch segments that might, or might not, form a face depending on whether the sketch segments form a closed area.

## Accessors

[IExtrudeFeatureData2::Contours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~Contours.html)

[IExtrudeFeatureData2::IGetContours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IGetContours.html)

[IRevolveFeatureData2::Contours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~Contours.html)

[IRevolveFeatureData2::IGetContours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IGetContours.html)

[ISketch::GetSketchContours](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchContours.html) and [ISketch::IGetSketchContours](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetSketchContours.html)

[ISplitLineFeatureData::Contours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~Contours.html)

[ISplitLineFeatureData::IGetContours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~IGetContours.html)

## Access Diagram

[SketchContour](SWObjectModel.pdf#SketchContour)

## See Also

[ISketchContour Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
