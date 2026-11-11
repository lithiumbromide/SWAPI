---
title: "SetCustomData Method (IDgnReference)"
project: ""
interface: "IDgnReference"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDgnReference~SetCustomData.html"
---

# SetCustomData Method (IDgnReference)

Sets the custom data for this DGN reference.

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

[IDgnReference Interface](Interop.dsAutomation~Interop.dsAutomation.IDgnReference.html)
[IDgnReference Members](Interop.dsAutomation~Interop.dsAutomation.IDgnReference_members.html)
[IDgnReference::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~DeleteCustomData.html)
[IDgnReference::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~GetCustomData.html)
[IDgnReference::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~Handle.html)

## Availability

DraftSight 2020 SP0
