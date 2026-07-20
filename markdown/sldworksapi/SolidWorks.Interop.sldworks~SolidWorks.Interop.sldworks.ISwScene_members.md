---
title: "ISwScene Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISwScene_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html"
---

# ISwScene Interface Members

The following tables list the members exposed by[ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AccurateEnvLighting | Gets or sets whether to use the accurate environment lighting calculations from the high dynamic range imaging (HDRI) scene environment. |
| Property | AspectRatio | Gets the aspect ratio of the scene floor. |
| Property | BackgroundBottomGradientColor | Gets or sets the bottom color of the graduated range of background colors of this scene. |
| Property | BackgroundBrightness | Gets or sets the brightness of the background. |
| Property | BackgroundEnvImage | Gets or sets the environment image of this scene. |
| Property | BackgroundImage | Gets or sets the background image for this scene. |
| Property | BackgroundTopGradientColor | Gets or sets the background color of this scene. |
| Property | BackgroundType | Gets or sets the type of background for this scene. |
| Property | EnvironmentRotation | Gets or sets the rotation of the environment image of this scene. |
| Property | EnvironmentSize | Gets or sets the size of the high dynamic range imaging (HDRI) scene sphere that surrounds the model. |
| Property | FitToSWWindow | Gets or sets whether to stretch an image to fit the SOLIDWORKS window. |
| Property | FixedAspectRatio | Gets or sets whether to fix the aspect ratio of the scene floor. |
| Property | FlattenFloor | Get or sets whether to flatten the floor of a spherical environment to improve the look of models that naturally rest on flat floors. |
| Property | FloorAlignment | Gets or sets the plane with which to align the scene floor. |
| Property | FloorAutoSize | Gets or sets whether to resize the scene floor based on the model bounding box. |
| Property | FloorDepth | Gets or sets the depth of the scene floor. |
| Property | FloorDirection | Gets or sets whether to flip the direction of the floor of this scene. |
| Property | FloorOffset | Gets or sets the height of the model above or below the floor of this scene. |
| Property | FloorOffsetDirection | Gets or sets whether to swap the positions of the scene floor and the model. |
| Property | FloorReflections | Gets or sets whether to show reflections of the model on the scene floor. |
| Property | FloorRotation | Gets or sets the rotation of the scene floor relative to the environment of this scene. |
| Property | FloorSelection | Gets or sets the floor appearance of this scene. |
| Property | FloorShadows | Gets or sets whether to show shadows cast by the model on the scene floor. |
| Property | FloorWidth | Gets or sets the width of the scene floor. |
| Property | HorizonHeight | Gets or sets the height on the high dynamic range imaging (HDRI) scene sphere where the scene floor starts to flatten. |
| Property | KeepBackground | Gets or sets whether to retain the background when replacing the scene. |
| Property | RenderingBrightness | Gets or sets the brightness contributed by the high dynamic range imaging (HDRI) environment. |
| Property | SceneReflectivity | Gets or sets the amount of reflectivity provided by the high dynamic range imaging (HDRI) environment. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddOrEditFloorAppearance | Adds or modifies the floor appearance of this scene. |
| Method | DeleteFloorAppearance | Deletes the floor appearance of this scene. |
| Method | GetFloorAppearance | Gets the floor appearance of this scene. |
| Method | GetFloorNormal | Gets the normal to the floor of this scene. |
| Method | GetP2SFileName | Gets the scene file for this scene. |
| Method | Modify | Modifies and saves this scene. |
| Method | OffsetToGeometry | Resets the floor offset. |

[Top](#topBookmark)

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
