---
title: "SwapMembers Method (ITwoMemberCornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITwoMemberCornerTreatmentFeatureData"
member: "SwapMembers"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData~SwapMembers.html"
---

# SwapMembers Method (ITwoMemberCornerTreatmentFeatureData)

Assigns the trim tool functionality to the other member of this two member corner treatment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SwapMembers()
```

### Visual Basic (Usage)

```vb
Dim instance As ITwoMemberCornerTreatmentFeatureData

instance.SwapMembers()
```

### C#

```csharp
void SwapMembers()
```

### C++/CLI

```cpp
void SwapMembers();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [TwoMemberCornerTreatmentFeatureData::SwapMembers](ms-its:sldworksapivb6.chm::/sldworks~TwoMemberCornerTreatmentFeatureData~SwapMembers.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## Remarks

The first member appearing in the corner group members list in the user interface is assigned the trim tool function. Use this method to re-assign the trim tool function to the second member.

This method is valid only if [ITwoMemberCornerTreatmentFeatureData::CornerTreatmentTrimType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData~CornerTreatmentTrimType.html) is set to [swCornerTreatmentTrimType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentTrimType_e.html).:

- swCornerTreatmentTrim_BodyTrim

- or -

- swCornerTreatmentTrim_PlanarTrim

## See Also

[ITwoMemberCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData.html)
[ITwoMemberCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
