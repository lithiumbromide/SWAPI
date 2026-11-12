---
title: "BodyPattern Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "BodyPattern"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~BodyPattern.html"
---

# BodyPattern Property (ICurveDrivenPatternFeatureData)

Gets or sets whether to base this curve-driven pattern feature on bodies or features and faces.

## Syntax

### Visual Basic (Declaration)

```vb
Property BodyPattern As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Boolean

instance.BodyPattern = value

value = instance.BodyPattern
```

### C#

```csharp
System.bool BodyPattern {get; set;}
```

### C++/CLI

```cpp
property System.bool BodyPattern {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True for bodies, false for features and faces

## VBA Syntax

See [CurveDrivenPatternFeatureData::BodyPattern](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~BodyPattern.html).

## Remarks

If this property is:

- True, use [ICurveDrivenPatternFeatureData::PatternBodyArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PatternBodyArray.html) to specify the seed bodies to pattern.
- False, use [ICurveDrivenPatternFeatureData::PatternFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PatternFaceArray.html) or [ICurveDrivenPatternFeatureData::PatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PatternFeatureArray.html) to specify the face or feature seeds to pattern.

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::PatternElement Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PatternElement.html)
[ICurveDrivenPatternFeatureData::IGetPatternBodyArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~IGetPatternBodyArray.html)
[ICurveDrivenPatternFeatureData::IGetPatternFaceArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~IGetPatternFaceArray.html)
[ICurveDrivenPatternFeatureData::IGetPatternFeatureArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~IGetPatternFeatureArray.html)
[ICurveDrivenPatternFeatureData::ISetPatternBodyArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~ISetPatternBodyArray.html)
[ICurveDrivenPatternFeatureData::ISetPatternFaceArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~ISetPatternFaceArray.html)
[ICurveDrivenPatternFeatureData::ISetPatternFeatureArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~ISetPatternFeatureArray.html)

## Availability

SOLIDWORKS 2015 SP4, Revision Number 23.4
