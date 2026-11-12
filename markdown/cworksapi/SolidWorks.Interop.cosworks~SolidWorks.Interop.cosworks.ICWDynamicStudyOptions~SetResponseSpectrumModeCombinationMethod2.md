---
title: "SetResponseSpectrumModeCombinationMethod2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetResponseSpectrumModeCombinationMethod2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumModeCombinationMethod2.html"
---

# SetResponseSpectrumModeCombinationMethod2 Method (ICWDynamicStudyOptions)

Sets the mode combination method used by this response spectrum dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetResponseSpectrumModeCombinationMethod2( _
   ByVal NMethod As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim NMethod As System.Integer
Dim value As System.Integer

value = instance.SetResponseSpectrumModeCombinationMethod2(NMethod)
```

### C#

```csharp
System.int SetResponseSpectrumModeCombinationMethod2(
   System.int NMethod
)
```

### C++/CLI

```cpp
System.int SetResponseSpectrumModeCombinationMethod2(
   System.int NMethod
)
```

### Parameters

- `NMethod`: Mode combination method as defined in [swsModeCombinationMethod_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsModeCombinationMethod_e.html)

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::SetResponseSpectrumModeCombinationMethod2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetResponseSpectrumModeCombinationMethod2.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetResponseSpectrumModeCombinationMethod2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumModeCombinationMethod2.html)
[ICWDynamicStudyOptions::SetResponseSpectrumClusterFactor2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumClusterFactor2.html)
[ICWDynamicStudyOptions::SetResponseSpectrumCurveInterpolation2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumCurveInterpolation2.html)
[ICWDynamicStudyOptions::SetResponseSpectrumUseMaterialDamping2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumUseMaterialDamping2.html)
[ICWDynamicStudyOptions::GetResponseSpectrumClusterFactor2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumClusterFactor2.html)
[ICWDynamicStudyOptions::GetResponseSpectrumCurveInterpolation2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumCurveInterpolation2.html)
[ICWDynamicStudyOptions::GetResponseSpectrumUseMaterialDamping2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumUseMaterialDamping2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
