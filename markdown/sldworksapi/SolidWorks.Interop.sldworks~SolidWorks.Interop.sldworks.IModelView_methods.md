---
title: "IModelView Interface Methods"
project: "SOLIDWORKS API Help"
interface: "IModelView_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_methods.html"
---

# IModelView Interface Methods

For a list of all members of this type, see [IModelView members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html).

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
