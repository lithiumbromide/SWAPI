---
title: "DeleteCustomData Method (ITolerance)"
project: ""
interface: "ITolerance"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITolerance~DeleteCustomData.html"
---

# DeleteCustomData Method (ITolerance)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the geometric Tolerance.

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

[ITolerance Interface](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html)
[ITolerance Members](Interop.dsAutomation~Interop.dsAutomation.ITolerance_members.html)
[ITolerance::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ITolerance~GetCustomData.html)
[ITolerance::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ITolerance~SetCustomData.html)
[ITolerance::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ITolerance~Handle.html)

## Availability

DraftSight V1R1.2
