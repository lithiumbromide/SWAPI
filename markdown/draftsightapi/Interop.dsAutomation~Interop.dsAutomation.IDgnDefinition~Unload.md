---
title: "Unload Method (IDgnDefinition)"
project: ""
interface: "IDgnDefinition"
member: "Unload"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~Unload.html"
---

# Unload Method (IDgnDefinition)

Unloads the reference of this DGN definition.

## Syntax

### Visual Basic

```vb
Sub Unload()
```

### C#

```csharp
void Unload()
```

### JScript

```
function Unload();
```

### Managed Extensions for C++

```
void Unload();
```

### C++/CLI

```cpp
void Unload();
```

## Remarks

An unloaded DGN image is not visible in a drawing. However, the link to the file is maintained. Call [IDgnDefinition::Reload](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~Reload.html) to redisplay an unloaded image.

## See Also

[IDgnDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition.html)
[IDgnDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition_members.html)
[ISketchManager::InsertDgn Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertDgn.html)

## Availability

DraftSight 2020 SP0
