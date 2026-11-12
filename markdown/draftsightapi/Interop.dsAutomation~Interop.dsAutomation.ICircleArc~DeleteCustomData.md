---
title: "DeleteCustomData Method (ICircleArc)"
project: ""
interface: "ICircleArc"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICircleArc~DeleteCustomData.html"
---

# DeleteCustomData Method (ICircleArc)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the Arc.

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

[ICircleArc Interface](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)
[ICircleArc Members](Interop.dsAutomation~Interop.dsAutomation.ICircleArc_members.html)
[ICircleArc::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~GetCustomData.html)
[ICircleArc::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~SetCustomData.html)
[ICircleArc::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~Handle.html)

## Availability

DraftSight V1R1.2
