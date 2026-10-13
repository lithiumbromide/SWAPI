---
title: "IModelView Interface Properties"
project: "SOLIDWORKS API Help"
interface: "IModelView_properties"
member: ""
kind: "properties"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_properties.html"
---

# IModelView Interface Properties

For a list of all members of this type, see [IModelView members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Camera | Gets or sets the camera. |
| Property | DisplayMode | Gets or sets the display mode for this model view. |
| Property | DisplayZebraStripes | Gets or sets the zebra-line display state. |
| Property | DynamicMode | Gets the dynamic mode. |
| Property | EnableGraphicsUpdate | Gets or sets whether or not to refresh the model view. |
| Property | FrameHeight | Get or sets the height of the frame of the document window that contains the model view in the SOLIDWORKS client area. |
| Property | FrameLeft | Gets or sets the left position of the frame of the document window that contains the model view in the SOLIDWORKS client area. |
| Property | FrameState | Gets or sets the window state (minimum, maximum, or normal) for the frame of the document window that contains the model view in the SOLIDWORKS client area. |
| Property | FrameTop | Gets or sets the top position of the frame of the document window that contains the model view in the SOLIDWORKS client area. |
| Property | FrameWidth | Gets or sets the width of the frame of the document window that contains the model view in the SOLIDWORKS client area. |
| Property | HlrQuality | Gets or sets the hidden-line removal quality property of this model view. |
| Property | IOrientation | Obsolete. Superseded by IModelView::Orientation3 . |
| Property | IOrientation2 | Obsolete. Superseded by IModelView::Orientation3 . |
| Property | ITranslation | Obsolete. Superseded by IModelView::Translation3 . |
| Property | ITranslation2 | Obsolete. Superseded by IModelView::Translation3 . |
| Property | Linked | Gets whether or not this viewport is linked or not. |
| Property | ObjectSizesAway | Helps define the perspective of the current model view by relating the size of a displayed object with the distance of the object from the observer. |
| Property | Orientation | Obsolete. Superseded by IModelView::Orientation3 . |
| Property | Orientation2 | Obsolete. Superseded by IModelView::Orientation3 . |
| Property | Orientation3 | Gets or sets the model view orientation matrix. |
| Property | Scale | Obsolete. Superseded by IModelView::Scale2 . |
| Property | Scale2 | Gets and sets the model view scale factor. |
| Property | SuppressWaitCursorDuringRedraw | Gets or sets the state of the wait cursor (also called the hourglass) while this model view is being redrawn. |
| Property | Transform | Gets the model space to the model view plane transform. NOTE: This property is a get-only property. Set is not implemented . |
| Property | Translation | Obsolete. Superseded by IModelView::Translation3 . |
| Property | Translation2 | Obsolete. Superseded by IModelView::Translation3 . |
| Property | Translation3 | Gets or sets the model view translation vector. |
| Property | UpAxisFlyout | Gets or sets the up axis flyout flag. |
| Property | UpdateAllGraphicsLayers | Gets or sets whether to update all graphic layers in any mode. |
| Property | VisibilityViewTools | Gets or sets the visibility of the Heads-up View Toolbar for this model view. |
| Property | XorHighlight | Gets or sets the Xor highlight state. |

[Top](#topBookmark)

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelWindow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow.html)
