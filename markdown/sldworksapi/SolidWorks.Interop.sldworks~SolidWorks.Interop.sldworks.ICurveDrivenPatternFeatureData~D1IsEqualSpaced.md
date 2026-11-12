---
title: "D1IsEqualSpaced Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "D1IsEqualSpaced"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D1IsEqualSpaced.html"
---

# D1IsEqualSpaced Property (ICurveDrivenPatternFeatureData)

Gets or sets whether the pattern items are equally spaced in Direction 1.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1IsEqualSpaced As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Boolean

instance.D1IsEqualSpaced = value

value = instance.D1IsEqualSpaced
```

### C#

```csharp
System.bool D1IsEqualSpaced {get; set;}
```

### C++/CLI

```cpp
property System.bool D1IsEqualSpaced {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True spaces the pattern items equally, false does not

## VBA Syntax

See [CurveDrivenPatternFeatureData::D1IsEqualSpaced](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~D1IsEqualSpaced.html).

## Examples

[Create and Access Curve-driven Pattern Feature (C#)](Create_and_Access_Curve-driven_Pattern_Feature_Example_CSharp.htm)
[Create and Access Curve-driven Pattern Feature (VB.NET)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VBNET.htm)
[Create and Access Curve-driven Pattern Feature (VBA)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VB.htm)

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::D2IsEqualSpaced Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2IsEqualSpaced.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
