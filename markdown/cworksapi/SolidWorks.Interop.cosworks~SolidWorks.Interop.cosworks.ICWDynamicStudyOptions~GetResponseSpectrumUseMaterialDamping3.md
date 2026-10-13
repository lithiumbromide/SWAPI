---
title: "GetResponseSpectrumUseMaterialDamping3 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetResponseSpectrumUseMaterialDamping3"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumUseMaterialDamping3.html"
---

# GetResponseSpectrumUseMaterialDamping3 Method (ICWDynamicStudyOptions)

Gets whether to use the material damping ratio in the response spectrum dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetResponseSpectrumUseMaterialDamping3( _
   ByRef BChecked As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim BChecked As System.Boolean
Dim value As System.Integer

value = instance.GetResponseSpectrumUseMaterialDamping3(BChecked)
```

### C#

```csharp
System.int GetResponseSpectrumUseMaterialDamping3(
   out System.bool BChecked
)
```

### C++/CLI

```cpp
System.int GetResponseSpectrumUseMaterialDamping3(
   [Out] System.bool BChecked
)
```

### Parameters

- `BChecked`: -1 or true to use the material damping ratio, 0 or false to not (see **Remarks**)

### Return Value

0 indicates success; a non-0 value indicates failure

## Examples

[Create Linear Dynamic Response Spectrum Study (VBA)](Create_Dynamic_Response_Spectrum_Study_Example_VB.htm)
[Create Linear Dynamic Response Spectrum Study (VB.NET)](Create_Dynamic_Response_Spectrum_Study_Example_VBNET.htm)
[Create Linear Dynamic Response Spectrum Study (C#)](Create_Dynamic_Response_Spectrum_Study_Example_CSharp.htm)

## Remarks

This method is valid only if the mode combination method is Complete Quadratic Combination (CQC). See [ICWDynamicStudyOptions::GetResponseSpectrumModeCombinationMethod2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumModeCombinationMethod2.html) and [ICWDynamicStudyOptions::SetResponseSpectrumModeCombinationMethod2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumModeCombinationMethod2.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
