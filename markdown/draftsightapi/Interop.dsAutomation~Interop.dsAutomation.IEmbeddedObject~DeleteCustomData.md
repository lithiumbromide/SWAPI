---
title: "DeleteCustomData Method (IEmbeddedObject)"
project: ""
interface: "IEmbeddedObject"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~DeleteCustomData.html"
---

# DeleteCustomData Method (IEmbeddedObject)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the embedded object.

## Syntax

### Visual Basic

```vb
Sub DeleteCustomData( _
   ByVal ApplicationName As System.String _
)
```

### C#

```csharp
void DeleteCustomData(
   System.string ApplicationName
)
```

### JScript

```
function DeleteCustomData(
   ApplicationName : System.String
);
```

### Managed Extensions for C++

```
void DeleteCustomData(
   System.string* ApplicationName
)
```

### C++/CLI

```cpp
void DeleteCustomData(
   System.String^ ApplicationName
)
```

### Parameters

- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to get the names of the document's existing custom data.

## See Also

[IEmbeddedObject Interface](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject.html)
[IEmbeddedObject Members](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject_members.html)
[IEmbeddedObject::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~GetCustomData.html)
[IEmbeddedObject::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~SetCustomData.html)
[IEmbeddedObject::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~Handle.html)

## Availability

DraftSight V1R1.4
