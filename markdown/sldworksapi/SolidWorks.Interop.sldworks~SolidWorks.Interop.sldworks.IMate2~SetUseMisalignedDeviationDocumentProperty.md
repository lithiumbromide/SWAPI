---
title: "SetUseMisalignedDeviationDocumentProperty Method (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "SetUseMisalignedDeviationDocumentProperty"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetUseMisalignedDeviationDocumentProperty.html"
---

# SetUseMisalignedDeviationDocumentProperty Method (IMate2)

Sets whether to use the document property value for the maximum misalignment deviation for the misaligned concentric mate.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetUseMisalignedDeviationDocumentProperty( _
   ByVal UseDocumentProperty As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim UseDocumentProperty As System.Boolean

instance.SetUseMisalignedDeviationDocumentProperty(UseDocumentProperty)
```

### C#

```csharp
void SetUseMisalignedDeviationDocumentProperty(
   System.bool UseDocumentProperty
)
```

### C++/CLI

```cpp
void SetUseMisalignedDeviationDocumentProperty(
   System.bool UseDocumentProperty
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDocumentProperty`: True to use the document property value for maximum misalignment deviation, false to not

## VBA Syntax

See [Mate2::SetUseMisalignedDeviationDocumentProperty](ms-its:sldworksapivb6.chm::/sldworks~Mate2~SetUseMisalignedDeviationDocumentProperty.html).

## Remarks

If [IMate2::GetCurrentMisalignedDeviation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetCurrentMisalignedDeviation.html) is greater than the document property value of the maximum misalignment deviation, then the mate fails to solve.

The current deviation and the maximum deviation are cumulative across both concentric mates in the Hole Set. For example, if [IMate2::GetConcentricAlignmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetConcentricAlignmentType.html) is set to [swConcentricAlignmentType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConcentricAlignmentType_e.html).swConcentricAlignSymmetric, the deviation from both holes is summed before comparison with the maximum deviation.

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::GetUseMisalignedDeviationDocumentProperty Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetUseMisalignedDeviationDocumentProperty.html)
[IMate2::SetMaximumMisalignedDeviation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetMaximumMisalignedDeviation.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
