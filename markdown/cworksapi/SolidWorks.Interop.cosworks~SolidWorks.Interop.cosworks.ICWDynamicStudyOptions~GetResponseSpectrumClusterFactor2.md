---
title: "GetResponseSpectrumClusterFactor2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetResponseSpectrumClusterFactor2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumClusterFactor2.html"
---

# GetResponseSpectrumClusterFactor2 Method (ICWDynamicStudyOptions)

Gets the cluster factor for the response spectrum dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetResponseSpectrumClusterFactor2( _
   ByRef DFactor As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim DFactor As System.Double
Dim value As System.Integer

value = instance.GetResponseSpectrumClusterFactor2(DFactor)
```

### C#

```csharp
System.int GetResponseSpectrumClusterFactor2(
   out System.double DFactor
)
```

### C++/CLI

```cpp
System.int GetResponseSpectrumClusterFactor2(
   [Out] System.double DFactor
)
```

### Parameters

- `DFactor`: Cluster factor (see **Remarks**)

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::GetResponseSpectrumClusterFactor2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetResponseSpectrumClusterFactor2.html).

## Examples

[Create Linear Dynamic Response Spectrum Study (VBA)](Create_Dynamic_Response_Spectrum_Study_Example_VB.htm)
[Create Linear Dynamic Response Spectrum Study (VB.NET)](Create_Dynamic_Response_Spectrum_Study_Example_VBNET.htm)
[Create Linear Dynamic Response Spectrum Study (C#)](Create_Dynamic_Response_Spectrum_Study_Example_CSharp.htm)

## Remarks

This property is valid only if the mode combination method is Absolute Sum. See [ICWDynamicStudyOptions::GetResponseSpectrumModeCombinationMethod2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumModeCombinationMethod2.html) and [ICWDynamicStudyOptions::SetResponseSpectrumModeCombinationMethod2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumModeCombinationMethod2.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::SetResponseSpectrumClusterFactor2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumClusterFactor2.html)
[ICWDynamicStudyOptions::GetResponseSpectrumCurveInterpolation2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumCurveInterpolation2.html)
[ICWDynamicStudyOptions::GetResponseSpectrumUseMaterialDamping2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumUseMaterialDamping2.html)
[ICWDynamicStudyOptions::SetResponseSpectrumCurveInterpolation2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumCurveInterpolation2.html)
[ICWDynamicStudyOptions::SetResponseSpectrumUseMaterialDamping2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumUseMaterialDamping2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
