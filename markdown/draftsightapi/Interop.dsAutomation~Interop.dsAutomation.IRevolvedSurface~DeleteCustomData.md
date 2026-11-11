---
title: "DeleteCustomData Method (IRevolvedSurface)"
project: ""
interface: "IRevolvedSurface"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface~DeleteCustomData.html"
---

# DeleteCustomData Method (IRevolvedSurface)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from this revolved surface

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

[IRevolvedSurface Interface](Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface.html)
[IRevolvedSurface Members](Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface_members.html)
[IRevolvedSurface::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface~GetCustomData.html)
[IRevolvedSurface::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface~SetCustomData.html)

## Availability

DraftSight 2020 SP0
