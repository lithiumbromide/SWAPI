---
title: "GetSolidBackground Method (IModelNamedView)"
project: ""
interface: "IModelNamedView"
member: "GetSolidBackground"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~GetSolidBackground.html"
---

# GetSolidBackground Method (IModelNamedView)

Gets the solid background of the model named view.

## Syntax

### Visual Basic

```vb
Function GetSolidBackground() As SolidBackground
```

### C#

```csharp
SolidBackground GetSolidBackground()
```

### JScript

```
function GetSolidBackground() : SolidBackground;
```

### Managed Extensions for C++

```
SolidBackground* GetSolidBackground();
```

### C++/CLI

```cpp
SolidBackground^ GetSolidBackground();
```

### Return Value

[Solid background](Interop.dsAutomation~Interop.dsAutomation.ISolidBackground.html)

## Remarks

Before calling this method, call [IModelNamedView::GetBackgroundType](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~GetBackgroundType.html) to see if the background type is set to [dsViewBackgroundType_e](Interop.dsAutomation~Interop.dsAutomation.dsViewBackgroundType_e.html).dsViewBackgroundTypeSolid. If the background type is [set](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~SetSolidBackground.html) to a different type of background, then this method returns null or nothing.

## See Also

[IModelNamedView Interface](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView.html)
[IModelNamedView Members](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView_members.html)
[IViewManager::CreateSolidBackground Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewManager~CreateSolidBackground.html)
[IModelNamedView::RemoveBackground Method ()](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~RemoveBackground.html)

## Availability

DraftSight V1R5.0
