---
title: "IGeneralDimension Interface Members"
project: ""
interface: "IGeneralDimension_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension_members.html"
---

# IGeneralDimension Interface Members

The following tables list the members exposed by [IGeneralDimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Color | Gets or sets the TextColor of the Dimension. |
| Property | DimensionStyle | Gets or sets the name of the DimensionStyle of the Dimension. |
| Property | Elevation | Gets or sets the elevation of this Dimension. |
| Property | Erased | Gets or sets whether to erase or restore the Dimension. |
| Property | Handle | Gets the value of the handle for the Dimension. |
| Property | Layer | Gets or sets the name of the Layer of the Dimension. |
| Property | LineScale | Gets or sets the scale factor for the Dimension's LineStyle . |
| Property | LineStyle | Gets or sets the name of the LineStyle for the Dimension. |
| Property | LineWeight | Gets or sets the LineWeight for the Dimension. |
| Property | Measurement | Gets or sets the Dimension measurement. |
| Property | PrintStyle | Gets or sets the name of the PrintStyle for this Dimension. |
| Property | Related | Gets whether the Dimension is related to an entity. |
| Property | TextOverride | Gets or sets the text with which to override the Dimension text. |
| Property | TextRotation | Gets or sets the angle with which to rotate the Dimension text. |
| Property | Transparency | Gets or sets the transparency object for this Dimension. |
| Property | Visible | Gets or sets whether to show the Dimension in the drawing. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | CreateExtensionDictionary | Creates a dictionary for the Dimension. |
| Method | DeleteCustomData | Deletes the specified custom data from the Dimension. |
| Method | DeleteHyperLink | Deletes the hyperlink attached to the Dimension. |
| Method | DropRelated | Removes the relationship between the entity and a Dimension. |
| Method | GetBoundingBox | Gets the bounding box enclosing the Dimension. |
| Method | GetCustomData | Gets the specified custom data for the Dimension. |
| Method | GetDimensionStyleData | Gets the DimensionStyle of the Dimension. |
| Method | GetDimensionStyleUserData | Gets the DimensionStyle user data, including overrides, of the Dimension. |
| Method | GetExtensionDictionary | Gets the dictionary for the Dimension. |
| Method | GetHyperLink | Gets the hyperlink attached to the Dimension. |
| Method | GetNormal | Gets the vector normal to this Dimension. |
| Method | GetTextPosition | Gets the position of the Dimension. |
| Method | IsUseDefaultPosition | Gets or sets whether the text of this Dimension uses the default position. |
| Method | ReleaseExtensionDictionary | Releases and erases the dictionary for the Dimension, if the dictionary exists and is empty. |
| Method | Select | Adds or removes the selected Dimension to or from the current selection set. |
| Method | SetCustomData | Sets the custom data for the Dimension. |
| Method | SetHyperLink | Attaches the hyperlink to the Dimension. |
| Method | SetNormal | Sets the vector normal to this Dimension. |
| Method | SetTextPosition | Sets the position of the Dimension. |
| Method | SetUseDefaultPosition | Sets the text of this Dimension to use the default position. |

[Top](#topBookmark)

## See Also

[IGeneralDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
