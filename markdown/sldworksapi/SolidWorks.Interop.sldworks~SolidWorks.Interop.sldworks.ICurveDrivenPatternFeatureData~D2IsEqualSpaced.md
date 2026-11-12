---
title: "D2IsEqualSpaced Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "D2IsEqualSpaced"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2IsEqualSpaced.html"
---

# D2IsEqualSpaced Property (ICurveDrivenPatternFeatureData)

Gets or sets whether the pattern items are equally spaced in Direction 2 of this bidirectional curve-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2IsEqualSpaced As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Boolean

instance.D2IsEqualSpaced = value

value = instance.D2IsEqualSpaced
```

### C#

```csharp
System.bool D2IsEqualSpaced {get; set;}
```

### C++/CLI

```cpp
property System.bool D2IsEqualSpaced {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True spaces the pattern items equally, false does not

## VBA Syntax

See [CurveDrivenPatternFeatureData::D2IsEqualSpaced](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~D2IsEqualSpaced.html).

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::D1IsEqualSpaced Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D1IsEqualSpaced.html)
[ICurveDrivenPatternFeatureData::Dir2Specified Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~Dir2Specified.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
