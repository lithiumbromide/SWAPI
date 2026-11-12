---
title: "GetCustomData Method (IReferenceImage)"
project: ""
interface: "IReferenceImage"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~GetCustomData.html"
---

# GetCustomData Method (IReferenceImage)

Gets the specified custom data for the Referenced image.

## Syntax

### Visual Basic

```vb
Function GetCustomData( _
   ByVal ApplicationName As System.String _
) As CustomData
```

### C#

```csharp
CustomData GetCustomData(
   System.string ApplicationName
)
```

### JScript

```
function GetCustomData(
   ApplicationName : System.String
) : CustomData;
```

### Managed Extensions for C++

```
CustomData* GetCustomData(
   System.string* ApplicationName
)
```

### C++/CLI

```cpp
CustomData^ GetCustomData(
   System.String^ ApplicationName
)
```

### Parameters

- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)

### Return Value

[Custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[IReferenceImage Interface](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage.html)
[IReferenceImage Members](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage_members.html)
[IReferenceImage::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~DeleteCustomData.html)
[IReferenceImage::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~SetCustomData.html)
[IReferenceImage::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~Handle.html)

## Availability

DraftSight V1R1.2
