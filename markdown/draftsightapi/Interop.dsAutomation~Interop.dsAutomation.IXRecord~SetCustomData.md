---
title: "SetCustomData Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetCustomData.html"
---

# SetCustomData Method (IXRecord)

Sets the custom data for this XRecord.

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

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~DeleteCustomData.html)
[IXRecord::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetCustomData.html)
[IXRecord::GetHandleData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetHandleData.html)
[IXRecord::InsertHandle Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertHandle.html)
[IXRecord::SetHandle Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetHandle.html)
[IXRecord::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~Handle.html)

## Availability

DraftSight V1R4.0
