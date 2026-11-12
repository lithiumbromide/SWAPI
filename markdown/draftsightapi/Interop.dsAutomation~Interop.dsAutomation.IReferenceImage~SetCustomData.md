---
title: "SetCustomData Method (IReferenceImage)"
project: ""
interface: "IReferenceImage"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~SetCustomData.html"
---

# SetCustomData Method (IReferenceImage)

Sets the custom data for the Referenced image.

## Syntax

### Visual Basic

```vb
Sub SetCustomData( _
   ByVal ApplicationName As System.String, _
   ByVal CustomData As CustomData _
)
```

### C#

```csharp
void SetCustomData(
   System.string ApplicationName,
   CustomData CustomData
)
```

### JScript

```
function SetCustomData(
   ApplicationName : System.String,
   CustomData : CustomData
);
```

### Managed Extensions for C++

```
void SetCustomData(
   System.string* ApplicationName,
   CustomData* CustomData
)
```

### C++/CLI

```cpp
void SetCustomData(
   System.String^ ApplicationName,
   CustomData^ CustomData
)
```

### Parameters

- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)
- `CustomData`: [Custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[IReferenceImage Interface](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage.html)
[IReferenceImage Members](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage_members.html)
[IReferenceImage::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~DeleteCustomData.html)
[IReferenceImage::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~GetCustomData.html)
[IReferenceImage::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~Handle.html)

## Availability

DraftSight V1R1.2
