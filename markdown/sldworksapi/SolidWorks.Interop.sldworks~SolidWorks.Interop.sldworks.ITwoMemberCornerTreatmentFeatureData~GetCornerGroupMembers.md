---
title: "GetCornerGroupMembers Method (ITwoMemberCornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITwoMemberCornerTreatmentFeatureData"
member: "GetCornerGroupMembers"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData~GetCornerGroupMembers.html"
---

# GetCornerGroupMembers Method (ITwoMemberCornerTreatmentFeatureData)

Gets the corner group members of this two member corner treatment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCornerGroupMembers() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITwoMemberCornerTreatmentFeatureData
Dim value As System.Object

value = instance.GetCornerGroupMembers()
```

### C#

```csharp
System.object GetCornerGroupMembers()
```

### C++/CLI

```cpp
System.Object^ GetCornerGroupMembers();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.html)s

## VBA Syntax

See [TwoMemberCornerTreatmentFeatureData::GetCornerGroupMembers](ms-its:sldworksapivb6.chm::/sldworks~TwoMemberCornerTreatmentFeatureData~GetCornerGroupMembers.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## See Also

[ITwoMemberCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData.html)
[ITwoMemberCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
