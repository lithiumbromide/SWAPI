---
title: "GetMemberPairs Method (ISecondaryMemberSupportPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberSupportPlaneFeatureData"
member: "GetMemberPairs"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData~GetMemberPairs.html"
---

# GetMemberPairs Method (ISecondaryMemberSupportPlaneFeatureData)

Gets the primary structure system members that pair together to create this secondary structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMemberPairs() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberSupportPlaneFeatureData
Dim value As System.Object

value = instance.GetMemberPairs()
```

### C#

```csharp
System.object GetMemberPairs()
```

### C++/CLI

```cpp
System.Object^ GetMemberPairs();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.html)s

## VBA Syntax

See [SecondaryMemberSupportPlaneFeatureData::GetMemberPairs](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberSupportPlaneFeatureData~GetMemberPairs.html).

## See Also

[ISecondaryMemberSupportPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData.html)
[ISecondaryMemberSupportPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
