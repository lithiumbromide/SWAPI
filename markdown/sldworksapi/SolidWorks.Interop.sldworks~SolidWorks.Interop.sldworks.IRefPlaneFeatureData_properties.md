---
title: "IRefPlaneFeatureData Interface Properties"
project: "SOLIDWORKS API Help"
interface: "IRefPlaneFeatureData_properties"
member: ""
kind: "properties"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_properties.html"
---

# IRefPlaneFeatureData Interface Properties

For a list of all members of this type, see [IRefPlaneFeatureData members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Angle | Gets or sets the angle of the reference plane feature. |
| Property | AngleOrDistance | Gets or sets the angle or distance of the specified reference for this reference plane feature. |
| Property | AutoSize | Gets or sets whether to automatically size the reference plane feature to either the geometry on which it is created or to the bounding box of the model geometry. |
| Property | Constraint | Gets or sets the constraint for the specified reference for this reference plane feature. |
| Property | Distance | Gets or sets the distance, in meters, to offset the reference plane feature. |
| Property | OriginOnCurve | Gets or sets whether to place the origin on the curve for this reference plane feature. |
| Property | ProjectionType | Gets or sets the projection type for this on-surface reference plane feature. |
| Property | Reference | Gets or sets the reference entity for the specified reference for this reference plane feature. |
| Property | ReverseDirection | Obsolete. Superseded by IRefPlaneFeatureData::ReversedReferenceDirection . |
| Property | ReversedReferenceDirection | Gets or sets whether to reverse the direction of the specified reference for this reference plane feature. |
| Property | Selections | Gets or sets the selected entities used to create the reference plane feature or sets the entities to use to create the reference plane feature. |
| Property | SolutionIndex | Gets or sets the intended plane when there are multiple planes from which to select for an on-surface reference plane feature. |
| Property | Type | Gets the type of reference plane created in SOLIDWORKS 2009 or earlier. Can also get whether a constraint-based reference plane created in SOLIDWORKS 2010 or has angle or offset distance references. NOTE: This property is a get-only property. Set is not implemented . |
| Property | Type2 | Gets whether the reference plane is constraint based; thus, created in SOLIDWORKS 2010 and later. NOTE: This property is a get-only property. Set is not implemented . |
| Property | UpdatePlane | Gets or sets whether to update this reference plane so that it is parallel to the screen. |
| Property | UseNormalPlane | Gets or sets whether to: Use the plane normal to the selected plane Automatically size the plane to either the geometry on which it is created or to the bounding box of the model geometry |

[Top](#topBookmark)

## See Also

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IRefPlane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)
