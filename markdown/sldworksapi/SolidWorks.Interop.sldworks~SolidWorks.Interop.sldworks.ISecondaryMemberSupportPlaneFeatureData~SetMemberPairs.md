---
title: "SetMemberPairs Method (ISecondaryMemberSupportPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberSupportPlaneFeatureData"
member: "SetMemberPairs"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData~SetMemberPairs.html"
---

# SetMemberPairs Method (ISecondaryMemberSupportPlaneFeatureData)

Sets the primary structure system members that pair together to create this secondary structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMemberPairs( _
   ByVal Pairs As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberSupportPlaneFeatureData
Dim Pairs As System.Object
Dim value As System.Boolean

value = instance.SetMemberPairs(Pairs)
```

### C#

```csharp
System.bool SetMemberPairs(
   System.object Pairs
)
```

### C++/CLI

```cpp
System.bool SetMemberPairs(
   System.Object^ Pairs
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Pairs`: Array of [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.html)s

### Return Value

True if member pairs successfully set, false if not

## VBA Syntax

See [SecondaryMemberSupportPlaneFeatureData::SetMemberPairs](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberSupportPlaneFeatureData~SetMemberPairs.html).

## Examples

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html) examples.

## Remarks

During editing, the array can contain only two objects.

## See Also

[ISecondaryMemberSupportPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData.html)
[ISecondaryMemberSupportPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
