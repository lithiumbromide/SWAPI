---
title: "DeleteCustomData Method (IAttributeInstance)"
project: ""
interface: "IAttributeInstance"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~DeleteCustomData.html"
---

# DeleteCustomData Method (IAttributeInstance)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) for the BlockAttribute instance.

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

[IAttributeInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance.html)
[IAttributeInstance Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance_members.html)
[IAttributeInstance::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~GetCustomData.html)
[IAttributeInstance::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~SetCustomData.html)
[IAttributeInstance::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~Handle.html)

## Availability

DraftSight V1R1.2
