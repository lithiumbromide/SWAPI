---
title: "GetCustomData Method (IBlockInstance)"
project: ""
interface: "IBlockInstance"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~GetCustomData.html"
---

# GetCustomData Method (IBlockInstance)

Gets the specified custom data for the Block instance.

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

[IBlockInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)
[IBlockInstance Members](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance_members.html)
[IBlockInstance::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~DeleteCustomData.html)
[IBlockInstance::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~SetCustomData.html)
[IBlockInstance::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~Handle.html)

## Availability

DraftSight V1R1.2
