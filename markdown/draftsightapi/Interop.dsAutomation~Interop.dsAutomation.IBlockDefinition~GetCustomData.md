---
title: "GetCustomData Method (IBlockDefinition)"
project: ""
interface: "IBlockDefinition"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~GetCustomData.html"
---

# GetCustomData Method (IBlockDefinition)

Gets the specified custom data for the Block definition.

## Syntax

### Visual Basic

```vb
Function GetCustomData( _
   ByVal ApplicationName As System.String _
) As CustomData
```

### C#

```csharp
CustomData GetCustomData(
   System.string ApplicationName
)
```

### JScript

```
function GetCustomData(
   ApplicationName : System.String
) : CustomData;
```

### Managed Extensions for C++

```
CustomData* GetCustomData(
   System.string* ApplicationName
)
```

### C++/CLI

```cpp
CustomData^ GetCustomData(
   System.String^ ApplicationName
)
```

### Parameters

- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)

### Return Value

[Custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[IBlockDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)
[IBlockDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition_members.html)
[IBlockDefinition::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~DeleteCustomData.html)
[IBlockDefinition::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~SetCustomData.html)
[IBlockDefinition::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~Handle.html)

## Availability

DraftSight V1R1.2
