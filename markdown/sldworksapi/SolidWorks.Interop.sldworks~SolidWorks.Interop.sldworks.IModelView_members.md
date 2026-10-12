---
title: "IModelView Interface Members"
project: "SOLIDWORKS API Help"
interface: "IModelView_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html"
---

# IModelView Interface Members

The following tables list the members exposed by [IModelView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html).

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

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | Activate | Activates the model view. |
| Method | AddPerspective | Adds perspective to the model view. |
| Method | CreateCallout | Creates a callout on this model view. |
| Method | DrawHighlightedItems | Draws or redraws the highlighted items. |
| Method | DrawTransparentFeatureTree | Draws a transparent FeatureManager design tree. |
| Method | GetBkgdImageDisplayAreaAspectRatio | Gets the aspect ratio (width/height) of the area of the window where the background image is displayed. |
| Method | GetDisplayState | Gets the display state of this model view. |
| Method | GetEyePoint | Gets the eye position for perspective viewing. |
| Method | GetIsoPlaneDistance | Gets the distance, in terms of screen space, from the eye position to the plane at which there is no scaling due to perspective. |
| Method | GetMouse | Gets the mouse for this model view. |
| Method | GetNext | Gets the next model view after this model view. |
| Method | GetStereoSeparation | Obsolete and not superseded. Functionality no longer implemented. |
| Method | GetViewDIB | Obsolete. Superseded by IModelView::GetViewDIBx64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. Gets an image of the document as it looks in Normal view or in the print preview. |
| Method | GetViewDIBx64 | Gets an image of the document as it looks in Normal view or in the print preview in 64-bit applications. |
| Method | GetViewHWnd | Obsolete. Superseded by IModelView::GetViewHWndx64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. Gets the Microsoft window handle for this model view. |
| Method | GetViewHWndx64 | Gets the Microsoft window handle for this model view in 64-bit applications. |
| Method | GetViewPlaneDistance | Gets the model view plane distance for perspective viewing. |
| Method | GetVisibleBox | Gets the boundaries of the visible model view window. |
| Method | GraphicsRedraw | Redraws the specified region of or the entire SOLIDWORKS graphics window. |
| Method | HasPerspective | Determines if the model view currently has perspective. |
| Method | HideMagnifyingGlass | Hides the Magnifying Glass tool. |
| Method | IGetEyePoint | Gets the eye position for perspective viewing. |
| Method | IGetNext | Gets the next model view after this model view. |
| Method | IGetStereoSeparation | Obsolete and not superseded. Functionality no longer implemented. |
| Method | IGetVisibleBox | Gets the boundaries of the visible model view window. |
| Method | IGraphicsRedraw | Redraws the specified region of or the entire SOLIDWORKS graphics window. |
| Method | InitializeShading | Sets up the model view for OpenGL shading. |
| Method | ISetEyePoint | Sets the eye position for perspective viewing. |
| Method | ISetStereoSeparation | Obsolete and not superseded. Functionality no longer implemented. |
| Method | MoveMagnifyingGlass | Moves Magnifying Glass tool to the specified coordinates. |
| Method | RemovePerspective | Removes perspective from the model view. |
| Method | RollBy | Rolls the model view about the line of sight by the specified angle. |
| Method | RotateAboutAxis | Rotates the model view about a point, by an angle in the specified direction. |
| Method | RotateAboutCenter | Rotates the model view about the screen X and Y axes. |
| Method | RotateAboutPoint | Rotates the model view about the specified point by the specified angles in the directions of the screen X and Y axes. |
| Method | SetCameraByName | Sets the model view to that of the specified camera, if in camera view mode. |
| Method | SetEyePoint | Sets the eye position for perspective viewing. |
| Method | SetStereoSeparation | Obsolete and not superseded. Functionality no longer implemented. |
| Method | ShowMagnifyingGlass | Shows the Magnifying Glass tool at the specified coordinates. |
| Method | StartDynamics | Provides faster rotation of model views. |
| Method | StopDynamics | Ends dynamic model view motion. |
| Method | TranslateBy | Translates the model view in the screen. |
| Method | TurnBy | Rotates the camera by the specified angles about the camera's x and y axes. |
| Method | ZoomByFactor | Modifies the zoom factor for the model view. |

[Top](#topBookmark)

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelWindow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow.html)
