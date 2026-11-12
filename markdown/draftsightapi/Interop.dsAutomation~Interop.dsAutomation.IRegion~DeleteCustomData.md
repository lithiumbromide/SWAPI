---
title: "DeleteCustomData Method (IRegion)"
project: ""
interface: "IRegion"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRegion~DeleteCustomData.html"
---

# DeleteCustomData Method (IRegion)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the Region.

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

[IRegion Interface](Interop.dsAutomation~Interop.dsAutomation.IRegion.html)
[IRegion Members](Interop.dsAutomation~Interop.dsAutomation.IRegion_members.html)
[IRegion::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRegion~GetCustomData.html)
[IRegion::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRegion~SetCustomData.html)
[IRegion::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IRegion~Handle.html)

## Availability

DraftSight V1R2.0
