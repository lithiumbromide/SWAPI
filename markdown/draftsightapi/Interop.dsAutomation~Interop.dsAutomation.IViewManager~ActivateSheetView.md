---
title: "ActivateSheetView Method (IViewManager)"
project: ""
interface: "IViewManager"
member: "ActivateSheetView"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewManager~ActivateSheetView.html"
---

# ActivateSheetView Method (IViewManager)

Activates the sheet view with the specified name.

## Syntax

### Visual Basic

```vb
Sub ActivateSheetView( _
   ByVal Name As System.String _
)
```

### C#

```csharp
void ActivateSheetView(
   System.string Name
)
```

### JScript

```
function ActivateSheetView(
   Name : System.String
);
```

### Managed Extensions for C++

```
void ActivateSheetView(
   System.string* Name
)
```

### C++/CLI

```cpp
void ActivateSheetView(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of sheet view to activate

## Examples

[Create Model and Sheet Views (JavaScript)](Create_Model_and_Sheet_Views_Example_JS.htm)
[Create Model and Sheet Views (C#)](Create_Model_and_Sheet_Views_Example_CSharp.htm)
[Create Model and Sheet Views (VB.NET)](Create_Model_and_Sheet_Views_Example_VBNET.htm)
[Create Model and Sheet Views (VBA)](Create_Model_and_Sheet_Views_Example_VBA.htm)

## See Also

[IViewManager Interface](Interop.dsAutomation~Interop.dsAutomation.IViewManager.html)
[IViewManager Members](Interop.dsAutomation~Interop.dsAutomation.IViewManager_members.html)
[IViewManager::CreateSheetNamedView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~CreateSheetNamedView.html)
[IViewManager::GetSheetNamedView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetSheetNamedView.html)
[IViewManager::GetSheetNamedViewList Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetSheetNamedViewList.html)
[IViewManager::SaveCurrentViewAsSheetView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~SaveCurrentViewAsSheetView.html)
[IViewManager::RemoveSheetNamedView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~RemoveSheetNamedView.html)

## Availability

DraftSight V1R1.4
