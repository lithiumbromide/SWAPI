---
title: "DeleteCustomData Method (IExtrudedSurface)"
project: ""
interface: "IExtrudedSurface"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface~DeleteCustomData.html"
---

# DeleteCustomData Method (IExtrudedSurface)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from this extruded surface.

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

[IExtrudedSurface Interface](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface.html)
[IExtrudedSurface Members](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface_members.html)
[IExtrudedSurface::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface~GetCustomData.html)
[IExtrudedSurface::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface~SetCustomData.html)

## Availability

DraftSight 2020 SP0
