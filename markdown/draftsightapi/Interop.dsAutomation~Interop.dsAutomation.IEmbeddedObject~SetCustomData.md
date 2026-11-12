---
title: "SetCustomData Method (IEmbeddedObject)"
project: ""
interface: "IEmbeddedObject"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~SetCustomData.html"
---

# SetCustomData Method (IEmbeddedObject)

Sets the custom data for the embedded object.

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

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to get the names of the document's existing custom data.

## See Also

[IEmbeddedObject Interface](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject.html)
[IEmbeddedObject Members](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject_members.html)
[IEmbeddedObject::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~DeleteCustomData.html)
[IEmbeddedObject::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~GetCustomData.html)
[IEmbeddedObject::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~Handle.html)

## Availability

DraftSight V1R1.4
