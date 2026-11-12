---
title: "Unload Method (IPdfReference)"
project: ""
interface: "IPdfReference"
member: "Unload"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPdfReference~Unload.html"
---

# Unload Method (IPdfReference)

Unloads this PDF reference.

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

An unloaded PDF image is not visible in a drawing. However, the link to the file is maintained. Call [IPdfReference::Reload](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~Reload.html) to redisplay an unloaded image.

## See Also

[IPdfReference Interface](Interop.dsAutomation~Interop.dsAutomation.IPdfReference.html)
[IPdfReference Members](Interop.dsAutomation~Interop.dsAutomation.IPdfReference_members.html)
[ISketchManager::InsertPdf Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPdf.html)

## Availability

DraftSight 2020 SP0
