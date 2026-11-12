---
title: "GetCustomData Method (IEmbeddedObject)"
project: ""
interface: "IEmbeddedObject"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~GetCustomData.html"
---

# GetCustomData Method (IEmbeddedObject)

Gets the specified custom data for the embedded object.

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

[ICustomData](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to get the names of the document's existing custom data.

## See Also

[IEmbeddedObject Interface](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject.html)
[IEmbeddedObject Members](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject_members.html)
[IEmbeddedObject::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~DeleteCustomData.html)
[IEmbeddedObject::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~SetCustomData.html)
[IEmbeddedObject::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~Handle.html)

## Availability

DraftSight V1R1.4
