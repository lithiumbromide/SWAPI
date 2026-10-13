---
title: "ITemplateOverrides Interface Members"
project: "SOLIDWORKS Costing API Help"
interface: "ITemplateOverrides_members"
member: ""
kind: "members"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_members.html"
---

# ITemplateOverrides Interface Members

The following tables list the members exposed by [ITemplateOverrides](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CustomBendCost | Gets or sets the custom cost per bend for sheet metal parts. |
| Property | CustomHemCost | Gets or sets the custom hem cost for sheet metal parts. |
| Property | CustomLibraryFeatureCost | Gets or sets the custom library feature cost for sheet metal parts. |
| Property | DefaultFinishingOperation | Gets or sets the default finishing operation for machined parts. |
| Property | DefaultMachiningOperationTool | Gets or sets the tool for the default machining operation for machined parts. |
| Property | FinishingCostPerVolume | Gets or sets the finishing cost per volume for machined parts. |
| Property | FinishingOffset | Gets or sets the finishing offset for machined parts. |
| Property | RemovedMaterialProcessingType | Gets or sets the removed material processing option for machined parts. |
| Property | RoughingCostPerVolume | Gets or sets the roughing cost per volume for machined parts. |
| Property | SemiFinishingCostPerVolume | Gets or sets the semi-finishing cost per volume for machined parts. |
| Property | SemiFinishingOffset | Gets or sets the semi-finishing offset for machined parts. |
| Property | ShowUndeterminedSlotsInNCAFolder | Gets or sets whether slot features whose volume cannot be determined are displayed as items in the No Cost Assigned folder. |
| Property | SlotFeatureRecognitionType | Gets or sets the slot feature recognition option for machined parts. |
| Property | UseCustomBendCost | Gets or sets whether to use a custom cost per bend for sheet metal parts. |
| Property | UseCustomHemCost | Gets or sets whether to use a custom hem cost for sheet metal parts. |
| Property | UseCustomLibraryFeatureCost | Gets or sets whether to use a custom library feature cost for sheet metal parts. |
| Property | UseOffsetBasedFinishing | Gets or sets the option to override template settings for offset-based finishing for machined parts. |
| Property | VolumeFeatureCalculationType | Gets or sets the volume feature calculation option for machined parts. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ApplyOverrides | Applies all overridden system-level options. |
| Method | ResetAll | Restores all overridden system-level options to their system-level settings and recalculates features and costs based on the system-level settings. |
| Method | SaveCostingOverrideSettings | Saves all overridden system-level settings to the registry. |

[Top](#topBookmark)

## See Also

[ITemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html)
[SolidWorks.Interop.sldcostingapi Namespace](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi_namespace.html)
