---
title: "DeleteCustomData Method (IPoint)"
project: ""
interface: "IPoint"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPoint~DeleteCustomData.html"
---

# DeleteCustomData Method (IPoint)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the point.

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

[IPoint Interface](Interop.dsAutomation~Interop.dsAutomation.IPoint.html)
[IPoint Members](Interop.dsAutomation~Interop.dsAutomation.IPoint_members.html)
[IPoint::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPoint~GetCustomData.html)
[IPoint::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPoint~SetCustomData.html)
[IPoint::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IPoint~Handle.html)

## Availability

DraftSight V1R1.2
