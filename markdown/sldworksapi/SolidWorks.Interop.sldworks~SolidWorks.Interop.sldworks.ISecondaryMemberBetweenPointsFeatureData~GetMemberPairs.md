---
title: "GetMemberPairs Method (ISecondaryMemberBetweenPointsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberBetweenPointsFeatureData"
member: "GetMemberPairs"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData~GetMemberPairs.html"
---

# GetMemberPairs Method (ISecondaryMemberBetweenPointsFeatureData)

Gets the primary structure system members that pair together to create this secondary structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMemberPairs() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberBetweenPointsFeatureData
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

See [SecondaryMemberBetweenPointsFeatureData::GetMemberPairs](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberBetweenPointsFeatureData~GetMemberPairs.html).

## See Also

[ISecondaryMemberBetweenPointsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html)
[ISecondaryMemberBetweenPointsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
