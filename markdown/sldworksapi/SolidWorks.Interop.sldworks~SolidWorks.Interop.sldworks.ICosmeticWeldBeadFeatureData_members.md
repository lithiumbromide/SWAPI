---
title: "ICosmeticWeldBeadFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html"
---

# ICosmeticWeldBeadFeatureData Interface Members

The following tables list the members exposed by [ICosmeticWeldBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BeadSize | Gets or sets the thickness of a weld bead. |
| Property | FromToLength | Gets or sets whether to enable the from/to length properties. |
| Property | FromToReverse | Gets or sets whether to start the weld from the opposite end. |
| Property | FromToStartPoint | Gets or sets the position of the first weld bead with respect to the end of the selected face or edge. |
| Property | FromToWeldLength | Gets or sets the length of the weld. |
| Property | Gap | Gets or sets the gap between intermittent weld beads. |
| Property | GapOrPitch | Gets or sets whether to use gap or pitch spacing for intermittent weld beads. |
| Property | IntermittentWeld | Gets or sets whether to enable intermittent weld properties. |
| Property | IntermittentWeldLength | Gets or sets the length of the weld for intermittent weld beads. |
| Property | Pitch | Gets or sets the pitch of intermittent weld beads. |
| Property | Side | Gets or sets how the weld bead is applied to selected faces or edges. |
| Property | Staggered | Gets or sets whether to alternate the positioning of the weld beads on both sides of the weld body. |
| Property | TangentPropagation | Gets or sets whether to apply the weld bead to all edges that are tangent to the selected faces or edges. |
| Property | WeldSymbol | Gets or sets the weld symbol for this weld bead. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this cosmetic weld bead feature. |
| Method | GetEntities | Obso lete. Superseded by ICosmeticWeldBeadFeatureData::GetEntitiesWeldFrom and ICosmeticWeldBeadFeatureData::GetEntitiesWeldTo. |
| Method | GetEntitiesWeldFrom | Gets the weld-from entity type and weld-from entities for this cosmetic weld bead, which was created using weld geometry. |
| Method | GetEntitiesWeldPath | Gets the entities for this cosmetic weld bead, which was created using a weld path. |
| Method | GetEntitiesWeldTo | Gets the weld-to entity type and weld-to entities for this cosmetic weld bead, which was created using weld geometry. |
| Method | GetReferenceEdges | Gets the reference edges created by this cosmetic weld bead feature. |
| Method | GetWeldBeadFolder | Gets the weld bead folder. |
| Method | ReleaseSelectionAccess | Releases access to the selections that define this cosmetic weld bead feature. |
| Method | SetEntities | Obso lete. Superseded by ICosmeticWeldBeadFeatureData::SetEntitiesWeldFrom and ICosmeticWeldBeadFeatureData::SetEntitiesWeldTo. |
| Method | SetEntitiesWeldFrom | Sets the weld-from entities for this cosmetic weld bead, which was created using weld geometry. |
| Method | SetEntitiesWeldPath | Sets the entities for this cosmetic weld bead, which was created using a weld path. |
| Method | SetEntitiesWeldTo | Sets the weld-to entities for this cosmetic weld bead, which was created using weld geometry. |

[Top](#topBookmark)

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ICosmeticWeldBeadFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFolder.html)
[IFeatureManager::InsertCosmeticWeldBead2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCosmeticWeldBead2.html)
