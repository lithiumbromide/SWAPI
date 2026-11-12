---
title: "InsertRibbonRow Method (IRibbonPanel)"
project: ""
interface: "IRibbonPanel"
member: "InsertRibbonRow"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRibbonPanel~InsertRibbonRow.html"
---

# InsertRibbonRow Method (IRibbonPanel)

Inserts the specified ribbon row into this ribbon panel.

## Syntax

### Visual Basic

```vb
Function InsertRibbonRow( _
   ByVal ApiUuid As System.String, _
   ByVal RowName As System.String _
) As RibbonRow
```

### C#

```csharp
RibbonRow InsertRibbonRow(
   System.string ApiUuid,
   System.string RowName
)
```

### JScript

```
function InsertRibbonRow(
   ApiUuid : System.String,
   RowName : System.String
) : RibbonRow;
```

### Managed Extensions for C++

```
RibbonRow* InsertRibbonRow(
   System.string* ApiUuid,
   System.string* RowName
)
```

### C++/CLI

```cpp
RibbonRow^ InsertRibbonRow(
   System.String^ ApiUuid,
   System.String^ RowName
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or application
- `RowName`: Name of the ribbon row

### Return Value

[IRibbonRow](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow.html)

## Examples

See the [IRibbonPanel](Interop.dsAutomation~Interop.dsAutomation.IRibbonPanel.html) example.

## Remarks

Only one ribbon row can be added to a ribbon panel.

## See Also

[IRibbonPanel Interface](Interop.dsAutomation~Interop.dsAutomation.IRibbonPanel.html)
[IRibbonPanel Members](Interop.dsAutomation~Interop.dsAutomation.IRibbonPanel_members.html)

## Availability

DraftSight 2017 SP0
