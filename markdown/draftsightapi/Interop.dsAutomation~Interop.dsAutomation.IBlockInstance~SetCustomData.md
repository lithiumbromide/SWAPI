---
title: "SetCustomData Method (IBlockInstance)"
project: ""
interface: "IBlockInstance"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~SetCustomData.html"
---

# SetCustomData Method (IBlockInstance)

Sets the custom data for the Block instance.

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

[IBlockInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)
[IBlockInstance Members](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance_members.html)
[IBlockInstance::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~DeleteCustomData.html)
[IBlockInstance::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~GetCustomData.html)
[IBlockInstance::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~Handle.html)

## Availability

DraftSight V1R1.2
