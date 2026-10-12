---
title: "SelectedPoint Property (ILocalSketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalSketchPatternFeatureData"
member: "SelectedPoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~SelectedPoint.html"
---

# SelectedPoint Property (ILocalSketchPatternFeatureData)

Gets or sets the selected point for this sketch-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SelectedPoint As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalSketchPatternFeatureData
Dim value As SketchPoint

instance.SelectedPoint = value

value = instance.SelectedPoint
```

### C#

```csharp
SketchPoint SelectedPoint {get; set;}
```

### C++/CLI

```cpp
property SketchPoint^ SelectedPoint {
   SketchPoint^ get();
   void set (    SketchPoint^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html)

## VBA Syntax

See [LocalSketchPatternFeatureData::SelectedPoint](ms-its:sldworksapivb6.chm::/sldworks~LocalSketchPatternFeatureData~SelectedPoint.html).

## Remarks

This property is valid only if [ILocalSketchPatternFeatureData::ReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~ReferencePoint.html) is set to [swLocalSketchPatternReferencePoint_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLocalSketchPatternReferencePoint_e.html).swLocalSketchPatternSelectedPoint.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalSketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.html)
[ILocalSketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData_members.html)
[ILocalSketchPatternFeatureData::GetReferencePointType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~GetReferencePointType.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
