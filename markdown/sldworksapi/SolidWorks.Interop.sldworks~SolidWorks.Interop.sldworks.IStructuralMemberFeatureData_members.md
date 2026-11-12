---
title: "IStructuralMemberFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html"
---

# IStructuralMemberFeatureData Interface Members

The following tables list the members exposed by [IStructuralMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AllowProtrusion | Gets or sets whether to allow protrusion. |
| Property | ApplyCornerTreatment | Gets or sets whether or not to apply a corner treatment to this structural member. |
| Property | ConfigurationName | Gets or sets the name of the configuration in the custom weldment profile for this structural member. |
| Property | ConnectedSegmentsOption | Gets or sets the connected segments option. |
| Property | ConnectionType | Gets or sets the type of corner treatment at the specified connection point of this structural member. |
| Property | CornerTreatmentType | Gets or sets the type of corner treatment for this structural member. |
| Property | Groups | Gets or sets the groups to use in this structural member. |
| Property | LibraryProfileMaterial | Gets the name of the material for the library profile for this structural member. |
| Property | LocateProfilePoint | Gets or sets the point to use to locate the profile for this structural member. |
| Property | PathSegments | Gets the path segments used or sets the path segments to use to create this structural member. |
| Property | RotationAngle | Gets or sets the angle by which the structural member turns relative to the adjacent structural member. |
| Property | TransferMaterial | Gets or sets whether to transfer the material properties of a library profile for this structural member. |
| Property | WeldmentProfilePath | Gets or sets the path for the profile for this structural member. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this structural member. |
| Method | GetConnectionPoints | Gets the connection points for this structural member. |
| Method | GetConnectionPointsCount | Gets the number of sketch points for this structural member. |
| Method | GetGroupsCount | Gets the number of structural-member groups for this structural member. |
| Method | GetPathSegmentAt | Gets the sketch segment associated with the body of this structural member. |
| Method | GetPathSegmentsCount | Gets the number of path segments for this structural member. |
| Method | GetSketchSegments | Gets the sketch segments that define the path of the specified structural member body. |
| Method | IGetConnectionPoints | Gets the connection points for this structural member. |
| Method | IGetGroups | Gets the structural-member groups in this structural member. |
| Method | IGetPathSegments | Gets the path segments used to create this structural member. |
| Method | ISetGroups | Sets the structural-member groups to use in this structural member. |
| Method | ISetPathSegments | Sets the path segments to use to create this structural member. |
| Method | ReleaseSelectionAccess | Releases access to the selections that define this structural member. |

[Top](#topBookmark)

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.html)
[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.html)
[IWeldmentCutListAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation.html)
[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.html)
[IFeatureManager::InsertStructuralWeldment3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment3.html)
[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)
