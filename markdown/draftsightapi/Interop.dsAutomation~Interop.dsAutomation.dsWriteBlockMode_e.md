---
title: "dsWriteBlockMode_e Enumeration"
project: ""
interface: "dsWriteBlockMode_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsWriteBlockMode_e.html"
---

# dsWriteBlockMode_e Enumeration

Ways of handling entities in the drawing after they are saved to a Block.

## Syntax

### Visual Basic

```vb
Public Enum dsWriteBlockMode_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsWriteBlockMode_e : System.Enum
```

### JScript

```
public enum dsWriteBlockMode_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsWriteBlockMode_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsWriteBlockMode_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsWriteBlockMode_ConvertToBlock | 1 = Replaces the entities in the drawing with a Reference to the Block |
| dsWriteBlockMode_Delete | 3 = Removes the entities from the drawing |
| dsWriteBlockMode_DoNotConvertToBlock | 2 = Leaves the entities unconverted in the drawing |

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
