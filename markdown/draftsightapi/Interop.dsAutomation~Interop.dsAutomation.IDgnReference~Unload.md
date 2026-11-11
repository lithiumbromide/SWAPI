---
title: "Unload Method (IDgnReference)"
project: ""
interface: "IDgnReference"
member: "Unload"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDgnReference~Unload.html"
---

# Unload Method (IDgnReference)

Unloads this DGN reference.

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

An unloaded DGN image is not visible in a drawing. However, the link to the file is maintained. Call [IDgnReference::Reload](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~Reload.html) to redisplay an unloaded image.

## See Also

[IDgnReference Interface](Interop.dsAutomation~Interop.dsAutomation.IDgnReference.html)
[IDgnReference Members](Interop.dsAutomation~Interop.dsAutomation.IDgnReference_members.html)
[ISketchManager::InsertDgn Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertDgn.html)

## Availability

DraftSight 2020 SP0
