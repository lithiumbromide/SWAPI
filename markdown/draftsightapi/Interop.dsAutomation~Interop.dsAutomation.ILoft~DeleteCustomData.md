---
title: "DeleteCustomData Method (ILoft)"
project: ""
interface: "ILoft"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILoft~DeleteCustomData.html"
---

# DeleteCustomData Method (ILoft)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from this Loft.

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

[ILoft Interface](Interop.dsAutomation~Interop.dsAutomation.ILoft.html)
[ILoft Members](Interop.dsAutomation~Interop.dsAutomation.ILoft_members.html)
[ILoft::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ILoft~GetCustomData.html)
[ILoft::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ILoft~SetCustomData.html)

## Availability

DraftSight 2020 SP0
