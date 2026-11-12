---
title: "GetMaximumMisalignedDeviation Method (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "GetMaximumMisalignedDeviation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetMaximumMisalignedDeviation.html"
---

# GetMaximumMisalignedDeviation Method (IMate2)

Gets the maximum allowed misalignment deviation for this misaligned concentric mate.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaximumMisalignedDeviation() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim value As System.Double

value = instance.GetMaximumMisalignedDeviation()
```

### C#

```csharp
System.double GetMaximumMisalignedDeviation()
```

### C++/CLI

```cpp
System.double GetMaximumMisalignedDeviation();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Maximum allowed misalignment deviation

## VBA Syntax

See [Mate2::GetMaximumMisalignedDeviation](ms-its:sldworksapivb6.chm::/sldworks~Mate2~GetMaximumMisalignedDeviation.html).

## Remarks

If [IMate2::GetCurrentMisalignedDeviation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetCurrentMisalignedDeviation.html) is greater than the value returned by this method, then the mate fails to solve.

The current deviation and the maximum deviation are cumulative across both concentric mates in the Hole Set. For example, if [IMate2::GetConcentricAlignmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetConcentricAlignmentType.html) is set to [swConcentricAlignmentType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConcentricAlignmentType_e.html).swConcentricAlignSymmetric, the deviation from both holes is summed before comparison with the maximum deviation.

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::GetUseMisalignedDeviationDocumentProperty Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetUseMisalignedDeviationDocumentProperty.html)
[IMate2::SetMaximumMisalignedDeviation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetMaximumMisalignedDeviation.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
