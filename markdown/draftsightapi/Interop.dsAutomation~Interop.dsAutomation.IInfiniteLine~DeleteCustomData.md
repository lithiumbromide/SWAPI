---
title: "DeleteCustomData Method (IInfiniteLine)"
project: ""
interface: "IInfiniteLine"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~DeleteCustomData.html"
---

# DeleteCustomData Method (IInfiniteLine)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the InfiniteLine.

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

[IInfiniteLine Interface](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)
[IInfiniteLine Members](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine_members.html)
[IInfiniteLine::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~GetCustomData.html)
[IInfiniteLine::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~SetCustomData.html)
[IInfiniteLine::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~Handle.html)

## Availability

DraftSight V1R1.2
