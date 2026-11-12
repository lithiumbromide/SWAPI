---
title: "Dir2Specified Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "Dir2Specified"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~Dir2Specified.html"
---

# Dir2Specified Property (ICurveDrivenPatternFeatureData)

Gets or sets whether Direction 2 is specified for this curve-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Dir2Specified As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Boolean

instance.Dir2Specified = value

value = instance.Dir2Specified
```

### C#

```csharp
System.bool Dir2Specified {get; set;}
```

### C++/CLI

```cpp
property System.bool Dir2Specified {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if Direction 2 is specified, false if not

## VBA Syntax

See [CurveDrivenPatternFeatureData::Dir2Specified](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~Dir2Specified.html).

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::D2Direction Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2Direction.html)
[ICurveDrivenPatternFeatureData::D2InstanceCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2InstanceCount.html)
[ICurveDrivenPatternFeatureData::D2IsEqualSpaced Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2IsEqualSpaced.html)
[ICurveDrivenPatternFeatureData::D2PatternSeedOnly Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2PatternSeedOnly.html)
[ICurveDrivenPatternFeatureData::D2ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2ReverseDirection.html)
[ICurveDrivenPatternFeatureData::D2Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2Spacing.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
