---
title: "DeleteCustomData Method (ILoftedSurface)"
project: ""
interface: "ILoftedSurface"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface~DeleteCustomData.html"
---

# DeleteCustomData Method (ILoftedSurface)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from this lofted surface.

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

[ILoftedSurface Interface](Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface.html)
[ILoftedSurface Members](Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface_members.html)
[ILoftedSurface::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface~GetCustomData.html)
[ILoftedSurface::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface~SetCustomData.html)

## Availability

DraftSight 2020 SP0
