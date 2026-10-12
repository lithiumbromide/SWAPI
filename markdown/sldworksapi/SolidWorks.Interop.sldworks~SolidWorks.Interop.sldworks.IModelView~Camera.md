---
title: "Camera Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "Camera"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Camera.html"
---

# Camera Property (IModelView)

Gets or sets the camera.

## Syntax

### Visual Basic (Declaration)

```vb
Property Camera As Camera
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As Camera

instance.Camera = value

value = instance.Camera
```

### C#

```csharp
Camera Camera {get; set;}
```

### C++/CLI

```cpp
property Camera^ Camera {
   Camera^ get();
   void set (    Camera^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Camera](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICamera.html)

## VBA Syntax

See [ModelView::Camera](ms-its:sldworksapivb6.chm::/sldworks~ModelView~Camera.html).

## Examples

[Turn Cameras On and Off (VBA)](Turn_Cameras_On_and_Off_Example_VB.htm)

## Remarks

If the return value is Nothing or NULL, then the camera view for this model is turned off.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::SetCameraByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SetCameraByName.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
