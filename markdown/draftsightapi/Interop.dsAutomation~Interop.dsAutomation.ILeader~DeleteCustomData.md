---
title: "DeleteCustomData Method (ILeader)"
project: ""
interface: "ILeader"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILeader~DeleteCustomData.html"
---

# DeleteCustomData Method (ILeader)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the Leader.

## Syntax

### Visual Basic

```vb
Sub DeleteCustomData( _
   ByVal ApplicationName As System.String _
)
```

### C#

```csharp
void DeleteCustomData(
   System.string ApplicationName
)
```

### JScript

```
function DeleteCustomData(
   ApplicationName : System.String
);
```

### Managed Extensions for C++

```
void DeleteCustomData(
   System.string* ApplicationName
)
```

### C++/CLI

```cpp
void DeleteCustomData(
   System.String^ ApplicationName
)
```

### Parameters

- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[ILeader Interface](Interop.dsAutomation~Interop.dsAutomation.ILeader.html)
[ILeader Members](Interop.dsAutomation~Interop.dsAutomation.ILeader_members.html)
[ILeader::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ILeader~GetCustomData.html)
[ILeader::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ILeader~SetCustomData.html)
[ILeader::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ILeader~Handle.html)

## Availability

DraftSight V1R1.2
