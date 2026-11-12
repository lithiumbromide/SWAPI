---
title: "DeleteCustomData Method (ITrace)"
project: ""
interface: "ITrace"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITrace~DeleteCustomData.html"
---

# DeleteCustomData Method (ITrace)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the Trace.

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

[ITrace Interface](Interop.dsAutomation~Interop.dsAutomation.ITrace.html)
[ITrace Members](Interop.dsAutomation~Interop.dsAutomation.ITrace_members.html)
[ITrace::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ITrace~GetCustomData.html)
[ITrace::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ITrace~SetCustomData.html)
[ITrace::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.ITrace~Handle.html)

## Availability

DraftSight V1R5.0
