---
title: "D2Direction Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "D2Direction"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2Direction.html"
---

# D2Direction Property (ICurveDrivenPatternFeatureData)

Gets or sets Direction 2 of this bidirectional curve-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2Direction As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Object

instance.D2Direction = value

value = instance.D2Direction
```

### C#

```csharp
System.object D2Direction {get; set;}
```

### C++/CLI

```cpp
property System.Object^ D2Direction {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pattern direction entity

## VBA Syntax

See [CurveDrivenPatternFeatureData::D2Direction](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~D2Direction.html).

## Remarks

The pattern direction can be a curve, edge, sketch entity, or a sketch. You must pre-select the Direction 2 entity using selection Mark = 2 before creating the feature definition. Use this property only when editing the pattern feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::D1Direction Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D1Direction.html)
[ICurveDrivenPatternFeatureData::Dir2Specified Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~Dir2Specified.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
