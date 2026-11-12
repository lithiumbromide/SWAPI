---
title: "DeleteCustomData Method (ISheet)"
project: ""
interface: "ISheet"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISheet~DeleteCustomData.html"
---

# DeleteCustomData Method (ISheet)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the Sheet.

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

[ISheet Interface](Interop.dsAutomation~Interop.dsAutomation.ISheet.html)
[ISheet Members](Interop.dsAutomation~Interop.dsAutomation.ISheet_members.html)
[ISheet::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ISheet~GetCustomData.html)
[ISheet::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ISheet~SetCustomData.html)
[ISheet::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ISheet~Handle.html)

## Availability

DraftSight V1R1.2
