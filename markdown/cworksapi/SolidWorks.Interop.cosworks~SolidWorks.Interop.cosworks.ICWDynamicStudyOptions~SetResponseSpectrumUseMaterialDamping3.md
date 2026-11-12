---
title: "SetResponseSpectrumUseMaterialDamping3 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetResponseSpectrumUseMaterialDamping3"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumUseMaterialDamping3.html"
---

# SetResponseSpectrumUseMaterialDamping3 Method (ICWDynamicStudyOptions)

Sets whether to use the material damping ratio in the response spectrum dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetResponseSpectrumUseMaterialDamping3( _
   ByVal BChecked As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim BChecked As System.Boolean
Dim value As System.Integer

value = instance.SetResponseSpectrumUseMaterialDamping3(BChecked)
```

### C#

```csharp
System.int SetResponseSpectrumUseMaterialDamping3(
   System.bool BChecked
)
```

### C++/CLI

```cpp
System.int SetResponseSpectrumUseMaterialDamping3(
   System.bool BChecked
)
```

### Parameters

- `BChecked`: -1 or true to use the material damping ratio, 0 or false to not (see **Remarks**)

### Return Value

0 indicates success; a non-0 value indicates failure

## Remarks

This method is valid only if the mode combination methods is Complete Quadratic Combination (CQC). See [ICWDynamicStudyOptions::GetResponseSpectrumModeCombinationMethod2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetResponseSpectrumModeCombinationMethod2.html) and [ICWDynamicStudyOptions::SetResponseSpectrumModeCombinationMethod2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetResponseSpectrumModeCombinationMethod2.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
