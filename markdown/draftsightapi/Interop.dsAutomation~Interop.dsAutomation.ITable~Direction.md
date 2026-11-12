---
title: "Direction Property (ITable)"
project: ""
interface: "ITable"
member: "Direction"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~Direction.html"
---

# Direction Property (ITable)

Gets or sets the header orientation of the table.

## Syntax

### Visual Basic

```vb
Property Direction As dsTableDirection_e
```

### C#

```csharp
dsTableDirection_e Direction {get; set;}
```

### JScript

```
function get,set Direction : dsTableDirection_e
```

### Managed Extensions for C++

```
__property dsTableDirection_e get_Direction();
__property void set_Direction(
   dsTableDirection_e value
);
```

### C++/CLI

```cpp
property dsTableDirection_e Direction {
   dsTableDirection_e get();
   void set (    dsTableDirection_e value);
}
```

### Property Value

Header orientation of the table as defined in [dsTableDirection_e](Interop.dsAutomation~Interop.dsAutomation.dsTableDirection_e.html)

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)

## Availability

DraftSight V1R5.0
