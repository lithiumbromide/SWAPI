---
title: "GuideCurveInfluence Property (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "GuideCurveInfluence"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GuideCurveInfluence.html"
---

# GuideCurveInfluence Property (ILoftFeatureData)

Gets or sets the type of guide curve influence for this loft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property GuideCurveInfluence As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim value As System.Integer

instance.GuideCurveInfluence = value

value = instance.GuideCurveInfluence
```

### C#

```csharp
System.int GuideCurveInfluence {get; set;}
```

### C++/CLI

```cpp
property System.int GuideCurveInfluence {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of guide curve influence as defined in [swGuideCurveInfluence_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swGuideCurveInfluence_e.html)

## VBA Syntax

See [LoftFeatureData::GuideCurveInfluence](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~GuideCurveInfluence.html).

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)
[ILoftFeatureData::GetGuideCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetGuideCurvesCount.html)
[ILoftFeatureData::GetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetGuideCurvesType.html)
[ILoftFeatureData::GetGuideTangencyType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetGuideTangencyType.html)
[ILoftFeatureData::IGetGuideCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IGetGuideCurves.html)
[ILoftFeatureData::IGetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IGetGuideCurvesType.html)
[ILoftFeatureData::ISetGuideCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ISetGuideCurves.html)
[ILoftFeatureData::SetGuideTangencyType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~SetGuideTangencyType.html)
[ILoftFeatureData::GuideCurves Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GuideCurves.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
