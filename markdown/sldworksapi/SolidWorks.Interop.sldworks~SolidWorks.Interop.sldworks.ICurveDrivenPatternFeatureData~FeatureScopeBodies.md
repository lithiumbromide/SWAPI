---
title: "FeatureScopeBodies Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "FeatureScopeBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~FeatureScopeBodies.html"
---

# FeatureScopeBodies Property (ICurveDrivenPatternFeatureData)

Gets the bodies in this multibody part that are affected by this curve-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FeatureScopeBodies As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Object

value = instance.FeatureScopeBodies
```

### C#

```csharp
System.object FeatureScopeBodies {get;}
```

### C++/CLI

```cpp
property System.Object^ FeatureScopeBodies {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html) to be affected

## VBA Syntax

See [CurveDrivenPatternFeatureData::FeatureScopeBodies](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~FeatureScopeBodies.html).

## Remarks

This property is valid only if [ICurveDrivenPatternFeatureData::GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~GeometryPattern.html) is true.

Call [ICurveDrivenPatternFeatureData::SetFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~SetFeatureScope.html) to set this property.

For more information, see the **Curve Driven Patterns and the** **Curve Driven Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
