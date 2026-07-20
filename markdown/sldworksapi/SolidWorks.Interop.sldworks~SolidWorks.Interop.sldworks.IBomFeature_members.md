---
title: "IBomFeature Interface Members"
project: "SOLIDWORKS API Help"
interface: "IBomFeature_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html"
---

# IBomFeature Interface Members

The following tables list the members exposed by[IBomFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Configuration | Gets or sets the name of configuration for this BOM table. |
| Property | DetailedCutList | Gets or sets whether to show the detailed cut list in this BOM table. |
| Property | DisplayAsOneItem | Gets or sets whether all of the configurations appear with the same item number if the BOM table contains components that have multiple configurations. |
| Property | DissolvePartLevelRows | Gets or sets whether to dissolve weldment part level rows. |
| Property | FollowAssemblyOrder2 | Gets or sets whether the order of the item numbers in the BOM follows the order in which the assembly appears in the FeatureManager design tree. |
| Property | KeepCurrentItemNumbers | Gets or sets whether item numbers are kept with their components when reordering rows of a BOM table. |
| Property | KeepMissingItems | Gets and sets the Keep Missing Items option for this BOM feature. |
| Property | KeepReplacedCompOption | Gets or sets how to replace components when keeping missing items. |
| Property | Name | Gets the name of this BOM table feature. |
| Property | NumberingTypeOnIndentedBOM | Gets and sets the type of numbering for this indented BOM table. |
| Property | PartConfigurationGrouping | Gets and sets the part configuration grouping for this BOM table. |
| Property | RoutingComponentGrouping | Gets or sets the routing component grouping options for this BOM table in a drawing of an assembly containing routing components. |
| Property | SequenceStartNumber | Gets or sets the number with which to start the numbering for this BOM table. |
| Property | StrikeoutMissingItems | Inserts a horizontal line through missing items in this BOM table (also called strike outs). |
| Property | TableType | Gets and sets the type of table for the Bill of Materials. |
| Property | ZeroQuantityDisplay | Gets or sets the character or value to display when a value is 0 in this BOM table. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | FollowAssemblyOrder | Obsolete. Superseded by IBomFeature::FollowAssemblyOrder2 . |
| Method | GetConfigurationCount | Gets the number of configurations available to this BOM table or used in this BOM table. |
| Method | GetConfigurations | Gets the configurations available to this BOM table or used in this BOM table. |
| Method | GetFeature | Gets the BOM table feature. |
| Method | GetLinkToDisplayState | Gets the name of the Display State linked to this BOM feature. |
| Method | GetReferencedModelName | Gets the name of the model referenced by this BOM feature. |
| Method | GetTableAnnotationCount | Gets the number of BOM table annotations for this BOM table feature. |
| Method | GetTableAnnotations | Gets the BOM table annotations for this BOM table feature. |
| Method | IGetConfigurations | Gets the configurations available to this BOM table or used in this BOM table. |
| Method | IGetTableAnnotations | Gets the BOM table annotations for this BOM table feature. |
| Method | ISetConfigurations | Sets the configurations used in this BOM table. |
| Method | SetConfigurations | Sets the configurations used in this BOM table. |
| Method | SetLinkToDisplayState | Sets the name of the Display State to which to link this BOM feature. |

[Top](#topBookmark)

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
