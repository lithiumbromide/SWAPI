---
title: "DeleteCustomData Method (IBlockInstance)"
project: ""
interface: "IBlockInstance"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~DeleteCustomData.html"
---

# DeleteCustomData Method (IBlockInstance)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) for the Block instance.

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

[IBlockInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)
[IBlockInstance Members](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance_members.html)
[IBlockInstance::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~GetCustomData.html)
[IBlockInstance::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~SetCustomData.html)
[IBlockInstance::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~Handle.html)

## Availability

DraftSight V1R1.2
