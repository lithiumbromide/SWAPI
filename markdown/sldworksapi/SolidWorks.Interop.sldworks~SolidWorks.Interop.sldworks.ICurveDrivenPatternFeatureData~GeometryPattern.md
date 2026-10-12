---
title: "GeometryPattern Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "GeometryPattern"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~GeometryPattern.html"
---

# GeometryPattern Property (ICurveDrivenPatternFeatureData)

Gets or sets whether to create the pattern using only the geometry (faces and edges) of the feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property GeometryPattern As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Boolean

instance.GeometryPattern = value

value = instance.GeometryPattern
```

### C#

```csharp
System.bool GeometryPattern {get; set;}
```

### C++/CLI

```cpp
property System.bool GeometryPattern {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use only the geometry of the feature to create the pattern (faster), false to pattern and solve each instance of the feature in its entirety (slower)

## VBA Syntax

See [CurveDrivenPatternFeatureData::GeometryPattern](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~GeometryPattern.html).

## Remarks

This property is valid only if [ICurveDrivenPatternFeatureData::BodyPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~BodyPattern.html) is false.

If this property is true, you can call [ICurveDrivenPatternFeatureData::SetFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~SetFeatureScope.html).

For more information, see the **Curve Driven Patterns and the** **Curve Driven Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
