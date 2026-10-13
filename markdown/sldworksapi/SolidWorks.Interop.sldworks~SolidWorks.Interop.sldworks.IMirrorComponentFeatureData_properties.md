---
title: "IMirrorComponentFeatureData Interface Properties"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData_properties"
member: ""
kind: "properties"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_properties.html"
---

# IMirrorComponentFeatureData Interface Properties

For a list of all members of this type, see [IMirrorComponentFeatureData members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AlignmentReferences | Gets or sets the alignment references for components whose orientation axes align to them. |
| Property | BreakLinksToOriginalPart | Gets or sets whether to break links between opposite-hand components and original components. |
| Property | ComponentOrientationsAlignToComponentOrigin | Gets or sets the array of orientations for the components whose axes align to origins. |
| Property | ComponentOrientationsAlignToSelection | Gets or sets the array of orientations for the components whose axes align to a selected reference. |
| Property | ComponentsToInstanceAlignToComponentOrigin | Gets or sets the array of components whose orientation axes align to origins. |
| Property | ComponentsToInstanceAlignToSelection | Gets or sets the array of components whose orientation axes align to selected references. |
| Property | CreateDerivedConfigurations | Gets or sets whether to create a derived configuration of the opposite-hand components in the original assembly. |
| Property | DimXpertScheme | Gets or sets whether to copy the DimXpert scheme of the original components to the opposite-hand versions. |
| Property | FlipDirections | Gets or sets whether to reverse the direction of alignment for selected alignment references. |
| Property | ForceUseSeedConfiguration | Gets or sets whether to synchronize the configuration of mirror components with the configuration of the mirrored component in this mirror component feature. |
| Property | MirrorComponentsFolderLocation | Gets or sets the existing folder where all opposite-hand versions are saved. |
| Property | MirroredComponentFilenames | Gets or sets the file names of the opposite-hand component versions. |
| Property | MirrorPlane | Gets or sets the plane about which components are mirrored. |
| Property | MirrorTransferOptions | Gets or sets the items to transfer to the opposite-hand versions. |
| Property | MirrorType | Gets or sets the mirror position. |
| Property | NameModifier | Gets or sets the prefix or suffix to add to the file or configuration names of the components to be mirrored. |
| Property | NameModifierType | Gets or sets the type of modifier to apply to the opposite-hand version file name. |
| Property | OppositeHandComponents | Gets or sets the array of components for which to create opposite-hand versions. |
| Property | PlaceFilesInOneFolder | Gets or sets whether to place the opposite-hand versions in one folder. |
| Property | PreserveZAxis | Gets or sets whether to preserve the orientation of the Z-axis in the opposite-hand versions. |
| Property | PropagateFromOriginalPart | Gets or sets whether to propagate visual properties from the orginal part to the opposite-hand versions. |
| Property | ReplaceFileLocations | Gets or sets the file locations of existing files that are to be replaced with new opposite-hand versions. |
| Property | SyncFlexibleSubAssemblies | Gets or sets whether to synchronize the movement of mirrored components with the movement of seed components in the flexible subassembly. |

[Top](#topBookmark)

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IComponent2::IsMirrored Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsMirrored.html)
[IPartDoc::IsMirrored Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IsMirrored.html)
