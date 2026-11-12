---
title: "CreateStructureSystem Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "CreateStructureSystem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateStructureSystem.html"
---

# CreateStructureSystem Method (IModelDocExtension)

Creates a structure system feature using the specified primary and secondary member arrays.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateStructureSystem( _
   ByVal PrimaryMembersData As System.Object, _
   ByVal SecondaryMembersData As System.Object _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim PrimaryMembersData As System.Object
Dim SecondaryMembersData As System.Object
Dim value As Feature

value = instance.CreateStructureSystem(PrimaryMembersData, SecondaryMembersData)
```

### C#

```csharp
Feature CreateStructureSystem(
   System.object PrimaryMembersData,
   System.object SecondaryMembersData
)
```

### C++/CLI

```cpp
Feature^ CreateStructureSystem(
   System.Object^ PrimaryMembersData,
   System.Object^ SecondaryMembersData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PrimaryMembersData`: Array of primary [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.html) objects; null or Nothing if none
- `SecondaryMembersData`: Array of secondary IStructureSystemMemberFeatureData objects; null or Nothing if none

### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [ModelDocExtension::CreateStructureSystem](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~CreateStructureSystem.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

See the [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.html) examples.

See the [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html) examples.

See the [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.html) examples.

See the [IPrimaryMemberRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.html) examples.

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html) examples.

## Remarks

The feature returned is an [IStructureSystemFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder.html). Use [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html) to get the specific interface.

See the IStructureSystemFolder Remarks.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
