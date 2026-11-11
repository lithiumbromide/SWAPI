---
title: "Unload Method (IReferenceImage)"
project: ""
interface: "IReferenceImage"
member: "Unload"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~Unload.html"
---

# Unload Method (IReferenceImage)

Unloads the Referenced image.

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

An unloaded Referenced image is not visible in a drawing. However, the link to the file is maintained. Call [IReferenceImage::Reload](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~Reload.html) to redisplay an unloaded image.

## See Also

[IReferenceImage Interface](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage.html)
[IReferenceImage Members](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage_members.html)
[ISketchManager::DetachReferenceImage Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~DetachReferenceImage.html)
[ISketchManager::InsertPicture Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPicture.html)

## Availability

DraftSight V1R5.0
