---
title: "InsertRibbonSeparator Method (IRibbonRow)"
project: ""
interface: "IRibbonRow"
member: "InsertRibbonSeparator"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRibbonRow~InsertRibbonSeparator.html"
---

# InsertRibbonSeparator Method (IRibbonRow)

Inserts a ribbon row separator into this ribbon row.

## Syntax

### Visual Basic

```vb
Function InsertRibbonSeparator( _
   ByVal ApiUuid As System.String, _
   ByVal SeparatorStyle As dsRibbonSeparatorStyle_e _
) As RibbonSeparator
```

### C#

```csharp
RibbonSeparator InsertRibbonSeparator(
   System.string ApiUuid,
   dsRibbonSeparatorStyle_e SeparatorStyle
)
```

### JScript

```
function InsertRibbonSeparator(
   ApiUuid : System.String,
   SeparatorStyle : dsRibbonSeparatorStyle_e
) : RibbonSeparator;
```

### Managed Extensions for C++

```
RibbonSeparator* InsertRibbonSeparator(
   System.string* ApiUuid,
   dsRibbonSeparatorStyle_e SeparatorStyle
)
```

### C++/CLI

```cpp
RibbonSeparator^ InsertRibbonSeparator(
   System.String^ ApiUuid,
   dsRibbonSeparatorStyle_e SeparatorStyle
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or application
- `SeparatorStyle`: Separator style as defined in [dsRibbonSeparatorStyle_e](Interop.dsAutomation~Interop.dsAutomation.dsRibbonSeparatorStyle_e.html)

### Return Value

[IRibbonSeparator](Interop.dsAutomation~Interop.dsAutomation.IRibbonSeparator.html)

## Examples

See the [IRibbonRow](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow.html) example.

## See Also

[IRibbonRow Interface](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow.html)
[IRibbonRow Members](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow_members.html)
[IRibbonRow::GetRibbonRowItems Method ()](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow~GetRibbonRowItems.html)

## Availability

DraftSight 2017 SP0
