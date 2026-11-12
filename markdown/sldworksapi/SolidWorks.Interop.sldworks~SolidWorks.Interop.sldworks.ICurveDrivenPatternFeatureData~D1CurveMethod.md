---
title: "D1CurveMethod Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "D1CurveMethod"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D1CurveMethod.html"
---

# D1CurveMethod Property (ICurveDrivenPatternFeatureData)

Gets or sets the curve method for this curve-driven pattern feature in Direction 1.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1CurveMethod As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Integer

instance.D1CurveMethod = value

value = instance.D1CurveMethod
```

### C#

```csharp
System.int D1CurveMethod {get; set;}
```

### C++/CLI

```cpp
property System.int D1CurveMethod {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Curve method as defined in [swCurveDrivenPatternCurveMethod_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCurveDrivenPatternCurveMethod_e.html)

## VBA Syntax

See [CurveDrivenPatternFeatureData::D1CurveMethod](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~D1CurveMethod.html).

## Examples

[Create and Access Curve-driven Pattern Feature (C#)](Create_and_Access_Curve-driven_Pattern_Feature_Example_CSharp.htm)
[Create and Access Curve-driven Pattern Feature (VB.NET)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VBNET.htm)
[Create and Access Curve-driven Pattern Feature (VBA)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VB.htm)

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
