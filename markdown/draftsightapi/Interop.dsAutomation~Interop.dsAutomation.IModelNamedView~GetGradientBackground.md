---
title: "GetGradientBackground Method (IModelNamedView)"
project: ""
interface: "IModelNamedView"
member: "GetGradientBackground"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~GetGradientBackground.html"
---

# GetGradientBackground Method (IModelNamedView)

Gets the gradient background for the model named view.

## Syntax

### Visual Basic

```vb
Function GetGradientBackground() As GradientBackground
```

### C#

```csharp
GradientBackground GetGradientBackground()
```

### JScript

```
function GetGradientBackground() : GradientBackground;
```

### Managed Extensions for C++

```
GradientBackground* GetGradientBackground();
```

### C++/CLI

```cpp
GradientBackground^ GetGradientBackground();
```

### Return Value

[Gradient background](Interop.dsAutomation~Interop.dsAutomation.IGradientBackground.html)

## Remarks

Before calling this method, call [IModelNamedView::GetBackgroundType](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~GetBackgroundType.html) to see if the background type is set to [dsViewBackgroundType_e](Interop.dsAutomation~Interop.dsAutomation.dsViewBackgroundType_e.html).dsViewBackgroundTypeGradient. If the background type is [set](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~SetGradientBackground.html) to a different type of background, then this method returns null or nothing.

## See Also

[IModelNamedView Interface](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView.html)
[IModelNamedView Members](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView_members.html)
[IViewManager::CreateGradientBackground Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewManager~CreateGradientBackground.html)
[IModelNamedView::RemoveBackground Method ()](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~RemoveBackground.html)

## Availability

DraftSight V1R5.0
