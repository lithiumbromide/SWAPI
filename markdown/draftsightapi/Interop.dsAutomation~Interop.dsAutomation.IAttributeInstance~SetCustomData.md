---
title: "SetCustomData Method (IAttributeInstance)"
project: ""
interface: "IAttributeInstance"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~SetCustomData.html"
---

# SetCustomData Method (IAttributeInstance)

Sets the custom data for the BlockAttribute instance.

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

[IAttributeInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance.html)
[IAttributeInstance Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance_members.html)
[IAttributeInstance::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~DeleteCustomData.html)
[IAttributeInstance::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~GetCustomData.html)
[IAttributeInstance::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~Handle.html)

## Availability

DraftSight V1R1.2
