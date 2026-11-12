---
title: "GetImageData Method (IReferenceImage)"
project: ""
interface: "IReferenceImage"
member: "GetImageData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~GetImageData.html"
---

# GetImageData Method (IReferenceImage)

Gets the image data of this Referenced image.

## Syntax

### Visual Basic

```vb
Sub GetImageData( _
   ByRef ImageData As System.Object, _
   ByRef Format As dsBitmapFormat_e _
)
```

### C#

```csharp
void GetImageData(
   out System.object ImageData,
   out dsBitmapFormat_e Format
)
```

### JScript

```
function GetImageData(
   ImageData : System.Object,
   Format : dsBitmapFormat_e
);
```

### Managed Extensions for C++

```
void GetImageData(
   [PARAMFLAG::Out] System.Object* ImageData,
   [PARAMFLAG::Out] dsBitmapFormat_e Format
)
```

### C++/CLI

```cpp
void GetImageData(
   [Out] System.Object^ ImageData,
   [Out] dsBitmapFormat_e Format
)
```

### Parameters

- `ImageData`: Array of binary data as defined by Format
- `Format`: Format as defined in [dsBitmapFormat_e](Interop.dsAutomation~Interop.dsAutomation.dsBitmapFormat_e.html)

## See Also

[IReferenceImage Interface](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage.html)
[IReferenceImage Members](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage_members.html)

## Availability

DraftSight 2019 SP0
