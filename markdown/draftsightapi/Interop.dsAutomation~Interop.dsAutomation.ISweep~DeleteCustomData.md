---
title: "DeleteCustomData Method (ISweep)"
project: ""
interface: "ISweep"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISweep~DeleteCustomData.html"
---

# DeleteCustomData Method (ISweep)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from this Sweep.

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

[ISweep Interface](Interop.dsAutomation~Interop.dsAutomation.ISweep.html)
[ISweep Members](Interop.dsAutomation~Interop.dsAutomation.ISweep_members.html)
[ISweep::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ISweep~GetCustomData.html)
[ISweep::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ISweep~SetCustomData.html)

## Availability

DraftSight 2020 SP0
