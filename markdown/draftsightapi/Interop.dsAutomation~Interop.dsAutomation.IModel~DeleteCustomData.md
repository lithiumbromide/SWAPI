---
title: "DeleteCustomData Method (IModel)"
project: ""
interface: "IModel"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IModel~DeleteCustomData.html"
---

# DeleteCustomData Method (IModel)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the model.

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

[IModel Interface](Interop.dsAutomation~Interop.dsAutomation.IModel.html)
[IModel Members](Interop.dsAutomation~Interop.dsAutomation.IModel_members.html)
[IModel::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IModel~GetCustomData.html)
[IModel::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IModel~SetCustomData.html)
[IModel::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IModel~Handle.html)

## Availability

DraftSight V1R1.2
