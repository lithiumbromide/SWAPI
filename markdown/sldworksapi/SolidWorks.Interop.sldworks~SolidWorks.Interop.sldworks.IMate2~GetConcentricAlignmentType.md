---
title: "GetConcentricAlignmentType Method (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "GetConcentricAlignmentType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetConcentricAlignmentType.html"
---

# GetConcentricAlignmentType Method (IMate2)

Gets the alignment type of this mate.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConcentricAlignmentType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim value As System.Integer

value = instance.GetConcentricAlignmentType()
```

### C#

```csharp
System.int GetConcentricAlignmentType()
```

### C++/CLI

```cpp
System.int GetConcentricAlignmentType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Alignment type as defined in [swConcentricAlignmentType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConcentricAlignmentType_e.html)

## VBA Syntax

See [Mate2::GetConcentricAlignmentType](ms-its:sldworksapivb6.chm::/sldworks~Mate2~GetConcentricAlignmentType.html).

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::SetConcentricAlignmentType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetConcentricAlignmentType.html)
[IMate2::GetCurrentMisalignedDeviation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetCurrentMisalignedDeviation.html)
[IMate2::GetMaximumMisalignedDeviation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetMaximumMisalignedDeviation.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
