---
title: "InsertRibbonRow Method (IRibbonRowPanel)"
project: ""
interface: "IRibbonRowPanel"
member: "InsertRibbonRow"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRibbonRowPanel~InsertRibbonRow.html"
---

# InsertRibbonRow Method (IRibbonRowPanel)

Inserts the specified ribbon row into this ribbon row panel.

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
- `RowName`: Name of the ribbon row to insert

### Return Value

[IRibbonRow](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow.html)

## Remarks

Up to three ribbon rows can be added to a ribbon row panel.

## See Also

[IRibbonRowPanel Interface](Interop.dsAutomation~Interop.dsAutomation.IRibbonRowPanel.html)
[IRibbonRowPanel Members](Interop.dsAutomation~Interop.dsAutomation.IRibbonRowPanel_members.html)

## Availability

DraftSight 2017 SP0
