---
title: "SetStereoSeparation Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "SetStereoSeparation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SetStereoSeparation.html"
---

# SetStereoSeparation Method (IModelView)

Obsolete and not superseded. Functionality no longer implemented.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetStereoSeparation( _
   ByVal DfSeparation As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim DfSeparation As System.Object
Dim value As System.Boolean

value = instance.SetStereoSeparation(DfSeparation)
```

### C#

```csharp
System.bool SetStereoSeparation(
   System.object DfSeparation
)
```

### C++/CLI

```cpp
System.bool SetStereoSeparation(
   System.Object^ DfSeparation
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DfSeparation`: Array of 2 doubles representing the stereo magnitude and stereo parallax balance settings

### Return Value

True if changing the stereo-value settings is successful, false if not

## VBA Syntax

See [ModelView::SetStereoSeparation](ms-its:sldworksapivb6.chm::/sldworks~ModelView~SetStereoSeparation.html).

## Remarks

This method only affects the model view's display if:

- Display window was set up to display stereoscopically
- Application is currently set to display stereoscopically.

[ISldWorks::EnableStereoDisplay](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~EnableStereoDisplay.html) needs to be called to do these things.

There are two stereoscopic display values this method sets.

1. Settings[0] controls the magnitude of the stereoscopic effect by specifying the stereoscopic, virtual, camera separation. Appropriate values for this setting depend on the scale of the object, the distance from the virtual camera to the object center, the perspective field of view angle, and, perhaps, an adjustment factor that is available to the user.
2. Settings[1] controls the asymmetry of the projection frustums, thus, adjusting the parallax balance of the stereoscopic scene. It is desirable for any stereoscopic scene to comfortably balance the use of negative parallax (elements appearing to float in front of the display surface) and positive parallax (elements appearing to reside somewhere behind the display surface). Appropriate values for this setting should be arrived at experimentally.

If this method is not called, the default settings will equal 0.0, resulting in identical left-eye and right-eye renderings, and no visible stereo effect, even if stereoscopic display is currently enabled.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
