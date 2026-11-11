---
title: "SetCustomData Method (ITrace)"
project: ""
interface: "ITrace"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITrace~SetCustomData.html"
---

# SetCustomData Method (ITrace)

Sets the custom data for this Trace.

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

[ITrace Interface](Interop.dsAutomation~Interop.dsAutomation.ITrace.html)
[ITrace Members](Interop.dsAutomation~Interop.dsAutomation.ITrace_members.html)
[ITrace::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ITrace~GetCustomData.html)
[ITrace::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ITrace~DeleteCustomData.html)
[ITrace::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.ITrace~Handle.html)

## Availability

DraftSight V1R5.0
