---
title: "SetClipBoundary Method (IReferenceImage)"
project: ""
interface: "IReferenceImage"
member: "SetClipBoundary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~SetClipBoundary.html"
---

# SetClipBoundary Method (IReferenceImage)

Sets the clipping boundary for this Referenced image.

## Syntax

### Visual Basic

```vb
Sub SetClipBoundary( _
   ByVal ClipPointsDblArray As System.Object _
)
```

### C#

```csharp
void SetClipBoundary(
   System.object ClipPointsDblArray
)
```

### JScript

```
function SetClipBoundary(
   ClipPointsDblArray : System.Object
);
```

### Managed Extensions for C++

```
void SetClipBoundary(
   System.Object* ClipPointsDblArray
)
```

### C++/CLI

```cpp
void SetClipBoundary(
   System.Object^ ClipPointsDblArray
)
```

### Parameters

- `ClipPointsDblArray`: Array of doubles indicating the x, y pixel coordinates of the clipping boundary

## See Also

[IReferenceImage Interface](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage.html)
[IReferenceImage Members](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage_members.html)
[IReferenceImage::GetClipBoundary Method ()](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~GetClipBoundary.html)
[IReferenceImage::RemoveClipBoundary Method ()](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~RemoveClipBoundary.html)

## Availability

DraftSight V1R6.0
