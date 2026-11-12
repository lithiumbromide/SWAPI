---
title: "SetCameraByName Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "SetCameraByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SetCameraByName.html"
---

# SetCameraByName Method (IModelView)

Sets the model view to that of the specified camera, if in camera view mode.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCameraByName( _
   ByVal Name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim Name As System.String
Dim value As System.Boolean

value = instance.SetCameraByName(Name)
```

### C#

```csharp
System.bool SetCameraByName(
   System.string Name
)
```

### C++/CLI

```cpp
System.bool SetCameraByName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Feature name of the camera to use to set the model view, if in camera view mode

### Return Value

True if the camera is set, false if not

## VBA Syntax

See [ModelView::SetCameraByName](ms-its:sldworksapivb6.chm::/sldworks~ModelView~SetCameraByName.html).

## Examples

[Turn Cameras On and Off (VBA)](Turn_Cameras_On_and_Off_Example_VB.htm)

## Remarks

| If you specify ... | Then... |
| --- | --- |
| A nonexistent camera when another camera view is active | Return value is false and the other camera view remains active |
| An empty string when another camera view is active | Return value is True and the camera view is turned off for this model view |

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::Camera Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Camera.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
