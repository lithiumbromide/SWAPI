---
title: "PatternBodyArray Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "PatternBodyArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PatternBodyArray.html"
---

# PatternBodyArray Property (ICurveDrivenPatternFeatureData)

Gets or sets a list of the bodies to pattern for this curve-driven pattern.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternBodyArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Object

instance.PatternBodyArray = value

value = instance.PatternBodyArray
```

### C#

```csharp
System.object PatternBodyArray {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PatternBodyArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) to pattern

## VBA Syntax

See [CurveDrivenPatternFeatureData::PatternBodyArray](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~PatternBodyArray.html).

## Remarks

This property is valid only if:

- you have a multilbody part,

- and -

- [ICurveDrivenPatternFeatureData::BodyPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~BodyPattern.html) is true.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::GetPatternBodyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~GetPatternBodyCount.html)
[ICurveDrivenPatternFeatureData::IGetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~IGetPatternBodyArray.html)
[ICurveDrivenPatternFeatureData::ISetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~ISetPatternBodyArray.html)
[ICurveDrivenPatternFeatureData::BodyPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~BodyPattern.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
