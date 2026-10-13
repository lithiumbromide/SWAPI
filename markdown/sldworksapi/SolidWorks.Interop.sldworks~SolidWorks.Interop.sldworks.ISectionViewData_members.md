---
title: "ISectionViewData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html"
---

# ISectionViewData Interface Members

The following tables list the members exposed by [ISectionViewData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ExcludeSelectedItems | Gets or sets whether to exclude or include the specific bodies in the multibody part or specific components in the assembly in selective sectioning in this section view. |
| Property | FirstColor | Gets or sets the first color of the section view in the part or assembly. |
| Property | FirstOffset | Gets or sets the first offset distance of the section view for this part or assembly. |
| Property | FirstPlane | Gets or sets the section plane for the first section of the section view for the part or assembly. |
| Property | FirstReverseDirection | Gets or sets whether to reverse the first direction of the section view for this part or assembly. |
| Property | FirstRotationX | Gets or sets the first x rotation of the section view in the part or assembly. |
| Property | FirstRotationY | Gets or sets the first y rotation of the section view in the part or assembly. |
| Property | GraphicsOnlySection | Gets or sets whether to generate a graphics-only section view. |
| Property | KeepCapColor | Gets or sets whether to color the caps of section views. |
| Property | Redraw | Gets or sets whether to have IModelViewManager::CreateSectionView validate and return a status for section bodies instead of section views. |
| Property | SecondColor | Gets or sets the second color of the section view in the part or assembly. |
| Property | SecondOffset | Gets or sets the second offset distance of the section view for this part or assembly. |
| Property | SecondPlane | Gets or sets the section plane for the second section of the section view for the part or assembly. |
| Property | SecondReverseDirection | Gets or sets whether to reverse the second direction of the section view for this part or assembly. |
| Property | SecondRotationX | Gets or sets the second x rotation of the section view in the part or assembly. |
| Property | SecondRotationY | Gets or sets the second y rotation of the section view in the part or assembly. |
| Property | SectionedZones | Gets or sets the intersection zones that define how to section this section view. |
| Property | SectionTransparentItemsTransparent | Gets or sets whether the specified sectioned bodies in the multibody part or the specified sectioned components in the assembly are transparently sectioned in this section view. |
| Property | SelectiveSection | Gets or sets whether selective sectioning is enabled in this section view. |
| Property | SelectiveSectioningList | Gets or sets the bodies in the multibody part or the components in the assembly for selective sectioning in this section view. |
| Property | ShowSectionCap | Gets or sets whether to cap the section views. |
| Property | ThirdColor | Gets or sets the third color of the section view in this part or assembly. |
| Property | ThirdOffset | Gets or sets the third offset distance of the section view for this part or assembly. |
| Property | ThirdPlane | Gets or sets the section plane for the third section of the section view for the part or assembly. |
| Property | ThirdReverseDirection | Gets or sets whether to reverse the third direction of the section view for this part or assembly. |
| Property | ThirdRotationX | Gets or sets the third x rotation of the section view in the part or assembly. |
| Property | ThirdRotationY | Gets or sets the third y rotation of the section view in the part or assembly. |
| Property | TransparencyList | Gets or sets the sectioned bodies in the multibody part or the sectioned components in the assembly to transparently section in this section view. |
| Property | TransparencyValue | Gets or sets the level of transparency for the specified transparently sectioned bodies in the multibody part or the specified transparently sectioned components in the assembly in this section view. |
| Property | TransparentSection | Gets or sets whether transparent sectioning is enabled in this section view. |
| Property | ZonalSection | Gets or sets whether the section method is zonal or planar. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetDynamicCenterTransform | Gets the translation between the center of the model and the plane in the specified section in this section view. |
| Method | GetFirstPlaneParameters | Gets the first transformed plane's parameters for this section view. |
| Method | GetSecondPlaneParameters | Gets the second transformed plane's parameters for this section view. |
| Method | GetThirdPlaneParameters | Gets the third transformed plane's parameters for this section view. |

[Top](#topBookmark)

## See Also

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
