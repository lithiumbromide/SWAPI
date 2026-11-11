---
title: "InsertRibbonSplitButton Method (IRibbonRow)"
project: ""
interface: "IRibbonRow"
member: "InsertRibbonSplitButton"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRibbonRow~InsertRibbonSplitButton.html"
---

# InsertRibbonSplitButton Method (IRibbonRow)

Inserts the specified ribbon split button into this ribbon row.

## Syntax

### Visual Basic

```vb
Function InsertRibbonSplitButton( _
   ByVal ApiUuid As System.String, _
   ByVal ItemType As dsRibbonItemType_e, _
   ByVal ButtonStyle As dsRibbonButtonStyle_e, _
   ByVal SplitButtonListStyle As dsRibbonSplitButtonListStyle_e, _
   ByVal SplitButtonBehavior As dsRibbonSplitButtonBehaviour_e, _
   ByVal ItemName As System.String _
) As RibbonSplitButton
```

### C#

```csharp
RibbonSplitButton InsertRibbonSplitButton(
   System.string ApiUuid,
   dsRibbonItemType_e ItemType,
   dsRibbonButtonStyle_e ButtonStyle,
   dsRibbonSplitButtonListStyle_e SplitButtonListStyle,
   dsRibbonSplitButtonBehaviour_e SplitButtonBehavior,
   System.string ItemName
)
```

### JScript

```
function InsertRibbonSplitButton(
   ApiUuid : System.String,
   ItemType : dsRibbonItemType_e,
   ButtonStyle : dsRibbonButtonStyle_e,
   SplitButtonListStyle : dsRibbonSplitButtonListStyle_e,
   SplitButtonBehavior : dsRibbonSplitButtonBehaviour_e,
   ItemName : System.String
) : RibbonSplitButton;
```

### Managed Extensions for C++

```
RibbonSplitButton* InsertRibbonSplitButton(
   System.string* ApiUuid,
   dsRibbonItemType_e ItemType,
   dsRibbonButtonStyle_e ButtonStyle,
   dsRibbonSplitButtonListStyle_e SplitButtonListStyle,
   dsRibbonSplitButtonBehaviour_e SplitButtonBehavior,
   System.string* ItemName
)
```

### C++/CLI

```cpp
RibbonSplitButton^ InsertRibbonSplitButton(
   System.String^ ApiUuid,
   dsRibbonItemType_e ItemType,
   dsRibbonButtonStyle_e ButtonStyle,
   dsRibbonSplitButtonListStyle_e SplitButtonListStyle,
   dsRibbonSplitButtonBehaviour_e SplitButtonBehavior,
   System.String^ ItemName
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or application
- `ItemType`: Ribbon item type as defined in [dsRibbonItemType_e](Interop.dsAutomation~Interop.dsAutomation.dsRibbonItemType_e.html)
- `ButtonStyle`: Split button style as defined in [dsRibbonButtonStyle_e](Interop.dsAutomation~Interop.dsAutomation.dsRibbonButtonStyle_e.html)
- `SplitButtonListStyle`: Split button list style as defined in [dsRibbonSplitButtonListStyle_e](Interop.dsAutomation~Interop.dsAutomation.dsRibbonSplitButtonListStyle_e.html)
- `SplitButtonBehavior`: Split button behavior as defined in [dsRibbonSplitButtonBehavior_e](Interop.dsAutomation~Interop.dsAutomation.dsRibbonSplitButtonBehaviour_e.html)
- `ItemName`: Name of the ribbon row item in which to insert the split button

### Return Value

[IRibbonSplitButton](Interop.dsAutomation~Interop.dsAutomation.IRibbonSplitButton.html)

## Examples

See the [IRibbonRow](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow.html) example.

## See Also

[IRibbonRow Interface](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow.html)
[IRibbonRow Members](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow_members.html)
[IRibbonRow::GetRibbonRowItems Method ()](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow~GetRibbonRowItems.html)

## Availability

DraftSight 2017 SP0
