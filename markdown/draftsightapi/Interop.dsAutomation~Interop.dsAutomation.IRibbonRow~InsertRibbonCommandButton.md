---
title: "InsertRibbonCommandButton Method (IRibbonRow)"
project: ""
interface: "IRibbonRow"
member: "InsertRibbonCommandButton"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRibbonRow~InsertRibbonCommandButton.html"
---

# InsertRibbonCommandButton Method (IRibbonRow)

Inserts the specified ribbon command button in this ribbon row.

## Syntax

### Visual Basic

```vb
Function InsertRibbonCommandButton( _
   ByVal ApiUuid As System.String, _
   ByVal ButtonStyle As dsRibbonButtonStyle_e, _
   ByVal ItemName As System.String, _
   ByVal UserCmdID As System.String _
) As RibbonCommandButton
```

### C#

```csharp
RibbonCommandButton InsertRibbonCommandButton(
   System.string ApiUuid,
   dsRibbonButtonStyle_e ButtonStyle,
   System.string ItemName,
   System.string UserCmdID
)
```

### JScript

```
function InsertRibbonCommandButton(
   ApiUuid : System.String,
   ButtonStyle : dsRibbonButtonStyle_e,
   ItemName : System.String,
   UserCmdID : System.String
) : RibbonCommandButton;
```

### Managed Extensions for C++

```
RibbonCommandButton* InsertRibbonCommandButton(
   System.string* ApiUuid,
   dsRibbonButtonStyle_e ButtonStyle,
   System.string* ItemName,
   System.string* UserCmdID
)
```

### C++/CLI

```cpp
RibbonCommandButton^ InsertRibbonCommandButton(
   System.String^ ApiUuid,
   dsRibbonButtonStyle_e ButtonStyle,
   System.String^ ItemName,
   System.String^ UserCmdID
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or application
- `ButtonStyle`: Style of the command button as defined in [dsRibbonButtonStyle_e](Interop.dsAutomation~Interop.dsAutomation.dsRibbonButtonStyle_e.html)
- `ItemName`: Name of the ribbon row item in which to insert the command button
- `UserCmdID`: User-defined command ID

### Return Value

[IRibbonCommandButton](Interop.dsAutomation~Interop.dsAutomation.IRibbonCommandButton.html)

## Examples

See the [IRibbonRow](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow.html) example.

## See Also

[IRibbonRow Interface](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow.html)
[IRibbonRow Members](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow_members.html)
[IRibbonRow::GetRibbonRowItems Method ()](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow~GetRibbonRowItems.html)

## Availability

DraftSight 2017 SP0
