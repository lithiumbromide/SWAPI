---
title: "dsCleanObjectType_e Enumeration"
project: ""
interface: "dsCleanObjectType_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsCleanObjectType_e.html"
---

# dsCleanObjectType_e Enumeration

Type of objects to purge from a document. [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum dsCleanObjectType_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsCleanObjectType_e : System.Enum
```

### JScript

```
public enum dsCleanObjectType_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsCleanObjectType_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsCleanObjectType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsCleanObjectType_Blocks | 1 or 0x001 |
| dsCleanObjectType_DimensionStyles | 2 or 0x002 |
| dsCleanObjectType_Layers | 4 or 0x004 |
| dsCleanObjectType_LineStyles | 8 or 0x008 |
| dsCleanObjectType_Materials | 16 or 0x010 |
| dsCleanObjectType_PrintStyles | 32 or 0x020 |
| dsCleanObjectType_RLineStyles | 64 or 0x040 |
| dsCleanObjectType_Shapes | 128 or 0x080 |
| dsCleanObjectType_TableStyles | 256 or 0x100 |
| dsCleanObjectType_TextStyles | 512 or 0x200 |

## Remarks

0 = All types

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
