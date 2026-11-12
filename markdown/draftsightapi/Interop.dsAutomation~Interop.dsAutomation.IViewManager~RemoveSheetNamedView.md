---
title: "RemoveSheetNamedView Method (IViewManager)"
project: ""
interface: "IViewManager"
member: "RemoveSheetNamedView"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewManager~RemoveSheetNamedView.html"
---

# RemoveSheetNamedView Method (IViewManager)

Removes the specified sheet named view from the document.

## Syntax

### Visual Basic

```vb
Function RemoveSheetNamedView( _
   ByVal NamedView As SheetNamedView _
) As System.Boolean
```

### C#

```csharp
System.bool RemoveSheetNamedView(
   SheetNamedView NamedView
)
```

### JScript

```
function RemoveSheetNamedView(
   NamedView : SheetNamedView
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool RemoveSheetNamedView(
   SheetNamedView* NamedView
)
```

### C++/CLI

```cpp
System.bool RemoveSheetNamedView(
   SheetNamedView^ NamedView
)
```

### Parameters

- `NamedView`: [Sheet named view](Interop.dsAutomation~Interop.dsAutomation.ISheetNamedView.html) to remove

## See Also

[IViewManager Interface](Interop.dsAutomation~Interop.dsAutomation.IViewManager.html)
[IViewManager Members](Interop.dsAutomation~Interop.dsAutomation.IViewManager_members.html)
[IViewManager::ActivateSheetView Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewManager~ActivateSheetView.html)
[IViewManager::CreateSheetNamedView Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewManager~CreateSheetNamedView.html)
[IViewManager::GetSheetNamedView Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetSheetNamedView.html)
[IViewManager::GetSheetNamedViewList Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetSheetNamedViewList.html)
[IViewManager::SaveCurrentViewAsSheetView Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewManager~SaveCurrentViewAsSheetView.html)

## Availability

DraftSight V1R5.0
