---
title: "SetCustomData Method (IBlockDefinition)"
project: ""
interface: "IBlockDefinition"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~SetCustomData.html"
---

# SetCustomData Method (IBlockDefinition)

Sets the custom data for the Block definition.

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

[IBlockDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)
[IBlockDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition_members.html)
[IBlockDefinition::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~DeleteCustomData.html)
[IBlockDefinition::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~GetCustomData.html)
[IBlockDefinition::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~Handle.html)

## Availability

DraftSight V1R1.2
