---
title: "GetResponseSpectrumUseMaterialDamping2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetResponseSpectrumUseMaterialDamping2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumUseMaterialDamping2.html"
---

# GetResponseSpectrumUseMaterialDamping2 Method (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetResponseSpectrumUseMaterialDamping3](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumUseMaterialDamping3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetResponseSpectrumUseMaterialDamping2( _
   ByRef BChecked As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim BChecked As System.Integer
Dim value As System.Integer

value = instance.GetResponseSpectrumUseMaterialDamping2(BChecked)
```

### C#

```csharp
System.int GetResponseSpectrumUseMaterialDamping2(
   out System.int BChecked
)
```

### C++/CLI

```cpp
System.int GetResponseSpectrumUseMaterialDamping2(
   [Out] System.int BChecked
)
```

### Parameters

- `BChecked`: 1 to use the material damping ratio, 0 to not (see **Remarks**)

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::GetResponseSpectrumUseMaterialDamping2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetResponseSpectrumUseMaterialDamping2.html).

## Remarks

This method is valid only if the mode combination method is Complete Quadratic Combination (CQC). See [ICWDynamicStudyOptions::GetResponseSpectrumModeCombinationMethod2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumModeCombinationMethod2.html) and [ICWDynamicStudyOptions::SetResponseSpectrumModeCombinationMethod2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumModeCombinationMethod2.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::SetResponseSpectrumUseMaterialDamping2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumUseMaterialDamping2.html)
[ICWDynamicStudyOptions::GetResponseSpectrumClusterFactor2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumClusterFactor2.html)
[ICWDynamicStudyOptions::GetResponseSpectrumCurveInterpolation2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumCurveInterpolation2.html)
[ICWDynamicStudyOptions::SetResponseSpectrumClusterFactor2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumClusterFactor2.html)
[ICWDynamicStudyOptions::SetResponseSpectrumCurveInterpolation2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumCurveInterpolation2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
