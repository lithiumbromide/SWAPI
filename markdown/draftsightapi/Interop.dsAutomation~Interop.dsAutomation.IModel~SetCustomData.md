---
title: "SetCustomData Method (IModel)"
project: ""
interface: "IModel"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IModel~SetCustomData.html"
---

# SetCustomData Method (IModel)

Sets the custom data for the model.

## Syntax

### Visual Basic

```vb
Sub SetCustomData( _
   ByVal ApplicationName As System.String, _
   ByVal CustomData As CustomData _
)
```

### C#

```csharp
void SetCustomData(
   System.string ApplicationName,
   CustomData CustomData
)
```

### JScript

```
function SetCustomData(
   ApplicationName : System.String,
   CustomData : CustomData
);
```

### Managed Extensions for C++

```
void SetCustomData(
   System.string* ApplicationName,
   CustomData* CustomData
)
```

### C++/CLI

```cpp
void SetCustomData(
   System.String^ ApplicationName,
   CustomData^ CustomData
)
```

### Parameters

- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)
- `CustomData`: [Custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[IModel Interface](Interop.dsAutomation~Interop.dsAutomation.IModel.html)
[IModel Members](Interop.dsAutomation~Interop.dsAutomation.IModel_members.html)
[IModel::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IModel~DeleteCustomData.html)
[IModel::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IModel~GetCustomData.html)
[IModel::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IModel~Handle.html)

## Availability

DraftSight V1R1.2
