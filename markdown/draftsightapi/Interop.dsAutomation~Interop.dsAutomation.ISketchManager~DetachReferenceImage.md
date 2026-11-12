---
title: "DetachReferenceImage Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "DetachReferenceImage"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~DetachReferenceImage.html"
---

# DetachReferenceImage Method (ISketchManager)

Detaches the specified Referenced image from the drawing.

## Syntax

### Visual Basic

```vb
Function DetachReferenceImage( _
   ByVal ReferenceImage As ReferenceImage _
) As System.Boolean
```

### C#

```csharp
System.bool DetachReferenceImage(
   ReferenceImage ReferenceImage
)
```

### JScript

```
function DetachReferenceImage(
   ReferenceImage : ReferenceImage
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool DetachReferenceImage(
   ReferenceImage* ReferenceImage
)
```

### C++/CLI

```cpp
System.bool DetachReferenceImage(
   ReferenceImage^ ReferenceImage
)
```

### Parameters

- `ReferenceImage`: [Referenced image](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage.html) to detach from the drawing

### Return Value

True if the Referenced image is detached from the drawing, false if not

## Remarks

This method removes the Referenced image from the drawing, including the link to the Referenced image.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertPicture Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPicture.html)
[IReferenceImage::Reload Method ()](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~Reload.html)
[IReferenceImage::Unload Method ()](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~Unload.html)

## Availability

DraftSight V1R5.0
