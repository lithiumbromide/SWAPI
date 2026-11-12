---
title: "D2PatternSeedOnly Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "D2PatternSeedOnly"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2PatternSeedOnly.html"
---

# D2PatternSeedOnly Property (ICurveDrivenPatternFeatureData)

Gets or sets whether to replicate the seed pattern only in Direction 2, without replicating the curve pattern created under Direction 1.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2PatternSeedOnly As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Boolean

instance.D2PatternSeedOnly = value

value = instance.D2PatternSeedOnly
```

### C#

```csharp
System.bool D2PatternSeedOnly {get; set;}
```

### C++/CLI

```cpp
property System.bool D2PatternSeedOnly {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True patterns the seed feature only in Direction 2

## VBA Syntax

See [CurveDrivenPatternFeatureData::D2PatternSeedOnly](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~D2PatternSeedOnly.html).

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::Dir2Specified Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~Dir2Specified.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
