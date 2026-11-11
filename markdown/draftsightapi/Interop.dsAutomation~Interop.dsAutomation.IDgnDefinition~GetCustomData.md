---
title: "GetCustomData Method (IDgnDefinition)"
project: ""
interface: "IDgnDefinition"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~GetCustomData.html"
---

# GetCustomData Method (IDgnDefinition)

Gets the specified custom data for the DGN definition.

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

[IDgnDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition.html)
[IDgnDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition_members.html)
[IDgnDefinition::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~DeleteCustomData.html)
[IDgnDefinition::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~SetCustomData.html)
[IDgnDefinition::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~Handle.html)

## Availability

DraftSight 2020 SP0
