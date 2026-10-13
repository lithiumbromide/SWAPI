---
title: "ILoftedBendsFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ILoftedBendsFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.html"
---

# ILoftedBendsFeatureData Interface Members

The following tables list the members exposed by [ILoftedBendsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BendLineControlOption | Gets or sets the lofted bend line control options. |
| Property | Direction | Gets or sets the thickness direction of this lofted bends feature. |
| Property | FacetingOption | Gets or sets how facets are created in this lofted bend feature. |
| Property | FacetValue | Gets or sets the value corresponding to ILoftedBendsFeatureData::FacetingOption . |
| Property | FormedMethod | Gets or sets whether this lofted bend feature is formed. |
| Property | MaximumDeviation | Gets or sets the maximum deviation for the bend lines in a lofted bend feature. |
| Property | NumberOfBendLines | Gets or sets the number of bend lines in this lofted bend feature. |
| Property | Profiles | Gets or sets the profiles for this lofted bends feature. |
| Property | ReferToEndPoint | Gets or sets whether to calculate facet transitions using theoretical vertexes. |
| Property | SymmetricThickness | Gets or sets whether to symmetrically thicken this bi-directional lofted bends feature. |
| Property | Thickness | Gets or sets the thickness for this lofted bends feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Accesses the selections used to define the lofted bends feature. |
| Method | CanCreateBendLines | Gets whether the bend lines parameters affect this lofted bend feature. |
| Method | GetProfileCount | Gets the number of profiles in this lofted bends feature. |
| Method | IAccessSelections | Accesses the selections used to define the lofted bends feature |
| Method | IGetProfiles | Gets the profiles for this lofted bends feature. |
| Method | ISetProfiles | Sets the profiles for this lofted bends feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections for this lofted bends feature. |

[Top](#topBookmark)

## See Also

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertSheetMetalLoftedBend Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalLoftedBend.html)
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
