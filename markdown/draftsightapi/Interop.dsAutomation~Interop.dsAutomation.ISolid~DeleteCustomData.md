---
title: "DeleteCustomData Method (ISolid)"
project: ""
interface: "ISolid"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISolid~DeleteCustomData.html"
---

# DeleteCustomData Method (ISolid)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the 2D Solid.

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

[ISolid Interface](Interop.dsAutomation~Interop.dsAutomation.ISolid.html)
[ISolid Members](Interop.dsAutomation~Interop.dsAutomation.ISolid_members.html)
[ISolid::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~GetCustomData.html)
[ISolid::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~SetCustomData.html)
[ISolid::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ISolid~Handle.html)

## Availability

DraftSight V1R1.3
