---
title: "IBlockInstance Interface Members"
project: ""
interface: "IBlockInstance_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockInstance_members.html"
---

# IBlockInstance Interface Members

The following tables list the members exposed by [IBlockInstance](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Color | Gets or sets the LineColor of this Block instance. |
| Property | Erased | Gets or sets whether to erase or restore the Block instance. |
| Property | Handle | Gets the value of the handle for the Block instance. |
| Property | IsDynamicBlock | Gets whether this is a dynamic block instance. |
| Property | Layer | Gets or sets the name of the Layer of the Block instance. |
| Property | LineScale | Gets or sets the scale factor for the Block instance's LineStyle . |
| Property | LineStyle | Gets or sets the name of the LineStyle for the Block instance. |
| Property | LineWeight | Gets or sets the LineWeight for the BlockAttribute. |
| Property | PrintStyle | Gets or sets the name of the PrintStyle for this Block instance. |
| Property | Rotation | Gets or sets the angle by which to rotate the Block instance. |
| Property | Transparency | Gets or sets the transparency object for this Block instance. |
| Property | Visible | Gets or sets whether to show the Block instance in the drawing. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ConvertToStaticBlock | Converts this dynamic block instance to a static block instance. |
| Method | CreateExtensionDictionary | Creates a dictionary for the Block instance. |
| Method | DeleteCustomData | Deletes the specified custom data for the Block instance. |
| Method | DeleteHyperLink | Deletes the hyperlink attached to the Block instance. |
| Method | Explode | Explodes the Block instance. |
| Method | GetAttributeInstances | Gets the BlockAttribute instances for the Block instance. |
| Method | GetBlockDefinition | Gets the Block definition for the Block instance. |
| Method | GetBoundingBox | Gets the bounding box enclosing the Block instance. |
| Method | GetCustomData | Gets the specified custom data for the Block instance. |
| Method | GetDynamicBlockProperties | Gets the dynamic block instance property objects of this dynamic block instance. |
| Method | GetExtensionDictionary | Gets the dictionary for the Block instance. |
| Method | GetHyperLink | Gets the hyperlink attached to the Block instance. |
| Method | GetID | Gets the ID of the Block instance. |
| Method | GetNormal | Gets the vector normal to this Block instance. |
| Method | GetPosition | Gets the insertion point of the Block instance. |
| Method | GetScales | Gets the scale factors for the x, y, and z coordinates of the Block instance. |
| Method | GetWorkingSpace | Gets the type of working space and the working space object. |
| Method | ReleaseExtensionDictionary | Releases and erases the dictionary for the Block instance, if the dictionary exists and is empty. |
| Method | ResetBlock | Resets this block instance. |
| Method | Select | Adds or removes the selected Block instance to or from the current selection set. |
| Method | SetCustomData | Sets the custom data for the Block instance. |
| Method | SetHyperLink | Attaches a hyperlink to the Block instance. |
| Method | SetNormal | Sets the vector normal to this Block instance. |
| Method | SetPosition | Sets the insertion point of the Block instance. |
| Method | SetScales | Sets the scale factors for the x, y, and z coordinates of the Block instance. |

[Top](#topBookmark)

## See Also

[IBlockInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IBlockDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)
[IAttributeInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance.html)
[IDrawingSupportFiles::LibraryFilesPath Property ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles~LibraryFilesPath.html)
