---
title: "ActivateModelView Method (IViewManager)"
project: ""
interface: "IViewManager"
member: "ActivateModelView"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewManager~ActivateModelView.html"
---

# ActivateModelView Method (IViewManager)

Activates the model view with the specified name.

## Syntax

### Visual Basic

```vb
Sub ActivateModelView( _
   ByVal Name As System.String _
)
```

### C#

```csharp
void ActivateModelView(
   System.string Name
)
```

### JScript

```
function ActivateModelView(
   Name : System.String
);
```

### Managed Extensions for C++

```
void ActivateModelView(
   System.string* Name
)
```

### C++/CLI

```cpp
void ActivateModelView(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of model view to activate

## Examples

[Create Model and Sheet Views (JavaScript)](Create_Model_and_Sheet_Views_Example_JS.htm)
[Create Model and Sheet Views (C#)](Create_Model_and_Sheet_Views_Example_CSharp.htm)
[Create Model and Sheet Views (VB.NET)](Create_Model_and_Sheet_Views_Example_VBNET.htm)
[Create Model and Sheet Views (VBA)](Create_Model_and_Sheet_Views_Example_VBA.htm)

## See Also

[IViewManager Interface](Interop.dsAutomation~Interop.dsAutomation.IViewManager.html)
[IViewManager Members](Interop.dsAutomation~Interop.dsAutomation.IViewManager_members.html)
[IViewManager::CreateModelNamedView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~CreateModelNamedView.html)
[IViewManager::GetModelNamedView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetModelNamedView.html)
[IViewManager::GetModelNamedViewList Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetModelNamedViewList.html)
[IViewManager::SaveCurrentViewAsModelView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~SaveCurrentViewAsModelView.html)
[IViewManager::RemoveModelNamedView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~RemoveModelNamedView.html)

## Availability

DraftSight V1R1.4
