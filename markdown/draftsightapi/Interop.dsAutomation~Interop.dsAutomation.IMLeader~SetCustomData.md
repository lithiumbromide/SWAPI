---
title: "SetCustomData Method (IMLeader)"
project: ""
interface: "IMLeader"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~SetCustomData.html"
---

# SetCustomData Method (IMLeader)

Sets the custom data for this MLeader.

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

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)
[IMLeader::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IMLeader~GetCustomData.html)
[IMLeader::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IMLeader~DeleteCustomData.html)

## Availability

DraftSight 2024 SP4
