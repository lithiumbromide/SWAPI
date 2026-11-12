---
title: "GetResponseSpectrumCurveInterpolation2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetResponseSpectrumCurveInterpolation2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumCurveInterpolation2.html"
---

# GetResponseSpectrumCurveInterpolation2 Method (ICWDynamicStudyOptions)

Gets the curve interpolation used by this response spectrum dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetResponseSpectrumCurveInterpolation2( _
   ByRef NInterpolation As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim NInterpolation As System.Integer
Dim value As System.Integer

value = instance.GetResponseSpectrumCurveInterpolation2(NInterpolation)
```

### C#

```csharp
System.int GetResponseSpectrumCurveInterpolation2(
   out System.int NInterpolation
)
```

### C++/CLI

```cpp
System.int GetResponseSpectrumCurveInterpolation2(
   [Out] System.int NInterpolation
)
```

### Parameters

- `NInterpolation`: Curve interpolation as defined in [swsInterpolationType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsInterpolationType_e.html)

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::GetResponseSpectrumCurveInterpolation2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetResponseSpectrumCurveInterpolation2.html).

## Examples

[Create Linear Dynamic Response Spectrum Study (VBA)](Create_Dynamic_Response_Spectrum_Study_Example_VB.htm)
[Create Linear Dynamic Response Spectrum Study (VB.NET)](Create_Dynamic_Response_Spectrum_Study_Example_VBNET.htm)
[Create Linear Dynamic Response Spectrum Study (C#)](Create_Dynamic_Response_Spectrum_Study_Example_CSharp.htm)

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::SetResponseSpectrumCurveInterpolation2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumCurveInterpolation2.html)
[ICWDynamicStudyOptions::GetResponseSpectrumClusterFactor2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumClusterFactor2.html)
[ICWDynamicStudyOptions::GetResponseSpectrumModeCombinationMethod2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumModeCombinationMethod2.html)
[ICWDynamicStudyOptions::GetResponseSpectrumUseMaterialDamping2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumUseMaterialDamping2.html)
[ICWDynamicStudyOptions::SetResponseSpectrumClusterFactor2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumClusterFactor2.html)
[ICWDynamicStudyOptions::SetResponseSpectrumModeCombinationMethod2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumModeCombinationMethod2.html)
[ICWDynamicStudyOptions::SetResponseSpectrumUseMaterialDamping2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumUseMaterialDamping2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
