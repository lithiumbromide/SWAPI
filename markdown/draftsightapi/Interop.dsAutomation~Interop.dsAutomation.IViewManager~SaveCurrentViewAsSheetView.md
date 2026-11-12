---
title: "SaveCurrentViewAsSheetView Method (IViewManager)"
project: ""
interface: "IViewManager"
member: "SaveCurrentViewAsSheetView"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewManager~SaveCurrentViewAsSheetView.html"
---

# SaveCurrentViewAsSheetView Method (IViewManager)

Saves the current sheet view with the specified name and category.

## Syntax

### Visual Basic

```vb
Function SaveCurrentViewAsSheetView( _
   ByVal Name As System.String, _
   ByVal Class As System.String, _
   ByRef NamedView As SheetNamedView _
) As dsCreateObjectResult_e
```

### C#

```csharp
dsCreateObjectResult_e SaveCurrentViewAsSheetView(
   System.string Name,
   System.string Class,
   out SheetNamedView NamedView
)
```

### JScript

```
function SaveCurrentViewAsSheetView(
   Name : System.String,
   Class : System.String,
   NamedView : SheetNamedView
) : dsCreateObjectResult_e;
```

### Managed Extensions for C++

```
dsCreateObjectResult_e SaveCurrentViewAsSheetView(
   System.string* Name,
   System.string* Class,
   [PARAMFLAG::Out] SheetNamedView* NamedView
)
```

### C++/CLI

```cpp
dsCreateObjectResult_e SaveCurrentViewAsSheetView(
   System.String^ Name,
   System.String^ Class,
   [Out] SheetNamedView^ NamedView
)
```

### Parameters

- `Name`: Name of sheet named view
- `Class`: Name of category to which to assign this sheet named view
- `NamedView`: [ISheetNamedView](Interop.dsAutomation~Interop.dsAutomation.ISheetNamedView.html)

### Return Value

Result status as defined in [dsCreateObjectResult_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateObjectResult_e.html)

## Examples

[Create Model and Sheet Views (C#)](Create_Model_and_Sheet_Views_Example_CSharp.htm)
[Create Model and Sheet Views (VB.NET)](Create_Model_and_Sheet_Views_Example_VBNET.htm)
[Create Model and Sheet Views (JavaScript)](Create_Model_and_Sheet_Views_Example_JS.htm)
[Create Model and Sheet Views (VBA)](Create_Model_and_Sheet_Views_Example_VBA.htm)

## See Also

[IViewManager Interface](Interop.dsAutomation~Interop.dsAutomation.IViewManager.html)
[IViewManager Members](Interop.dsAutomation~Interop.dsAutomation.IViewManager_members.html)
[IViewManager::ActivateSheetView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~ActivateSheetView.html)
[IViewManager::CreateSheetNamedView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~CreateSheetNamedView.html)
[IViewManager::GetSheetNamedView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetSheetNamedView.html)
[IViewManager::GetSheetNamedViewList Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetSheetNamedViewList.html)
[IViewManager::RemoveSheetNamedView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~RemoveSheetNamedView.html)

## Availability

DraftSight V1R1.4
