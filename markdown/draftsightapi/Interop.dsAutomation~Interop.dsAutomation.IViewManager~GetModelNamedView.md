---
title: "GetModelNamedView Method (IViewManager)"
project: ""
interface: "IViewManager"
member: "GetModelNamedView"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetModelNamedView.html"
---

# GetModelNamedView Method (IViewManager)

Gets the model view with the specified name.

## Syntax

### Visual Basic

```vb
Function GetModelNamedView( _
   ByVal Name As System.String _
) As ModelNamedView
```

### C#

```csharp
ModelNamedView GetModelNamedView(
   System.string Name
)
```

### JScript

```
function GetModelNamedView(
   Name : System.String
) : ModelNamedView;
```

### Managed Extensions for C++

```
ModelNamedView* GetModelNamedView(
   System.string* Name
)
```

### C++/CLI

```cpp
ModelNamedView^ GetModelNamedView(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of model view to retrieve

### Return Value

[IModelNamedView](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView.html)

## Examples

[Create Model and Sheet Views (JavaScript)](Create_Model_and_Sheet_Views_Example_JS.htm)
[Create Model and Sheet Views (C#)](Create_Model_and_Sheet_Views_Example_CSharp.htm)
[Create Model and Sheet Views (VB.NET)](Create_Model_and_Sheet_Views_Example_VBNET.htm)
[Create Model and Sheet Views (VBA)](Create_Model_and_Sheet_Views_Example_VBA.htm)

## See Also

[IViewManager Interface](Interop.dsAutomation~Interop.dsAutomation.IViewManager.html)
[IViewManager Members](Interop.dsAutomation~Interop.dsAutomation.IViewManager_members.html)
[IViewManager::ActivateModelView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~ActivateModelView.html)
[IViewManager::CreateModelNamedView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~CreateModelNamedView.html)
[IViewManager::GetModelNamedViewList Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetModelNamedViewList.html)
[IViewManager::SaveCurrentViewAsModelView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~SaveCurrentViewAsModelView.html)
[IViewManager::RemoveModelNamedView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~RemoveModelNamedView.html)

## Availability

DraftSight V1R1.4
