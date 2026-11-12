---
title: "GetSheetNamedView Method (IViewManager)"
project: ""
interface: "IViewManager"
member: "GetSheetNamedView"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetSheetNamedView.html"
---

# GetSheetNamedView Method (IViewManager)

Gets the sheet view with the specified name.

## Syntax

### Visual Basic

```vb
Function GetSheetNamedView( _
   ByVal Name As System.String _
) As SheetNamedView
```

### C#

```csharp
SheetNamedView GetSheetNamedView(
   System.string Name
)
```

### JScript

```
function GetSheetNamedView(
   Name : System.String
) : SheetNamedView;
```

### Managed Extensions for C++

```
SheetNamedView* GetSheetNamedView(
   System.string* Name
)
```

### C++/CLI

```cpp
SheetNamedView^ GetSheetNamedView(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of the sheet view to retrieve

### Return Value

[ISheetNamedView](Interop.dsAutomation~Interop.dsAutomation.ISheetNamedView.html)

## Examples

[Create Model and Sheet Views (JavaScript)](Create_Model_and_Sheet_Views_Example_JS.htm)
[Create Model and Sheet Views (VB.NET)](Create_Model_and_Sheet_Views_Example_VBNET.htm)
[Create Model and Sheet Views (C#)](Create_Model_and_Sheet_Views_Example_CSharp.htm)
[Create Model and Sheet Views (VBA)](Create_Model_and_Sheet_Views_Example_VBA.htm)

## See Also

[IViewManager Interface](Interop.dsAutomation~Interop.dsAutomation.IViewManager.html)
[IViewManager Members](Interop.dsAutomation~Interop.dsAutomation.IViewManager_members.html)
[IViewManager::ActivateSheetView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~ActivateSheetView.html)
[IViewManager::CreateSheetNamedView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~CreateSheetNamedView.html)
[IViewManager::GetSheetNamedViewList Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetSheetNamedViewList.html)
[IViewManager::SaveCurrentViewAsSheetView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~SaveCurrentViewAsSheetView.html)
[IViewManager::RemoveSheetNamedView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~RemoveSheetNamedView.html)

## Availability

DraftSight V1R1.4
