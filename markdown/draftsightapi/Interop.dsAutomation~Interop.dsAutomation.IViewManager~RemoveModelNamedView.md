---
title: "RemoveModelNamedView Method (IViewManager)"
project: ""
interface: "IViewManager"
member: "RemoveModelNamedView"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewManager~RemoveModelNamedView.html"
---

# RemoveModelNamedView Method (IViewManager)

Removes the specified model named view from the document.

## Syntax

### Visual Basic

```vb
Function RemoveModelNamedView( _
   ByVal NamedView As ModelNamedView _
) As System.Boolean
```

### C#

```csharp
System.bool RemoveModelNamedView(
   ModelNamedView NamedView
)
```

### JScript

```
function RemoveModelNamedView(
   NamedView : ModelNamedView
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool RemoveModelNamedView(
   ModelNamedView* NamedView
)
```

### C++/CLI

```cpp
System.bool RemoveModelNamedView(
   ModelNamedView^ NamedView
)
```

### Parameters

- `NamedView`: [Model named view](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView.html) to remove

### Return Value

True if the specified model name view is removed, false if not

## See Also

[IViewManager Interface](Interop.dsAutomation~Interop.dsAutomation.IViewManager.html)
[IViewManager Members](Interop.dsAutomation~Interop.dsAutomation.IViewManager_members.html)
[IViewManager::ActivateModelView Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewManager~ActivateModelView.html)
[IViewManager::CreateModelNamedView Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewManager~CreateModelNamedView.html)
[IViewManager::GetModelNamedView Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetModelNamedView.html)
[IViewManager::GetModelNamedViewList Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetModelNamedViewList.html)
[IViewManager::SaveCurrentViewAsModelView Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewManager~SaveCurrentViewAsModelView.html)

## Availability

DraftSight V1R5.0
