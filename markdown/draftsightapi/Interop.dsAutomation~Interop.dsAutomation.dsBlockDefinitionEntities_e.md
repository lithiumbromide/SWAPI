---
title: "dsBlockDefinitionEntities_e Enumeration"
project: ""
interface: "dsBlockDefinitionEntities_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsBlockDefinitionEntities_e.html"
---

# dsBlockDefinitionEntities_e Enumeration

Options for the source entities of Block definitions.

## Syntax

### Visual Basic

```vb
Public Enum dsBlockDefinitionEntities_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsBlockDefinitionEntities_e : System.Enum
```

### JScript

```
public enum dsBlockDefinitionEntities_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsBlockDefinitionEntities_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsBlockDefinitionEntities_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsBlockDefinitionEntities_ConvertToBlock | 2 = Replace the source entities with a Reference of the Block definition |
| dsBlockDefinitionEntities_PreserveAsSeparateEntities | 1 = Leave the source entities as they are |
| dsBlockDefinitionEntities_RemoveFromDrawing | 3 = Remove the source entities from the drawing |

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
