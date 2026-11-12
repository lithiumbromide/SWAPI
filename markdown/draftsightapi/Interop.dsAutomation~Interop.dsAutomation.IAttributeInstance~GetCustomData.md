---
title: "GetCustomData Method (IAttributeInstance)"
project: ""
interface: "IAttributeInstance"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~GetCustomData.html"
---

# GetCustomData Method (IAttributeInstance)

Gets the specified custom data for the BlockAttribute instance.

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

[IAttributeInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance.html)
[IAttributeInstance Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance_members.html)
[IAttributeInstance::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~DeleteCustomData.html)
[IAttributeInstance::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~SetCustomData.html)
[IAttributeInstance::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~Handle.html)

## Availability

DraftSight V1R1.2
