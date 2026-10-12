---
title: "SetMaximumMisalignedDeviation Method (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "SetMaximumMisalignedDeviation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetMaximumMisalignedDeviation.html"
---

# SetMaximumMisalignedDeviation Method (IMate2)

Sets the maximum allowed misalignment deviation for this misaligned concentric mate.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMaximumMisalignedDeviation( _
   ByVal MaximumDeviation As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim MaximumDeviation As System.Double

instance.SetMaximumMisalignedDeviation(MaximumDeviation)
```

### C#

```csharp
void SetMaximumMisalignedDeviation(
   System.double MaximumDeviation
)
```

### C++/CLI

```cpp
void SetMaximumMisalignedDeviation(
   System.double MaximumDeviation
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MaximumDeviation`: Maximum allowed misalignment deviation

## VBA Syntax

See [Mate2::SetMaximumMisalignedDeviation](ms-its:sldworksapivb6.chm::/sldworks~Mate2~SetMaximumMisalignedDeviation.html).

## Remarks

This method is valid only if [IMate2::GetUseMisalignedDeviationDocumentProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetUseMisalignedDeviationDocumentProperty.html) returns false. Call [IMate2::SetUseMisalignedDeviationDocumentProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetUseMisalignedDeviationDocumentProperty.html) to set UseDocumentProperty to false if you want to use this method to set the maximum misaligned deviation for this mate.

If [IMate2::GetCurrentMisalignedDeviation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetCurrentMisalignedDeviation.html) is greater than the value set by this method, then the mate fails to solve.

The current deviation and the maximum deviation are cumulative across both concentric mates in the Hole Set. For example, if [IMate2::GetConcentricAlignmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetConcentricAlignmentType.html) is set to [swConcentricAlignmentType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConcentricAlignmentType_e.html).swConcentricAlignSymmetric, the deviation from both holes is summed before comparison with the maximum deviation.

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::GetMaximumMisalignedDeviation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetMaximumMisalignedDeviation.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
