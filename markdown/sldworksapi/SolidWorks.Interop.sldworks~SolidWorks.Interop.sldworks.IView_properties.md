---
title: "IView Interface Properties"
project: "SOLIDWORKS API Help"
interface: "IView_properties"
member: ""
kind: "properties"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_properties.html"
---

# IView Interface Properties

For a list of all members of this type, see [IView members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Angle | Gets or sets the rotation angle of the view. |
| Property | Bodies | Gets or sets the bodies of a multibody part to show in the drawing view. |
| Property | BreakLineGap | Gets or sets the width of the gap for a break line. |
| Property | CropViewJaggedOutline | Gets or sets whether to use a jagged outline in this cropped drawing view. |
| Property | CropViewJaggedShapeIntensity | Gets or sets the shape intensity of the jagged outline in this cropped drawing view. |
| Property | CropViewNoOutline | Gets or sets whether to show an outline in this cropped drawing view. |
| Property | DisableAutoUpdate | Gets or sets whether to disable the automatic update of this view. |
| Property | DisplayState | Gets or sets the name of the display state for this drawing view. |
| Property | EmphasizeOutline | Gets or sets whether the outlines of section views are emphasized in this drawing view. |
| Property | FlipView | Gets or sets whether to flip a flat-pattern view of a sheet metal part. |
| Property | FocusLocked | Gets or sets whether or not focus is locked on this view. |
| Property | HiddenEdges | Gets the hidden edges in the drawing view or sets the hidden edges in the drawing view to be visible. |
| Property | IPosition | Gets or sets t he X and Y location of the model view's geometric center, relative to the drawing sheet origin. |
| Property | IScaleRatio | Gets or sets the scale of the drawing view, returning the results in ratio format (n:n). |
| Property | LinkParentConfiguration | Gets or sets whether to link a projected or auxiliary view with the parent configuration. |
| Property | ModelToViewTransform | Gets the math transform to go from model to drawing view space. NOTE: This property is a get-only property. Set is not implemented . |
| Property | Name | Obsolete. Superseded by IView::GetName2 and IView::SetName2 . |
| Property | Position | Gets or sets t he X and Y location of the model view's geometric center, relative to the drawing sheet origin. |
| Property | PositionLocked | Gets or sets whether this drawing view's position is locked. |
| Property | ProjectedDimensions | Gets or sets whether dimensions in this view are true or projected. |
| Property | ReferencedConfiguration | Gets or sets the configuration referenced by this drawing view. |
| Property | ReferencedConfigurationID | Gets the persistent reference ID of the configuration referenced in this drawing view. |
| Property | ReferencedDocument | Gets the document referenced by this drawing view. |
| Property | RootDrawingComponent | Obsolete. Superseded by IView::RootDrawingComponent2 . |
| Property | RootDrawingComponent2 | Gets the root component of this drawing view. |
| Property | ScaleDecimal | Gets or sets the scale of the drawing view, returning the results in decimal format. |
| Property | ScaleHatchPattern | Gets or sets whether to scale the hatch pattern to the drawing view. |
| Property | ScaleRatio | Gets or sets the scale of the drawing view, returning the results in ratio format (n:n). |
| Property | Sheet | Gets the sheet on which this drawing view exists. |
| Property | ShowSheetMetalBendNotes | Gets or sets whether to show sheet metal bend notes. |
| Property | SuppressState | Gets or sets the view suppress state. |
| Property | Type | Gets the drawing view type. |
| Property | UseParentScale | Gets or sets the drawing view's scale to match the parent drawing view's scale. |
| Property | UseSheetScale | Gets or sets whether the scale of the drawing view is the same as the scale of the drawing sheet on which this view is located. |

[Top](#topBookmark)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
