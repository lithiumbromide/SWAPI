---
title: "CreateImageBackground Method (IViewManager)"
project: ""
interface: "IViewManager"
member: "CreateImageBackground"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewManager~CreateImageBackground.html"
---

# CreateImageBackground Method (IViewManager)

Creates an image background using the specified image.

## Syntax

### Visual Basic

```vb
Function CreateImageBackground( _
   ByVal FileName As System.String, _
   ByVal Position As dsImageBackgroundPosition_e, _
   ByVal OffsetX As System.Double, _
   ByVal OffsetY As System.Double, _
   ByVal ScaleX As System.Double, _
   ByVal ScaleY As System.Double _
) As ImageBackground
```

### C#

```csharp
ImageBackground CreateImageBackground(
   System.string FileName,
   dsImageBackgroundPosition_e Position,
   System.double OffsetX,
   System.double OffsetY,
   System.double ScaleX,
   System.double ScaleY
)
```

### JScript

```
function CreateImageBackground(
   FileName : System.String,
   Position : dsImageBackgroundPosition_e,
   OffsetX : System.double,
   OffsetY : System.double,
   ScaleX : System.double,
   ScaleY : System.double
) : ImageBackground;
```

### Managed Extensions for C++

```
ImageBackground* CreateImageBackground(
   System.string* FileName,
   dsImageBackgroundPosition_e Position,
   System.double OffsetX,
   System.double OffsetY,
   System.double ScaleX,
   System.double ScaleY
)
```

### C++/CLI

```cpp
ImageBackground^ CreateImageBackground(
   System.String^ FileName,
   dsImageBackgroundPosition_e Position,
   System.double OffsetX,
   System.double OffsetY,
   System.double ScaleX,
   System.double ScaleY
)
```

### Parameters

- `FileName`: Path and file name of image
- `Position`: Position of image as defined in [dsImageBackgroundPosition_e](Interop.dsAutomation~Interop.dsAutomation.dsImageBackgroundPosition_e.html)
- `OffsetX`: x offset of the image
- `OffsetY`: y offset of the image
- `ScaleX`: x scale of the image
- `ScaleY`: y scale of the image

### Return Value

[Image background](Interop.dsAutomation~Interop.dsAutomation.IImageBackground.html)

## Examples

[Create Model and Sheet Views (C#)](Create_Model_and_Sheet_Views_Example_CSharp.htm)
[Create Model and Sheet Views (VB.NET)](Create_Model_and_Sheet_Views_Example_VBNET.htm)
[Create Model and Sheet Views (VBA)](Create_Model_and_Sheet_Views_Example_VBA.htm)

## Remarks

If Position is set to dsImageBackgroundPosition_e.dsImageBackgroundPosition_Stretch, then the values specified for the OffsetX, OffsetY, ScaleX, and ScaleY parameters are ignored.

## See Also

[IViewManager Interface](Interop.dsAutomation~Interop.dsAutomation.IViewManager.html)
[IViewManager Members](Interop.dsAutomation~Interop.dsAutomation.IViewManager_members.html)
[IModelNamedView::GetImageBackground Method ()](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~GetImageBackground.html)
[IModelNamedView::SetImageBackground Method ()](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~SetImageBackground.html)

## Availability

DraftSight V1R5.0
