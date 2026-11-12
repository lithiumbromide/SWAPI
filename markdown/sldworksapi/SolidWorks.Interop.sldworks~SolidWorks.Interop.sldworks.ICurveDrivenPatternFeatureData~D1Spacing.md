---
title: "D1Spacing Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "D1Spacing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D1Spacing.html"
---

# D1Spacing Property (ICurveDrivenPatternFeatureData)

Gets or sets the spacing for this curve-driven pattern in Direction 1.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1Spacing As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Double

instance.D1Spacing = value

value = instance.D1Spacing
```

### C#

```csharp
System.double D1Spacing {get; set;}
```

### C++/CLI

```cpp
property System.double D1Spacing {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pattern spacing

## VBA Syntax

See [CurveDrivenPatternFeatureData::D1Spacing](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~D1Spacing.html).

## Examples

[Create and Access Curve-driven Pattern Feature (C#)](Create_and_Access_Curve-driven_Pattern_Feature_Example_CSharp.htm)
[Create and Access Curve-driven Pattern Feature (VB.NET)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VBNET.htm)
[Create and Access Curve-driven Pattern Feature (VBA)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VB.htm)

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::D2Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2Spacing.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
