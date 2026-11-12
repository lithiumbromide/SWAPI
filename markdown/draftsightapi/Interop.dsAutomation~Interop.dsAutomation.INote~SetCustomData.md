---
title: "SetCustomData Method (INote)"
project: ""
interface: "INote"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.INote~SetCustomData.html"
---

# SetCustomData Method (INote)

Sets the custom data for the Note.

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

[INote Interface](Interop.dsAutomation~Interop.dsAutomation.INote.html)
[INote Members](Interop.dsAutomation~Interop.dsAutomation.INote_members.html)
[INote::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.INote~DeleteCustomData.html)
[INote::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.INote~GetCustomData.html)
[INote::Handle Property](Interop.dsAutomation~Interop.dsAutomation.INote~Handle.html)

## Availability

DraftSight V1R1.2
