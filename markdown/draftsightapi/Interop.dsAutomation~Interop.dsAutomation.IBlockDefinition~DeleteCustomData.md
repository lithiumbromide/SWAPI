---
title: "DeleteCustomData Method (IBlockDefinition)"
project: ""
interface: "IBlockDefinition"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~DeleteCustomData.html"
---

# DeleteCustomData Method (IBlockDefinition)

Deletes the specified custom data for the Block definition.

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

[IBlockDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)
[IBlockDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition_members.html)
[IBlockDefinition::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~GetCustomData.html)
[IBlockDefinition::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~SetCustomData.html)
[IBlockDefinition::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~Handle.html)

## Availability

DraftSight V1R1.2
