---
title: "IStructureSystemFolder Interface"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemFolder"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder.html"
---

# IStructureSystemFolder Interface

Allows access to a structure system folder.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IStructureSystemFolder
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemFolder
```

### C#

```csharp
public interface IStructureSystemFolder
```

### C++/CLI

```cpp
public interface class IStructureSystemFolder
```

## VBA Syntax

See [StructureSystemFolder](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemFolder.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

See the [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.html) examples.

See the [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html) examples.

See the [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.html) examples.

See the [IPrimaryMemberRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.html) examples.

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html) examples.

## Remarks

This interface accesses the top-level folder of a structure system in the FeatureManager design tree. The structure system folder contains one or more profile group folders. Each profile group folder contains profile references and structure system members.

When a structure system is created in the user interface, the Corner Management PropertyManager opens automatically. When structure systems are created using the API, a Corner Management`X` folder is automatically created for each structure system in the FeatureManager design tree.

A structure system and its corner management folder appears similar to the following in the FeatureManager design tree. In parentheses are the APIs that you use to access the corresponding item:

- **Structure System1** (IStructureSystemFolder accessors)

- **Structure System Grid1**

- **<ansi inch> <c channel><3 x 5> (1)** ([IProfileGroupFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder.html) accessors)

- **Plane2** (profile reference plane - [IProfileGroupFolder::GetPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~GetPlane.html))

- **Sketch11** (profile sketch - [IProfileGroupFolder::GetSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~GetSketch.html))

- **Member1** (structure system member - [IProfileGroupFolder::GetStructureSystemMembers](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~GetStructureSystemMembers.html))

- **Corner Management1** ([ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) accessors)

- **Complex Corner Group1** ([ICornerTreatmentGroupFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentGroupFolder.html) accessors)

- **Corner5** ([ICornerTreatmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData.html) accessors and then cast to [IComplexCornerTreatmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData.html))

- more corners...

(Each corner in a complex corner group contains multiple corner members. If you edit a corner to open a Corner Management PropertyManager in the user interface, on the Complex tab are three boxes that list corner members for Trim Tool, Body Trim, and Planar Trim. Use [ICornerMember](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember.html) to access these corner members.)

- **Two member Corner Group1** (ICornerTreatmentGroupFolder accessors)

- **Corner1** (ICornerTreatmentFeatureData accessors and then cast to [ITwoMemberCornerTreatmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData.html))

- more corners...

(Each corner in a two member corner group contains two corner members, one for Trim Tool, and one for Body Trim. Use ICornerMember to access these corner members.)

- **Simple Corner Group1** (ICornerTreatmentGroupFolder accessors)

- **Corner9** (ICornerTreatmentFeatureData accessors and then cast to [ISimpleCornerTreatmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData.html))

- more corners...

To create a structure system:

1. Create an [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.html) object for every primary and secondary structure system member you intend to create.
2. Create [IStructureSystemSplitMember](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember.html) objects as needed. Use [IStructureSystemMemberFeatureData::IsSplit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~IsSplit.html) to indicate that split members exist.
3. Create one or more [IStructureSystemMemberProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.html) objects as the number of different profiles is needed.
4. Cast the IStructureSystemMemberFeatureData objects to [IPrimaryStructuralMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryStructuralMemberFeatureData.html) objects and [ISecondaryStructuralMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryStructuralMemberFeatureData.html) objects as needed.
5. Create specific primary member feature data objects by casting IPrimaryStructuralMemberFeatureData objects to:

  - [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.html)
  - [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.html)
  - [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html)
  - [IPrimaryMemberRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.html)
6. Create specific secondary member feature data objects by casting ISecondaryStructuralMemberFeatureData objects to:

  - [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html)
  - [ISecondaryMemberSupportPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData.html)
7. Use the methods and properties on the specific primary and secondary member feature data objects to detail the structure system members.
8. Call [IModelDocExtension::CreateStructureSystem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateStructureSystem.html)(`primaryFDArray`, `secondaryFDArray`), where `primaryFDArray` is an array of primary IStructureSystemMemberFeatureData objects and `secondaryFDArray` is an array of secondary IStructureSystemMemberFeatureData objects created in step 1.

To edit a structure system:

1. Get the structure system folder feature, which is returned by IModelDocExtension::CreateStructureSystem in step 8 above. Then call the accessor of this interface, IFeature::GetSpecificFeature2.
  (Or call both accessors of this interface.)
2. Use [IStructureSystemFolder::GetProfileGroupFolders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder~GetProfileGroupFolders.html) to access the profile group folders in a structure system folder.
3. Use IProfileGroupFolder methods and properties to get the sketch, reference plane, and structure system members in each profile group folder.
4. Use [IStructureSystemMemberFeatureData::StructureSystemMemberType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~StructureSystemMemberType.html) to determine whether a structure system member retrieved in step 3 is a primary or a secondary member.
5. Call [IStructureSystemMemberFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~AccessSelections.html) before editing the selections used to create the structure system. Call [IStructureSystemMemberFeatureData::ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~ReleaseSelectionAccess.html) after editing.
6. Cast IStructureSystemMemberFeatureData objects to their subclass feature data objects (see create steps 5 and 6).
7. If you need to change a structure member's profile, use [IStructureSystemMemberFeatureData::MemberProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~MemberProfile.html) to get the IStructureSystemMemberProfile object for each structure member.
8. Complete the structure system edit by calling [IStructureSystemMemberFeatureData::GetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~GetFeature.html), calling methods and properties on objects retrieved in previous steps as required, and finally calling [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).

Use the examples as models to create and edit structure sytems in your own applications.

For more information, read the **SOLIDWORKS Design user-interface help > Weldments and Structure System > Structure System** topics.

## Accessors

[ICircularPatternFeatureData::StructureSystemToPatternArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~StructureSystemToPatternArray.html)

[ICornerManagementFolder::GetStructureSystemFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder~GetStructureSystemFolder.html) and then [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html)

[IFeatureManager::GetStructureSystemFolders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetStructureSystemFolders.html) and then IFeature::GetSpecificFeature2

[ILinearPatternFeatureData::StructureSystemToPatternArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~StructureSystemToPatternArray.html)

[IMirrorSolidFeatureData::StructureSystemToPatternArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~StructureSystemToPatternArray.html)

## Access Diagram

[StructureSystemFolder](SWObjectModel.pdf#StructureSystemFolder)

## See Also

[IStructureSystemFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
