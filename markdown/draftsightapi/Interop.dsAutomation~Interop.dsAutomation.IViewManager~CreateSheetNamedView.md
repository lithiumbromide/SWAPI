---
title: "CreateSheetNamedView Method (IViewManager)"
project: ""
interface: "IViewManager"
member: "CreateSheetNamedView"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewManager~CreateSheetNamedView.html"
---

# CreateSheetNamedView Method (IViewManager)

Creates a sheet named view.

## Syntax

### Visual Basic

```vb
Function CreateSheetNamedView( _
   ByVal Name As System.String, _
   ByVal Class As System.String, _
   ByVal FirstCornerDblArray As System.Object, _
   ByVal OppositeCornerDblArray As System.Object, _
   ByRef NamedView As SheetNamedView _
) As dsCreateObjectResult_e
```

### C#

```csharp
dsCreateObjectResult_e CreateSheetNamedView(
   System.string Name,
   System.string Class,
   System.object FirstCornerDblArray,
   System.object OppositeCornerDblArray,
   out SheetNamedView NamedView
)
```

### JScript

```
function CreateSheetNamedView(
   Name : System.String,
   Class : System.String,
   FirstCornerDblArray : System.Object,
   OppositeCornerDblArray : System.Object,
   NamedView : SheetNamedView
) : dsCreateObjectResult_e;
```

### Managed Extensions for C++

```
dsCreateObjectResult_e CreateSheetNamedView(
   System.string* Name,
   System.string* Class,
   System.Object* FirstCornerDblArray,
   System.Object* OppositeCornerDblArray,
   [PARAMFLAG::Out] SheetNamedView* NamedView
)
```

### C++/CLI

```cpp
dsCreateObjectResult_e CreateSheetNamedView(
   System.String^ Name,
   System.String^ Class,
   System.Object^ FirstCornerDblArray,
   System.Object^ OppositeCornerDblArray,
   [Out] SheetNamedView^ NamedView
)
```

### Parameters

- `Name`: Name of the sheet named view
- `Class`: Name of category to which to assign this sheet named view
- `FirstCornerDblArray`: Array of doubles of the x, y, and z coordinates for the corner of the window that defines the view
- `OppositeCornerDblArray`: Array of doubles of the x, y, and z coordinates for the opposite corner of the window that defines the view
- `NamedView`: [ISheetNamedView](Interop.dsAutomation~Interop.dsAutomation.ISheetNamedView.html)

### Return Value

Result status as defined in [dsCreateObjectResult_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateObjectResult_e.html)

## Examples

[Create Model and Sheet Views (JavaScript)](Create_Model_and_Sheet_Views_Example_JS.htm)
[Create Model and Sheet Views (C#)](Create_Model_and_Sheet_Views_Example_CSharp.htm)
[Create Model and Sheet Views (VB.NET)](Create_Model_and_Sheet_Views_Example_VBNET.htm)
[Create Model and Sheet Views (VBA)](Create_Model_and_Sheet_Views_Example_VBA.htm)

## See Also

[IViewManager Interface](Interop.dsAutomation~Interop.dsAutomation.IViewManager.html)
[IViewManager Members](Interop.dsAutomation~Interop.dsAutomation.IViewManager_members.html)
[IViewManager::ActivateSheetView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~ActivateSheetView.html)
[IViewManager::GetSheetNamedView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetSheetNamedView.html)
[IViewManager::GetSheetNamedViewList Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~GetSheetNamedViewList.html)
[IViewManager::SaveCurrentViewAsSheetView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~SaveCurrentViewAsSheetView.html)
[IViewManager::RemoveSheetNamedView Method](Interop.dsAutomation~Interop.dsAutomation.IViewManager~RemoveSheetNamedView.html)

## Availability

DraftSight V1R1.4
