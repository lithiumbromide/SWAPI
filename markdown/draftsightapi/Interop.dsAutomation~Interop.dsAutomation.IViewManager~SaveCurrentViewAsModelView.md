---
title: "SaveCurrentViewAsModelView Method (IViewManager)"
project: ""
interface: "IViewManager"
member: "SaveCurrentViewAsModelView"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewManager~SaveCurrentViewAsModelView.html"
---

# SaveCurrentViewAsModelView Method (IViewManager)

Saves the current model view with the specified name and category.

## Syntax

### Visual Basic

```vb
Function SaveCurrentViewAsModelView( _
   ByVal Name As System.String, _
   ByVal Class As System.String, _
   ByRef NamedView As ModelNamedView _
) As dsCreateObjectResult_e
```

### C#

```csharp
dsCreateObjectResult_e SaveCurrentViewAsModelView(
   System.string Name,
   System.string Class,
   out ModelNamedView NamedView
)
```

### JScript

```
function SaveCurrentViewAsModelView(
   Name : System.String,
   Class : System.String,
   NamedView : ModelNamedView
) : dsCreateObjectResult_e;
```

### Managed Extensions for C++

```
dsCreateObjectResult_e SaveCurrentViewAsModelView(
   System.string* Name,
   System.string* Class,
   [PARAMFLAG::Out] ModelNamedView* NamedView
)
```

### C++/CLI

```cpp
dsCreateObjectResult_e SaveCurrentViewAsModelView(
   System.String^ Name,
   System.String^ Class,
   [Out] ModelNamedView^ NamedView
)
```

### Parameters

- `Name`: Name of model named view
- `Class`: Name of category to which to assign this model named view
- `NamedView`: [IModelNamedView](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView.html)

### Return Value

Result status as defined in [dsCreateObjectResult_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateObjectResult_e.html)

## Examples

[Create Model and Sheet Views (JavaScript)](Create_Model_and_Sheet_Views_Example_JS.htm)
[Create Model and Sheet Views (VB.NET)](Create_Model_and_Sheet_Views_Example_VBNET.htm)
[Create Model and Sheet Views (C#)](Create_Model_and_Sheet_Views_Example_CSharp.htm)
[Create Model and Sheet Views (VBA)](Create_Model_and_Sheet_Views_Example_VBA.htm)

## See Also

[IViewManager Interface](Interop.dsAutomation~Interop.dsAutomation.IViewManager.html)
[IViewManager Members](Interop.dsAutomation~Interop.dsAutomation.IViewManager_members.html)
[IViewManager::ActivateModelView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~ActivateModelView.html)
[IViewManager::CreateModelNamedView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~CreateModelNamedView.html)
[IViewManager::GetModelNamedView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetModelNamedView.html)
[IViewManager::GetModelNamedViewList Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetModelNamedViewList.html)
[IViewManager::RemoveModelNamedView Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewManager~RemoveModelNamedView.html)

## Availability

DraftSight V1R1.4
