---
title: "GetCameraById Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetCameraById"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCameraById.html"
---

# GetCameraById Method (IModelDocExtension)

Gets a camera using the specified camera ID.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCameraById( _
   ByVal CameraId As System.Integer _
) As Camera
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim CameraId As System.Integer
Dim value As Camera

value = instance.GetCameraById(CameraId)
```

### C#

```csharp
Camera GetCameraById(
   System.int CameraId
)
```

### C++/CLI

```cpp
Camera^ GetCameraById(
   System.int CameraId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CameraId`: Camera ID (see **Remarks**)

### Return Value

[Camera](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICamera.html)

## VBA Syntax

See [ModelDocExtension::GetCameraById](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetCameraById.html).

## Examples

[Turn Cameras On and Off (VBA)](Turn_Cameras_On_and_Off_Example_VB.htm)

## Remarks

A valid ID is 0 <= ID <= ([IModelDocExtension::GetCameraCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetCameraCount.html) -1).

CameraId is reassigned if there are multiple cameras and one of those cameras is deleted. For example:

| If... | And Camera2 is deleted, then... |
| --- | --- |
| CameraId = 1 for Camera1 | CameraId = 1 for Camera1 |
| CameraId = 2 for Camera2 | Deleted |
| CameraId = 3 for Camera3 | CameraId = 2 for Camera3 |

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[ICamera::GetCameraDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCameraDefinition.html)
[IModelDocExtension::InsertCamera Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertCamera.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
