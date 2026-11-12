---
title: "dsSelectionRemove_e Enumeration"
project: ""
interface: "dsSelectionRemove_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsSelectionRemove_e.html"
---

# dsSelectionRemove_e Enumeration

Options to allow and disallow selections. [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum dsSelectionRemove_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsSelectionRemove_e : System.Enum
```

### JScript

```
public enum dsSelectionRemove_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsSelectionRemove_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsSelectionRemove_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsSelectionRemove_Cloud | 128 or 0x80 = Disallow selection of Clouds |
| dsSelectionRemove_None | 0 or 0x0 = Allow selection of the entity without any restrictions |
| dsSelectionRemove_NotInCurrentSpace | 8 or 0x8 = Disallow selection of the entity if not in current space |
| dsSelectionRemove_NotInWorkingSet | 64 or 0x40 = Disallow selection of the entity if not in working set |
| dsSelectionRemove_NotRectViewports | 16 or 0x10 = Disallow selection of None Rectangular Viewports |
| dsSelectionRemove_OnFrozenLayers | 4 or 0x4 = Disallow selection of the entity if on a frozen Layer |
| dsSelectionRemove_OnLockedLayers | 1 or 0x1 = Disallow selection of the entity if on a Layer that is locked |
| dsSelectionRemove_OnOffLayers | 2 or 0x2 = Disallow selection of the entity if on a Layer that is turned off |
| dsSelectionRemove_OverallViewports | 128 or 0x80 = Disallow selection of Overall Viewports |

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
