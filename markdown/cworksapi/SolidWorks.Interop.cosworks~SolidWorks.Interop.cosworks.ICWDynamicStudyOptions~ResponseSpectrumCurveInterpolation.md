---
title: "ResponseSpectrumCurveInterpolation Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "ResponseSpectrumCurveInterpolation"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~ResponseSpectrumCurveInterpolation.html"
---

# ResponseSpectrumCurveInterpolation Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetResponseSpectrumCurveInterpolation2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumCurveInterpolation2.html) and [ICWDynamicStudyOptions::SetResponseSpectrumCurveInterpolation2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumCurveInterpolation2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property ResponseSpectrumCurveInterpolation As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Integer

instance.ResponseSpectrumCurveInterpolation = value

value = instance.ResponseSpectrumCurveInterpolation
```

### C#

```csharp
System.int ResponseSpectrumCurveInterpolation {get; set;}
```

### C++/CLI

```cpp
property System.int ResponseSpectrumCurveInterpolation {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Curve interpolation as defined in [swsInterpolationType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsInterpolationType_e.html)

## VBA Syntax

See [CWDynamicStudyOptions::ResponseSpectrumCurveInterpolation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~ResponseSpectrumCurveInterpolation.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::ResponseSpectrumClusterFactor Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~ResponseSpectrumClusterFactor.html)
[ICWDynamicStudyOptions::ResponseSpectrumModeCombinationMethod Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~ResponseSpectrumModeCombinationMethod.html)
[ICWDynamicStudyOptions::ResponseSpectrumUseMaterialDamping Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~ResponseSpectrumUseMaterialDamping.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
