---
title: "Sketch Property (IProjectionCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IProjectionCurveFeatureData"
member: "Sketch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~Sketch.html"
---

# Sketch Property (IProjectionCurveFeatureData)

Gets or sets the sketch to project in this projection curve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Sketch As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionCurveFeatureData
Dim value As System.Object

instance.Sketch = value

value = instance.Sketch
```

### C#

```csharp
System.object Sketch {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Sketch {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[ISketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)

## VBA Syntax

See [ProjectionCurveFeatureData::Sketch](ms-its:sldworksapivb6.chm::/sldworks~ProjectionCurveFeatureData~Sketch.html).

## Remarks

You cannot use this property to get or set the target sketch for sketch-on-sketch projection curve features. You can only pre-select the target sketch before creating the feature. See the [IProjectionCurveFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.html) Remarks.

Use [IFeature::GetSpecificFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html) to get the ISketch object from the selected [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IProjectionCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.html)
[IProjectionCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData_members.html)
[IProjectionCurveFeatureData::Reverse Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~Reverse.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
