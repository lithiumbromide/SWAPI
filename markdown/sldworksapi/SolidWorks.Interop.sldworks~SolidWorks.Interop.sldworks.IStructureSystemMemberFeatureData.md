---
title: "IStructureSystemMemberFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.html"
---

# IStructureSystemMemberFeatureData Interface

Allows access to a structure system member.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IStructureSystemMemberFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberFeatureData
```

### C#

```csharp
public interface IStructureSystemMemberFeatureData
```

### C++/CLI

```cpp
public interface class IStructureSystemMemberFeatureData
```

## VBA Syntax

See [StructureSystemMemberFeatureData](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberFeatureData.html).

## Examples

See the [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.html) examples.

See the [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html) examples.

See the [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.html) examples.

See the [IPrimaryMemberRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.html) examples.

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html) examples.

## Remarks

This interface is the superclass of [IPrimaryStructuralMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryStructuralMemberFeatureData.html) and [ISecondaryStructuralMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryStructuralMemberFeatureData.html).

See the [IStructureSystemFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder.html) Remarks.

For more information about structure system members, see the **SOLIDWORKS Design user-interface help > Weldments and Structure System > Structure System > Primary Member PropertyManager** and **Secondary Member PropertyManager** topics.

## Accessors

[IComplexCornerTreatmentFeatureData::GetBodyTrimMembers](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~GetBodyTrimMembers.html)

[IComplexCornerTreatmentFeatureData::GetPlanarTrimMembers](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~GetPlanarTrimMembers.html)

[ICornerMember::GetUnderlyingMemberFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember~GetUnderlyingMemberFeature.html) and then [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html)

[IModelDocExtension::CreateStructureSystemMemberData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateStructureSystemMemberData.html)

[IProfileGroupFolder::GetStructureSystemMembers](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~GetStructureSystemMembers.html)

[ISecondaryMemberBetweenPointsFeatureData::GetMemberPairs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData~GetMemberPairs.html)

[ISecondaryMemberSupportPlaneFeatureData::GetMemberPairs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData~GetMemberPairs.html)

[ISecondaryMemberUpToMembersFeatureData::GetFromPointMembers](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~GetFromPointMembers.html)

[ISecondaryMemberUpToMembersFeatureData::GetPointMemberPairs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~GetPointMemberPairs.html)

[ITwoMemberCornerTreatmentFeatureData::GetCornerGroupMembers](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData~GetCornerGroupMembers.html)

## Access Diagram

[StructureSystemMemberFeatureData](SWObjectModel.pdf#StructureSystemMemberFD)

## See Also

[IStructureSystemMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
