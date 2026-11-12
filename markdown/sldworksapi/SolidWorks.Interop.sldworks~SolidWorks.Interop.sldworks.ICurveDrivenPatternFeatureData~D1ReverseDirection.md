---
title: "D1ReverseDirection Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "D1ReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D1ReverseDirection.html"
---

# D1ReverseDirection Property (ICurveDrivenPatternFeatureData)

Gets or sets whether the pattern direction is reversed in Direction 1.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1ReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Boolean

instance.D1ReverseDirection = value

value = instance.D1ReverseDirection
```

### C#

```csharp
System.bool D1ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool D1ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True reverses the pattern direction, false does not

## VBA Syntax

See [CurveDrivenPatternFeatureData::D1ReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~D1ReverseDirection.html).

## Examples

[Create and Access Curve-driven Pattern Feature (C#)](Create_and_Access_Curve-driven_Pattern_Feature_Example_CSharp.htm)
[Create and Access Curve-driven Pattern Feature (VB.NET)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VBNET.htm)
[Create and Access Curve-driven Pattern Feature (VBA)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VB.htm)

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::D2ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2ReverseDirection.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
