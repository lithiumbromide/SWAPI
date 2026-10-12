---
title: "D1InstanceCount Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "D1InstanceCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D1InstanceCount.html"
---

# D1InstanceCount Property (ICurveDrivenPatternFeatureData)

Gets or sets the number of instances in this curve-driven pattern in Direction 1.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1InstanceCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Integer

instance.D1InstanceCount = value

value = instance.D1InstanceCount
```

### C#

```csharp
System.int D1InstanceCount {get; set;}
```

### C++/CLI

```cpp
property System.int D1InstanceCount {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of instances

## VBA Syntax

See [CurveDrivenPatternFeatureData::D1InstanceCount](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~D1InstanceCount.html).

## Examples

[Create and Access Curve-driven Pattern Feature (C#)](Create_and_Access_Curve-driven_Pattern_Feature_Example_CSharp.htm)
[Create and Access Curve-driven Pattern Feature (VB.NET)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VBNET.htm)
[Create and Access Curve-driven Pattern Feature (VBA)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VB.htm)

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::D2InstanceCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2InstanceCount.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
