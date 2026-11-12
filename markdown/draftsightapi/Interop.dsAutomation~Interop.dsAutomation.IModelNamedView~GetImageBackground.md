---
title: "GetImageBackground Method (IModelNamedView)"
project: ""
interface: "IModelNamedView"
member: "GetImageBackground"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~GetImageBackground.html"
---

# GetImageBackground Method (IModelNamedView)

Gets the image background for the model named view.

## Syntax

### Visual Basic

```vb
Function GetImageBackground() As ImageBackground
```

### C#

```csharp
ImageBackground GetImageBackground()
```

### JScript

```
function GetImageBackground() : ImageBackground;
```

### Managed Extensions for C++

```
ImageBackground* GetImageBackground();
```

### C++/CLI

```cpp
ImageBackground^ GetImageBackground();
```

### Return Value

[Image background](Interop.dsAutomation~Interop.dsAutomation.IImageBackground.html)

## Remarks

Before calling this method, call [IModelNamedView::GetBackgroundType](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~GetBackgroundType.html) to see if the background type is set to [dsViewBackgroundType_e](Interop.dsAutomation~Interop.dsAutomation.dsViewBackgroundType_e.html).dsViewBackgroundTypeImage. If the background type is [set](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~SetImageBackground.html) to a different type of background, then this method returns null or nothing.

## See Also

[IModelNamedView Interface](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView.html)
[IModelNamedView Members](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView_members.html)
[IViewManager::CreateImageBackground Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewManager~CreateImageBackground.html)
[IModelNamedView::RemoveBackground Method ()](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~RemoveBackground.html)

## Availability

DraftSight V1R5.0
