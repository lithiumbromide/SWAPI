---
title: "DeleteCustomData Method (IPdfReference)"
project: ""
interface: "IPdfReference"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPdfReference~DeleteCustomData.html"
---

# DeleteCustomData Method (IPdfReference)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the PDF reference.

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

[IPdfReference Interface](Interop.dsAutomation~Interop.dsAutomation.IPdfReference.html)
[IPdfReference Members](Interop.dsAutomation~Interop.dsAutomation.IPdfReference_members.html)
[IPdfReference::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~GetCustomData.html)
[IPdfReference::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~SetCustomData.html)
[IPdfReference::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~Handle.html)

## Availability

DraftSight 2020 SP0
