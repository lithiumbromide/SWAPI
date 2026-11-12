---
title: "SetCustomData Method (ISimpleNote)"
project: ""
interface: "ISimpleNote"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~SetCustomData.html"
---

# SetCustomData Method (ISimpleNote)

Sets the custom data for the SimpleNote.

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

[ISimpleNote Interface](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote.html)
[ISimpleNote Members](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote_members.html)
[ISimpleNote::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~DeleteCustomData.html)
[ISimpleNote::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~GetCustomData.html)
[ISimpleNote::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~Handle.html)

## Availability

DraftSight V1R1.2
