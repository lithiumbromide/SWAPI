---
title: "ResponseSpectrumUseMaterialDamping Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "ResponseSpectrumUseMaterialDamping"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~ResponseSpectrumUseMaterialDamping.html"
---

# ResponseSpectrumUseMaterialDamping Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetResponseSpectrumUseMaterialDamping2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumUseMaterialDamping2.html) and [ICWDynamicStudyOptions::SetResponseSpectrumUseMaterialDamping2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumUseMaterialDamping2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property ResponseSpectrumUseMaterialDamping As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Integer

instance.ResponseSpectrumUseMaterialDamping = value

value = instance.ResponseSpectrumUseMaterialDamping
```

### C#

```csharp
System.int ResponseSpectrumUseMaterialDamping {get; set;}
```

### C++/CLI

```cpp
property System.int ResponseSpectrumUseMaterialDamping {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to use the material damping ratio, 0 to not (see **Remarks**)

## VBA Syntax

See [CWDynamicStudyOptions::ResponseSpectrumUseMaterialDamping](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~ResponseSpectrumUseMaterialDamping.html).

## Remarks

This property is valid only if [ICWDynamicStudyOptions::ResponseSpectrumModeCombinationMethod](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~ResponseSpectrumModeCombinationMethod.html) = 2 (Complete Quadratic Combination (CQC)).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::ResponseSpectrumClusterFactor Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~ResponseSpectrumClusterFactor.html)
[ICWDynamicStudyOptions::ResponseSpectrumCurveInterpolation Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~ResponseSpectrumCurveInterpolation.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
