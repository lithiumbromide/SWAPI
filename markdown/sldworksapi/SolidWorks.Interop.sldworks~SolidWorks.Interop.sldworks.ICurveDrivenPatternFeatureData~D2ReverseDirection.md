---
title: "D2ReverseDirection Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "D2ReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2ReverseDirection.html"
---

# D2ReverseDirection Property (ICurveDrivenPatternFeatureData)

Gets or sets whether to reverse Direction 2 for this bidirectional curve-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2ReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Boolean

instance.D2ReverseDirection = value

value = instance.D2ReverseDirection
```

### C#

```csharp
System.bool D2ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool D2ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True reverses Direction 2, false does not

## VBA Syntax

See [CurveDrivenPatternFeatureData::D2ReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~D2ReverseDirection.html).

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::D1ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D1ReverseDirection.html)
[ICurveDrivenPatternFeatureData::Dir2Specified Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~Dir2Specified.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
