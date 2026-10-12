---
title: "FeatureScope Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "FeatureScope"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~FeatureScope.html"
---

# FeatureScope Property (ICurveDrivenPatternFeatureData)

Gets which bodies in this multibody part are affected by this curve-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FeatureScope As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Boolean

value = instance.FeatureScope
```

### C#

```csharp
System.bool FeatureScope {get;}
```

### C++/CLI

```cpp
property System.bool FeatureScope {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to specify affected bodies, false to apply the pattern to all bodies every time the feature regenerates

## VBA Syntax

See [CurveDrivenPatternFeatureData::FeatureScope](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~FeatureScope.html).

## Remarks

This property is valid only if [ICurveDrivenPatternFeatureData::GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~GeometryPattern.html) is true.

Call [ICurveDrivenPatternFeatureData::SetFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~SetFeatureScope.html) to set this property.

For more information, see the **Curve Driven Patterns and the** **Curve Driven Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
