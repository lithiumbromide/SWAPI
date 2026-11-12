---
title: "IFillPatternFeatureData Interface Properties"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData_properties"
member: ""
kind: "properties"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_properties.html"
---

# IFillPatternFeatureData Interface Properties

For a list of all members of this type, see [IFillPatternFeatureData members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AutoSelect | Gets or sets whether to automatically select all or only specific bodies in a multibody part to be affected by this fill pattern feature. |
| Property | CreateSeedCutPolygonSides | Gets or sets the number of sides in a polygon-cut seed instance of this fill pattern feature. |
| Property | CreateSeedCutType | Gets or sets the type of cut for this fill pattern's seed instance. |
| Property | Diagonal | Gets or sets the length of the diagonal of a diamond-cut seed instance of this fill pattern feature. |
| Property | Diameter | Gets or sets the diameter of a circle-cut seed instance of this fill pattern feature. |
| Property | Dimension | Gets or sets the length of a side of a diamond-cut or square-cut seed instance of this fill pattern feature. |
| Property | FeatureScope | Gets or sets whether to use scope for this fill pattern feature in a multibody part. |
| Property | FeatureScopeBodies | Gets or sets the solid bodies that the fill pattern feature affects in a multibody part. |
| Property | FeaturesToPatternType | Gets or sets the type of object to pattern in this fill pattern feature. |
| Property | GeometryPattern | Gets or sets whether to create this fill pattern using an exact copy of the seed feature. |
| Property | InnerRadius | Gets or sets the radius of the circle that inscribes the polygon-cut seed instance of this fill pattern feature. |
| Property | InstanceSpacing | Gets or sets the distance between the pattern instance centers of this fill pattern feature. |
| Property | LayoutSpacingType | Gets or sets the type of spacing between the instances in the layout of this fill pattern feature. |
| Property | LoopSpacing | Gets or sets the distance between loops of pattern instances in this fill pattern feature. |
| Property | Margins | Gets or sets the distance between the fill boundary and the outermost pattern instance in the layout of this fill pattern feature. |
| Property | NoOfInstances | Gets or sets the number of instances per loop or side of the layout of this fill pattern feature. |
| Property | OuterRadius | Gets or sets the radius of the circle that circumscribes the polygon-cut seed instance of this fill pattern feature. |
| Property | PatternBodyArray | Gets or sets the array of bodies to pattern in this fill pattern feature. |
| Property | PatternDirection | Gets or sets the direction reference for the layout of this fill pattern feature. |
| Property | PatternDirectionType | Gets the type of pattern direction reference returned by IFillPatternFeatureData::PatternDirection for this fill pattern feature. |
| Property | PatternElement | Gets or sets the pattern element selection of this fill pattern feature. |
| Property | PatternFaceArray | Gets or sets the array of faces to pattern in this fill pattern feature. |
| Property | PatternFeatureArray | Gets or sets the array of features to pattern in this fill pattern feature. |
| Property | PatternFillBoundaryArray | Gets or sets the array of objects representing the boundary of this fill pattern feature. |
| Property | PatternLayoutPolygonSides | Gets or sets the number of sides in the polygonal layout of this fill pattern feature. |
| Property | PatternLayoutType | Gets or sets the layout of the pattern instances within the fill boundary of this fill pattern feature. |
| Property | PropagateVisualProperty | Gets or sets whether to propagate visual properties (e.g., colors, textures, cosmetic thread data, etc.) to all fill pattern instances in this fill pattern feature. |
| Property | Rotation | Gets or sets the counterclockwise rotation of the seed instance of this fill pattern feature. |
| Property | SeedCutFlipShapeDirection | Gets or sets whether to reverse the direction of the seed instance cut of this fill pattern feature. |
| Property | SeedFeatureCenter | Gets or sets the vertex or sketch point where to place the center of the seed cut feature of this fill pattern feature. |
| Property | SeedFeatureCenterType | Gets or sets the type of entity where to place the center of the seed cut feature for this fill pattern feature. |
| Property | SkippedItemArray | Gets or sets the pattern instances to skip in this fill pattern feature. |
| Property | StaggerAngle | Gets or sets the angle by which to stagger the rows of pattern instances in the perforation layout of this fill pattern feature. |

[Top](#topBookmark)

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
