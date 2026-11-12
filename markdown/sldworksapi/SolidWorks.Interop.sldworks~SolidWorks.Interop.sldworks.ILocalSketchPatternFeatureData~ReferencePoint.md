---
title: "ReferencePoint Property (ILocalSketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalSketchPatternFeatureData"
member: "ReferencePoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~ReferencePoint.html"
---

# ReferencePoint Property (ILocalSketchPatternFeatureData)

Gets or sets the type of reference point for this sketch-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferencePoint As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalSketchPatternFeatureData
Dim value As System.Integer

instance.ReferencePoint = value

value = instance.ReferencePoint
```

### C#

```csharp
System.int ReferencePoint {get; set;}
```

### C++/CLI

```cpp
property System.int ReferencePoint {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of reference point as defined in [swLocalSketchPatternReferencePoint_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLocalSketchPatternReferencePoint_e.html)

## VBA Syntax

See [LocalSketchPatternFeatureData::ReferencePoint](ms-its:sldworksapivb6.chm::/sldworks~LocalSketchPatternFeatureData~ReferencePoint.html).

## Examples

[Create Local Sketch-driven Pattern (C#)](Create_Local_Sketch-driven_Pattern_Example_CSharp.htm)
[Create Local Sketch-driven Pattern (VB.NET)](Create_Local_Sketch-driven_Pattern_Example_VBNET.htm)
[Create Local Sketch-driven Pattern (VBA)](Create_Local_Sketch-driven_Pattern_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalSketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.html)
[ILocalSketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData_members.html)
[ILocalSketchPatternFeatureData::GetReferencePointType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~GetReferencePointType.html)
[ILocalSketchPatternFeatureData::SelectedPoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~SelectedPoint.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
