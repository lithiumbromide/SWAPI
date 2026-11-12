---
title: "DeleteCustomData Method (IDgnReference)"
project: ""
interface: "IDgnReference"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDgnReference~DeleteCustomData.html"
---

# DeleteCustomData Method (IDgnReference)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the DGN reference.

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

[IDgnReference Interface](Interop.dsAutomation~Interop.dsAutomation.IDgnReference.html)
[IDgnReference Members](Interop.dsAutomation~Interop.dsAutomation.IDgnReference_members.html)
[IDgnReference::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~GetCustomData.html)
[IDgnReference::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~SetCustomData.html)
[IDgnReference::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~Handle.html)

## Availability

DraftSight 2020 SP0
