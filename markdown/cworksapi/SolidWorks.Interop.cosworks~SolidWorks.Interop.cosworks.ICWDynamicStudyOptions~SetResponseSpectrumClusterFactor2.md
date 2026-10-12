---
title: "SetResponseSpectrumClusterFactor2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetResponseSpectrumClusterFactor2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumClusterFactor2.html"
---

# SetResponseSpectrumClusterFactor2 Method (ICWDynamicStudyOptions)

Sets the cluster factor for the response spectrum dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetResponseSpectrumClusterFactor2( _
   ByVal DFactor As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim DFactor As System.Double
Dim value As System.Integer

value = instance.SetResponseSpectrumClusterFactor2(DFactor)
```

### C#

```csharp
System.int SetResponseSpectrumClusterFactor2(
   System.double DFactor
)
```

### C++/CLI

```cpp
System.int SetResponseSpectrumClusterFactor2(
   System.double DFactor
)
```

### Parameters

- `DFactor`: Cluster factor (see **Remarks**)

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::SetResponseSpectrumClusterFactor2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetResponseSpectrumClusterFactor2.html).

## Remarks

This property is valid only if the mode combination method is Absolute Sum. See [ICWDynamicStudyOptions::GetResponseSpectrumModeCombinationMethod2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumModeCombinationMethod2.html) and [ICWDynamicStudyOptions::SetResponseSpectrumModeCombinationMethod2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumModeCombinationMethod2.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetResponseSpectrumClusterFactor2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumClusterFactor2.html)
[ICWDynamicStudyOptions::SetResponseSpectrumCurveInterpolation2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumCurveInterpolation2.html)
[ICWDynamicStudyOptions::SetResponseSpectrumModeCombinationMethod2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumModeCombinationMethod2.html)
[ICWDynamicStudyOptions::SetResponseSpectrumUseMaterialDamping2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumUseMaterialDamping2.html)
[ICWDynamicStudyOptions::GetResponseSpectrumCurveInterpolation2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumCurveInterpolation2.html)
[ICWDynamicStudyOptions::GetResponseSpectrumUseMaterialDamping2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumUseMaterialDamping2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
