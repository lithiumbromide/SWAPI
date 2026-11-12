---
title: "D1AlignmentMethod Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "D1AlignmentMethod"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D1AlignmentMethod.html"
---

# D1AlignmentMethod Property (ICurveDrivenPatternFeatureData)

Gets or sets the alignment method for this curve-driven pattern feature in Direction 1.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1AlignmentMethod As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Integer

instance.D1AlignmentMethod = value

value = instance.D1AlignmentMethod
```

### C#

```csharp
System.int D1AlignmentMethod {get; set;}
```

### C++/CLI

```cpp
property System.int D1AlignmentMethod {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Alignment method as defined in [swCurveDrivenPatternAlignment_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCurveDrivenPatternAlignment_e.html)

## VBA Syntax

See [CurveDrivenPatternFeatureData::D1AlignmentMethod](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~D1AlignmentMethod.html).

## Examples

[Create and Access Curve-driven Pattern Feature (C#)](Create_and_Access_Curve-driven_Pattern_Feature_Example_CSharp.htm)
[Create and Access Curve-driven Pattern Feature (VB.NET)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VBNET.htm)
[Create and Access Curve-driven Pattern Feature (VBA)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VB.htm)

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
