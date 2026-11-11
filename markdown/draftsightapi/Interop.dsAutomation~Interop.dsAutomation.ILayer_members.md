---
title: "ILayer Interface Members"
project: ""
interface: "ILayer_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html"
---

# ILayer Interface Members

The following tables list the members exposed by [ILayer](Interop.dsAutomation~Interop.dsAutomation.ILayer.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Color | Gets or sets the LineColor of this Layer. |
| Property | Description | Gets or sets a description for the Layer. |
| Property | Frozen | Gets or sets whether the Layer is frozen or thawed. |
| Property | FrozenInNewViewport | Gets or sets whether this Layer is frozen or thawed in newly created Viewports . |
| Property | Handle | Gets the value of the handle for the Layer. |
| Property | LineStyle | Gets or sets the name of the LineStyle for the Layer. |
| Property | LineWeight | Gets or sets the LineWeight for the Layer. |
| Property | Locked | Gets or sets whether the Layer is locked. |
| Property | Name | Gets the name of the Layer. |
| Property | Printable | Gets or sets whether the Layer can be printed. |
| Property | PrintStyle | Gets or sets the PrintStyle for the Layer. |
| Property | Shown | Gets or sets whether the Layer is shown or hidden. |
| Property | Transparency | Gets or sets the transparency percentage for this Layer. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | Activate | Activates this Layer. |
| Method | CreateExtensionDictionary | Creates a dictionary for the Layer. |
| Method | DeleteCustomData | Deletes the specified custom da ta from the Layer. |
| Method | GetColorInViewport | Gets the LineColor for the Layer in the specified Viewport and whether the LineColor is overridden in the that Viewport. |
| Method | GetCustomData | Gets the specified custom data for the Layer. |
| Method | GetExtensionDictionary | Gets the dictionary for the Layer. |
| Method | GetFrozenInViewport | Gets whether this Layer is frozen or thawed in the specified Viewport. |
| Method | GetLineSyleInViewport | Gets the name of the LineStyle for this Layer in the specified Viewport and whether the LineStyle is overridden in that Viewport. |
| Method | GetLineWeightInViewport | Gets the type of LineWeight for this Layer in the specified Viewport and whether the LineWeight is overridden in that Viewport. |
| Method | GetPrintStyleInViewport | Gets the name of the PrintStyle for this Layer in the specified Viewport and whether the PrintStyle is overridden in that Viewport. |
| Method | GetTranparencyInViewport | Gets the transparency percentage for this Layer in the specified Viewport and gets whether the transparency in this Layer is overridden in that Viewport. |
| Method | ReleaseExtensionDictionary | Releases and erases the dictionary for the Layer, if the dictionary exists and is empty. |
| Method | RemoveColorOverride | Removes the LineColor override from this Layer in the specified Viewport. |
| Method | RemoveColorOverrides | Removes the LineColor override from this Layer in all Viewports . |
| Method | RemoveLineStyleOverride | Removes the LineStyle override from this Layer in the specified Viewport. |
| Method | RemoveLineStyleOverrides | Removes the LineStyle override from this Layer in all Viewports . |
| Method | RemoveLineWeightOverride | Removes the LineWeight override from this Layer in the specified Viewport. |
| Method | RemoveLineWeightOverrides | Removes the LineWeight override for this Layer in all Viewports . |
| Method | RemovePrintStyleOverride | Removes the PrintStyle override from this Layer in the specified Viewport. |
| Method | RemovePrintStyleOverrides | Removes the PrintStyle override from this Layer in all Viewports . |
| Method | RemoveTransparencyOverride | Removes the transparency override from this Layer in the specified Viewport. |
| Method | RemoveTransparencyOverrides | Removes the transparency override from this layer in all Viewports . |
| Method | Rename | Renames the Layer. |
| Method | SetColorInViewport | Sets the LineColor of this Layer in the specified Viewport. |
| Method | SetCustomData | Sets the custom data for the Layer. |
| Method | SetFrozenInViewport | Sets whether this Layer is frozen or thawed in the specified Viewport. |
| Method | SetLineStyleInViewport | Sets the name of the LineStyle for this Layer in the specified Viewport. |
| Method | SetLineWeightInViewport | Sets the type of LineWeight for this Layer in the specified Viewport. |
| Method | SetPrintStyleInViewport | Sets the name of the PrintStyle for this Layer in the specified Viewport. |
| Method | SetTranparencyInViewport | Sets the transparency percentage for this Layer in the specified Viewport. |

[Top](#topBookmark)

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[ILayerManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerManager.html)
