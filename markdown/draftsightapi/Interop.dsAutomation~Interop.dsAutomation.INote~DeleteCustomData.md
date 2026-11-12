---
title: "DeleteCustomData Method (INote)"
project: ""
interface: "INote"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.INote~DeleteCustomData.html"
---

# DeleteCustomData Method (INote)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the Note.

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

[INote Interface](Interop.dsAutomation~Interop.dsAutomation.INote.html)
[INote Members](Interop.dsAutomation~Interop.dsAutomation.INote_members.html)
[INote::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.INote~GetCustomData.html)
[INote::SetPosition Method](Interop.dsAutomation~Interop.dsAutomation.INote~SetPosition.html)
[INote::Handle Property](Interop.dsAutomation~Interop.dsAutomation.INote~Handle.html)

## Availability

DraftSight V1R1.2
