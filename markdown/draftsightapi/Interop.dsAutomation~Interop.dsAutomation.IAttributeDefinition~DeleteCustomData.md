---
title: "DeleteCustomData Method (IAttributeDefinition)"
project: ""
interface: "IAttributeDefinition"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~DeleteCustomData.html"
---

# DeleteCustomData Method (IAttributeDefinition)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the BlockAttribute definition.

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

[IAttributeDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition.html)
[IAttributeDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition_members.html)
[IAttributeDefinition::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~GetCustomData.html)
[IAttributeDefinition::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~SetCustomData.html)
[IAttributeDefinition::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~Handle.html)

## Availability

DraftSight V1R1.2
