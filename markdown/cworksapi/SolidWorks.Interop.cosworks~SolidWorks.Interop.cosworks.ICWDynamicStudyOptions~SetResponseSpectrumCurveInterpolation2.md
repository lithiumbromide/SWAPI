---
title: "SetResponseSpectrumCurveInterpolation2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetResponseSpectrumCurveInterpolation2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumCurveInterpolation2.html"
---

# SetResponseSpectrumCurveInterpolation2 Method (ICWDynamicStudyOptions)

Sets the curve interpolation used by this response spectrum dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetResponseSpectrumCurveInterpolation2( _
   ByVal NInterpolation As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim NInterpolation As System.Integer
Dim value As System.Integer

value = instance.SetResponseSpectrumCurveInterpolation2(NInterpolation)
```

### C#

```csharp
System.int SetResponseSpectrumCurveInterpolation2(
   System.int NInterpolation
)
```

### C++/CLI

```cpp
System.int SetResponseSpectrumCurveInterpolation2(
   System.int NInterpolation
)
```

### Parameters

- `NInterpolation`: Curve interpolation as defined in [swsInterpolationType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsInterpolationType_e.html)

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::SetResponseSpectrumCurveInterpolation2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetResponseSpectrumCurveInterpolation2.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetResponseSpectrumCurveInterpolation2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumCurveInterpolation2.html)
[ICWDynamicStudyOptions::SetResponseSpectrumClusterFactor2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumClusterFactor2.html)
[ICWDynamicStudyOptions::SetResponseSpectrumModeCombinationMethod2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumModeCombinationMethod2.html)
[ICWDynamicStudyOptions::SetResponseSpectrumUseMaterialDamping2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumUseMaterialDamping2.html)
[ICWDynamicStudyOptions::GetResponseSpectrumClusterFactor2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumClusterFactor2.html)
[ICWDynamicStudyOptions::GetResponseSpectrumModeCombinationMethod2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumModeCombinationMethod2.html)
[ICWDynamicStudyOptions::GetResponseSpectrumUseMaterialDamping2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumUseMaterialDamping2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
