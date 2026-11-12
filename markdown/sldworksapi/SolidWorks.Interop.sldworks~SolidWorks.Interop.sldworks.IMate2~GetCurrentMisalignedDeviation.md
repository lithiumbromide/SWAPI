---
title: "GetCurrentMisalignedDeviation Method (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "GetCurrentMisalignedDeviation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetCurrentMisalignedDeviation.html"
---

# GetCurrentMisalignedDeviation Method (IMate2)

Gets the current misalignment deviation for the misaligned concentric mate.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurrentMisalignedDeviation() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim value As System.Double

value = instance.GetCurrentMisalignedDeviation()
```

### C#

```csharp
System.double GetCurrentMisalignedDeviation()
```

### C++/CLI

```cpp
System.double GetCurrentMisalignedDeviation();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Current misalignment deviation

## VBA Syntax

See [Mate2::GetCurrentMisalignedDeviation](ms-its:sldworksapivb6.chm::/sldworks~Mate2~GetCurrentMisalignedDeviation.html).

## Remarks

If the current deviation of misalignment is greater than [IMate2::GetMaximumMisalignedDeviation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetMaximumMisalignedDeviation.html), then the mate fails to solve.

The current deviation and the maximum deviation are cumulative across both concentric mates in the Hole Set. For example, if [IMate2::GetConcentricAlignmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetConcentricAlignmentType.html) is set to [swConcentricAlignmentType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConcentricAlignmentType_e.html).swConcentricAlignSymmetric, the deviation from both holes is summed before comparison with the maximum deviation.

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
