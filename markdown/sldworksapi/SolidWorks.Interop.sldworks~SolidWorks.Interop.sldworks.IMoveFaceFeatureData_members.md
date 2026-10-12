---
title: "IMoveFaceFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html"
---

# IMoveFaceFeatureData Interface Members

The following tables list the members exposed by [IMoveFaceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Angle | Gets or sets the angle for the Move Face feature. |
| Property | Distance | Gets or sets the offset distance of this offset or translated Move Face feature. |
| Property | EndCondition | Gets the end condition for this translated Move Face feature. |
| Property | Faces | Gets or sets the faces for the Move Face feature. |
| Property | MoveType | Gets or sets the type of Move Face feature. |
| Property | OffsetDistance | Gets or sets the offset distance of this translated Move Face feature that has an end condition of Offset From Surface . |
| Property | ReverseDirection | Gets or sets whether to reverse the direction of the Move Face feature. |
| Property | TriadRotationParameters | Gets or sets the rotation parameters for this Move Face feature. |
| Property | TriadTranslationParameters | Gets or sets the translation parameters for this Move Face feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to selections that define this Move Face feature. |
| Method | GetDirectionReference | Gets the direction reference for this Move Face feature. |
| Method | GetEndConditionEntity | Gets the entity to which the Move Face feature is translated. |
| Method | GetFacesCount | Gets the number of faces for this Move Face feature. |
| Method | GetFromEntity | Gets the entity from which the face of the Move Face feature is translated. |
| Method | IGetFaces | Gets the faces for this Move Face feature. |
| Method | IGetTriadRotationParameters | Gets the rotation parameters for this Move Face feature. |
| Method | IGetTriadTranslationParameters | Gets the translation parameters for this Move Face feature. |
| Method | ISetFaces | Sets the faces for this Move Face feature. |
| Method | ISetTriadRotationParameters | Sets the rotation parameters for this Move Face feature. |
| Method | ISetTriadTranslationParameters | Sets the translation parameters for this Move Face feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections that define this Move Face feature. |
| Method | SetDirectionReference | Sets the direction reference for the Move Face feature. |
| Method | SetEndConditionEntity | Sets the entity to which the face of the Move Face feature is translated. |
| Method | SetFromEntity | Sets the entity from which the face of the Move Face feature is translated. |

[Top](#topBookmark)

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.html)
[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.html)
[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.html)
[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.html)
[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.html)
[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html)
[IFeatureManager::InsertMoveFace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoveFace2.html)
[IFeatureManager::IInsertMoveFace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMoveFace2.html)
