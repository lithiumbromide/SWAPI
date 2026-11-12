---
title: "CreateModelNamedView Method (IViewManager)"
project: ""
interface: "IViewManager"
member: "CreateModelNamedView"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewManager~CreateModelNamedView.html"
---

# CreateModelNamedView Method (IViewManager)

Creates a model named view.

## Syntax

### Visual Basic

```vb
Function CreateModelNamedView( _
   ByVal Name As System.String, _
   ByVal Class As System.String, _
   ByVal FirstCornerDblArray As System.Object, _
   ByVal OppositeCornerDblArray As System.Object, _
   ByRef NamedView As ModelNamedView _
) As dsCreateObjectResult_e
```

### C#

```csharp
dsCreateObjectResult_e CreateModelNamedView(
   System.string Name,
   System.string Class,
   System.object FirstCornerDblArray,
   System.object OppositeCornerDblArray,
   out ModelNamedView NamedView
)
```

### JScript

```
function CreateModelNamedView(
   Name : System.String,
   Class : System.String,
   FirstCornerDblArray : System.Object,
   OppositeCornerDblArray : System.Object,
   NamedView : ModelNamedView
) : dsCreateObjectResult_e;
```

### Managed Extensions for C++

```
dsCreateObjectResult_e CreateModelNamedView(
   System.string* Name,
   System.string* Class,
   System.Object* FirstCornerDblArray,
   System.Object* OppositeCornerDblArray,
   [PARAMFLAG::Out] ModelNamedView* NamedView
)
```

### C++/CLI

```cpp
dsCreateObjectResult_e CreateModelNamedView(
   System.String^ Name,
   System.String^ Class,
   System.Object^ FirstCornerDblArray,
   System.Object^ OppositeCornerDblArray,
   [Out] ModelNamedView^ NamedView
)
```

### Parameters

- `Name`: Name of the model named view
- `Class`: Name of category to which to assign this model named view
- `FirstCornerDblArray`: Array of doubles of the x, y, and z coordinates for the corner of the window that defines the view
- `OppositeCornerDblArray`: Array of doubles of the x, y, and z coordinates for the opposite corner of the window that defines the view
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
[IViewManager::GetModelNamedView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetModelNamedView.html)
[IViewManager::GetModelNamedViewList Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetModelNamedViewList.html)
[IViewManager::SaveCurrentViewAsModelView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~SaveCurrentViewAsModelView.html)
[IViewManager::RemoveModelNamedView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~RemoveModelNamedView.html)

## Availability

DraftSight V1R1.4
