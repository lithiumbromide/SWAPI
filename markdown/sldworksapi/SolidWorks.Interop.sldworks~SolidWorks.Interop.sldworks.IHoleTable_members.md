---
title: "IHoleTable Interface Members"
project: "SOLIDWORKS API Help"
interface: "IHoleTable_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html"
---

# IHoleTable Interface Members

The following tables list the members exposed by [IHoleTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CombineSameSize | Gets or sets whether to merge cells of the same size in this hole table. |
| Property | CombineTags | Gets or sets whether to combine tags for same-size holes. |
| Property | DatumOrigin | Gets the datum origin annotation for this hole table. |
| Property | EnableUpdate | Gets or sets whether to update hole table and graphics after changing hole tags . |
| Property | HoleCentersVisible | Gets or sets whether to show the hole center marks for this hole table. |
| Property | HoleTag | Gets or sets the name of the specified tag in a hole table. |
| Property | HoleTagsVisible | Gets whether the hole tags are visible for this hole table. |
| Property | ShowANSIInchLetterNumberDrillSizes | Gets or sets whether to display hole sizes in this hole table using ANSI inch letters and drill numbers. |
| Property | StartingValue | Gets or sets the starting value for the datum tags of this hole table. |
| Property | TagStyle | Gets or sets the tag style for this hole table. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddHole | Adds holes to this hole table. |
| Method | AssignTagPrefix | Prefixes the manual datum tags of specified holes with specified text. |
| Method | GetFeature | Gets the IFeature object for this hole table. |
| Method | GetHoleLocationPrecision | Gets the precision to use for location values for this hole table. |
| Method | GetHoleLocationUseDocPrecision | Gets whether to display the location of this hole table using the document's location precision. |
| Method | GetTableAnnotationCount | Gets the number of hole table annotations for this hole table. |
| Method | GetTableAnnotations | Gets the hole table annotations for this hole table feature. |
| Method | IGetTableAnnotations | Gets the hole table annotations for this hole table feature. |
| Method | SetHoleLocationPrecision | Sets the precision to use for location values for this hole table. |

[Top](#topBookmark)

## See Also

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IHoleTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTableAnnotation.html)
[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
