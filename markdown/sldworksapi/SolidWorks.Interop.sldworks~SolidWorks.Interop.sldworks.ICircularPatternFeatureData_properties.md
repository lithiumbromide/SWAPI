---
title: "ICircularPatternFeatureData Interface Properties"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData_properties"
member: ""
kind: "properties"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_properties.html"
---

# ICircularPatternFeatureData Interface Properties

For a list of all members of this type, see [ICircularPatternFeatureData members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AutoSelect | Gets whether to automatically select all bodies in a multibody part intersected by this circular pattern feature. |
| Property | Axis | Gets or sets the entity used to determine the direction of this circular pattern feature. |
| Property | BodyPattern | Gets or sets whether to base this circular pattern feature on bodies and structure systems or features and faces. |
| Property | Direction2 | Gets or sets whether to create a bidirectional circular pattern feature. |
| Property | EqualSpacing | Gets or sets whether the pattern instances in Direction 1 are equally spaced in this circular pattern feature. |
| Property | EqualSpacing2 | Gets or sets whether the pattern instances in Direction 2 are equally spaced in this bidirectional circular pattern feature. |
| Property | FeatureScope | Gets which bodies in this multibody part are affected by this circular pattern feature. |
| Property | FeatureScopeBodies | Gets the bodies in this multibody part that are affected by this circular pattern feature. |
| Property | GeometryPattern | Gets or sets whether to create the pattern using only the geometry (faces and edges) of the feature. |
| Property | InstancesToVary | Gets or sets whether to vary the spacing of pattern instances in this circular pattern feature. |
| Property | PatternBodyArray | Gets or sets a list of bodies to pattern in a multibody part for this circular pattern feature. |
| Property | PatternElement | Gets or sets the type of entities on which to base this circular pattern feature. |
| Property | PatternFaceArray | Gets or sets the list of faces to pattern for this circular pattern feature. |
| Property | PatternFeatureArray | Gets or sets the seed features for the circular pattern feature. |
| Property | PropagateVisualProperty | Gets or sets whether to propagate visual properties (e.g., colors, textures, cosmetic thread data, etc.) to all pattern instances in this circular pattern feature. |
| Property | ReverseDirection | Gets or sets whether the direction of the axis should be reversed in this circular pattern feature. |
| Property | SkippedItemArray | Gets or sets the list of items to skip in this circular pattern feature. |
| Property | Spacing | Gets or sets the spacing between pattern instances in Direction 1 of the circular pattern feature. |
| Property | Spacing2 | Gets or sets the spacing between pattern instances in Direction 2 of this bidirectional circular pattern feature. |
| Property | StructureSystemToPatternArray | Gets or sets the structure systems to pattern in this circular pattern feature. |
| Property | Symmetric | Gets or sets whether to create a symmetric or asymmetric circular pattern feature in Direction 2. |
| Property | TotalInstances | Gets or sets the total number of pattern instances in Direction 1 of this circular pattern feature. |
| Property | TotalInstances2 | Gets or sets the total number of pattern instances in Direction 2 of this bidirectional circular pattern feature. |
| Property | VarySketch | Gets or sets whether to allow pattern instances of a seed sketch to vary in relation to the base part in this circular pattern. |

[Top](#topBookmark)

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
