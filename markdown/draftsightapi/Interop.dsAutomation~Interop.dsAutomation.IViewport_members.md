---
title: "IViewport Interface Members"
project: ""
interface: "IViewport_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewport_members.html"
---

# IViewport Interface Members

The following tables list the members exposed by [IViewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Active | Gets or sets whether this Viewport is activated. |
| Property | CCSPerViewport | Gets or sets whether the custom coordinate system associated with this Viewport becomes active when the Viewport is activated . |
| Property | Color | Gets or sets the LineColor of the Viewport. |
| Property | CustomScale | Gets or sets a custom scale factor for the Viewport. |
| Property | DisplayLocked | Gets or sets whether the Viewport is locked in model workspace. |
| Property | Erased | Gets or sets whether to erase or restore the Viewport. |
| Property | Handle | Gets the value of the handle for the Viewport. |
| Property | Height | Gets or sets the height of this selected Viewport. |
| Property | IsOn | Gets or sets whether the Viewport is displayed in the graphics area. |
| Property | Layer | Gets or sets the name of the Layer of the Viewport. |
| Property | LineScale | Gets or sets the scale factor for the Viewport's LineStyle . |
| Property | LineStyle | Gets or sets the name of the LineStyle for the Viewport. |
| Property | LineWeight | Gets or sets the LineWeight of the Viewport. |
| Property | PrintStyle | Gets or sets the name of the PrintStyle for this Viewport. |
| Property | ShadePrintStyle | Gets or sets the shaded view print style of the Viewport. |
| Property | StandardScale | Gets or sets the standard scale factor for the Viewport. |
| Property | Transparency | Gets or sets the transparency object for this Viewport. |
| Property | ViewHeight | Gets the height of the view or perspective in this activated Viewport. |
| Property | Visible | Gets or sets whether to show the Viewport. |
| Property | Width | Gets or sets the width of this selected Viewport. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | CreateExtensionDictionary | Creates a dictionary for the Viewport. |
| Method | DeleteCustomData | Deletes the specified custom data from the Viewport. |
| Method | DeleteHyperLink | Deletes the hyperlink attached to the Viewport. |
| Method | GetBoundingBox | Gets the bounding box enclosing the Viewport. |
| Method | GetCenter | Gets the center coordinates of this selected Viewport. |
| Method | GetClippedObject | Gets the entity that defines the clipping boundary of the Viewport. |
| Method | GetCustomData | Gets the specified custom data for the Viewport. |
| Method | GetExtensionDictionary | Gets the dictionary for the Viewport. |
| Method | GetHyperLink | Gets the hyperlink attached to the Viewport. |
| Method | GetIsClipped | Gets whether the Viewport is clipped by an entity. |
| Method | GetViewCenter | Gets the center coordinates of the view or perspective in this activated Viewport. |
| Method | ReleaseExtensionDictionary | Releases and erases the dictionary for the Viewport, if the dictionary exists and is empty. |
| Method | Select | Adds or removes the selected Viewport to or from the current selection set. |
| Method | SetCenter | Sets the center coordinates of this selected Viewport. |
| Method | SetCustomData | Sets the custom data for the Viewport. |
| Method | SetHyperLink | Sets the hyperlink to attach to the Viewport. |

[Top](#topBookmark)

## See Also

[IViewport Interface](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IViewTile Interface](Interop.dsAutomation~Interop.dsAutomation.IViewTile.html)
