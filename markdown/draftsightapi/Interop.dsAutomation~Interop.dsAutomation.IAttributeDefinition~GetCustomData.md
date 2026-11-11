---
title: "GetCustomData Method (IAttributeDefinition)"
project: ""
interface: "IAttributeDefinition"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~GetCustomData.html"
---

# GetCustomData Method (IAttributeDefinition)

Gets the specified custom data for the BlockAttribute definition.

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

[IAttributeDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition.html)
[IAttributeDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition_members.html)
[IAttributeDefinition::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~DeleteCustomData.html)
[IAttributeDefinition::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~SetCustomData.html)
[IAttributeDefinition::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~Handle.html)

## Availability

DraftSight V1R1.2
