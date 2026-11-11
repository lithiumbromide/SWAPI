---
title: "DeleteCustomData Method (ILayer)"
project: ""
interface: "ILayer"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~DeleteCustomData.html"
---

# DeleteCustomData Method (ILayer)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the Layer.

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

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetCustomData.html)
[ILayer::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ILayer~SetCustomData.html)
[ILayer::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ILayer~Handle.html)

## Availability

DraftSight V1R1.2
