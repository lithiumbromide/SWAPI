---
title: "dsOffsetType_e Enumeration"
project: ""
interface: "dsOffsetType_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsOffsetType_e.html"
---

# dsOffsetType_e Enumeration

Sketch offset gap types.

## Syntax

### Visual Basic

```vb
Public Enum dsOffsetType_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsOffsetType_e : System.Enum
```

### JScript

```
public enum dsOffsetType_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsOffsetType_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsOffsetType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsOffsetType_Arc | 1 = Fillets gaps; the fillet radius is equal to the offset distance |
| dsOffsetType_Corner | 2 = Chamfers gaps; the perpendicular distance from each chamfer to its corresponding vertex on the source linear polyline segment is equal to the offset distance |
| dsOffsetType_Natural | 0 = Extends linear polyline segments to their projected intersections |

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
