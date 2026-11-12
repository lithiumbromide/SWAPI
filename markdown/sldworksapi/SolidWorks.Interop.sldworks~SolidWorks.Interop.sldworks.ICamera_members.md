---
title: "ICamera Interface Members"
project: "SOLIDWORKS API Help"
interface: "ICamera_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html"
---

# ICamera Interface Members

The following tables list the members exposed by [ICamera](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AspectRatio | Gets the aspect ratio (width/height) of the field of view rectangle for the camera. NOTE: This property is a get-only property. Set is not implemented . |
| Property | DepthOfFieldEnabled | Gets whether depth of field effects are enabled or disabled. NOTE: This property is a get-only property. Set is not implemented . |
| Property | DepthOfFieldOffset | Gets the approximate distance from the camera's focal plane to point where focus is lost. NOTE: This property is a get-only property. Set is not implemented . |
| Property | FieldOfViewAngle | Gets the camera's horizontal angle of the field of view. NOTE: This property is a get-only property. Set is not implemented . |
| Property | FieldOfViewDepth | Gets the camera's depth of the field of view. NOTE: This property is a get-only property. Set is not implemented . |
| Property | FieldOfViewHeight | Gets the camera's height of the field of view. NOTE: This property is a get-only property. Set is not implemented . |
| Property | ID | Gets the ID for this camera. |
| Property | LockCameraPosition | Gets or sets whether the camera position is locked. |
| Property | Perspective | Gets whether the camera is in perspective mode or not. NOTE: This property is a get-only property. Set is not implemented . |
| Property | Pitch | Gets or sets the pitch (up or down angle) of a floating camera . |
| Property | PositionType | Gets or sets the camera position type. |
| Property | RotationRollAngle | Gets or sets the camera's roll angle. |
| Property | RotationRollBySelection | Gets or sets whether you can select the camera's rotation roll direction. |
| Property | RotationRollEntity | Gets or sets the entity (line, edge, face, or plane) that defines the camera's rotation up direction. |
| Property | RotationRollFlipDirection | Gets or sets whether to flip the direction of the camera 180 . |
| Property | TargetPointBySelection | Gets or sets whether you can set the target point. |
| Property | TargetPointPosition | Gets or sets the position of the target point. |
| Property | Type | Gets or sets the type of camera. |
| Property | Yaw | Gets or sets the yaw (side-to-side angle) of a floating camera . |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetFocalDistance | Gets the camera's focal distance. |
| Method | GetPointOfInterestDistance | Gets the distance of the point of interest from the camera. |
| Method | GetPosition | Gets the current position of the camera. |
| Method | GetPositionCartesian | Gets the Cartesian coordinates for the camera position. |
| Method | GetPositionEntity | Gets the entity to which the camera is attached. |
| Method | GetPositionSpherical | Gets the spherical coordinates for the camera position relative to the target, based on a sphere around the Z axis with the zero (0) point at the target. |
| Method | GetTargetPointEntity | Gets the target point on the entity for the camera. |
| Method | GetUpVector | Gets the camera's up direction. |
| Method | GetViewVector | Gets the direction in which the camera is looking. |
| Method | SetPositionCartesian | Sets the Cartesian coordinates for the camera position. |
| Method | SetPositionEntity | Sets the entity to which the camera is attached. |
| Method | SetPositionSpherical | Sets the spherical coordinates for the camera position relative to the target, based on a sphere around the Z axis with the zero (0) point at the target. |
| Method | SetTargetPointEntity | Gets the target point on the entity for the camera. |

[Top](#topBookmark)

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
