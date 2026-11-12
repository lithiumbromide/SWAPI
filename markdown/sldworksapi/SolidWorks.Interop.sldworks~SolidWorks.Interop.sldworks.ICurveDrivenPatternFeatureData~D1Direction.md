---
title: "D1Direction Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "D1Direction"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D1Direction.html"
---

# D1Direction Property (ICurveDrivenPatternFeatureData)

Gets or sets Direction 1 of this curve-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1Direction As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Object

instance.D1Direction = value

value = instance.D1Direction
```

### C#

```csharp
System.object D1Direction {get; set;}
```

### C++/CLI

```cpp
property System.Object^ D1Direction {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pattern direction entity (see **Remarks**)

## VBA Syntax

See [CurveDrivenPatternFeatureData::D1Direction](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~D1Direction.html).

## Examples

[Create and Access Curve-driven Pattern Feature (C#)](Create_and_Access_Curve-driven_Pattern_Feature_Example_CSharp.htm)
[Create and Access Curve-driven Pattern Feature (VB.NET)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VBNET.htm)
[Create and Access Curve-driven Pattern Feature (VBA)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VB.htm)

## Remarks

The pattern direction can be a curve, edge, sketch entity, or a sketch. You must pre-select the direction entity using selection Mark = 1 before creating the feature definition. If you are using a 3D curve for Direction 1, then you must also pre-select the face normal entity using selection Mark = 1024.

Use this property only when editing the pattern feature.

If you specify this property using a 3D curve, you should also specify [ICurveDrivenPatternFeatureData::D1FaceNormal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D1FaceNormal.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::D2Direction Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2Direction.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
