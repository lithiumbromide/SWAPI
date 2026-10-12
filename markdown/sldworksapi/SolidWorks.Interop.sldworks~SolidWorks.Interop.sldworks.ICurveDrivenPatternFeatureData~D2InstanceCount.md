---
title: "D2InstanceCount Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "D2InstanceCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2InstanceCount.html"
---

# D2InstanceCount Property (ICurveDrivenPatternFeatureData)

Gets or sets the number of instances in Direction 2 of this bidirectional curve-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2InstanceCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Integer

instance.D2InstanceCount = value

value = instance.D2InstanceCount
```

### C#

```csharp
System.int D2InstanceCount {get; set;}
```

### C++/CLI

```cpp
property System.int D2InstanceCount {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of instances

## VBA Syntax

See [CurveDrivenPatternFeatureData::D2InstanceCount](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~D2InstanceCount.html).

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::D1InstanceCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D1InstanceCount.html)
[ICurveDrivenPatternFeatureData::Dir2Specified Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~Dir2Specified.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
