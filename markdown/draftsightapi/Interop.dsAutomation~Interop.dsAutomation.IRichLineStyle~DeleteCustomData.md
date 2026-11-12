---
title: "DeleteCustomData Method (IRichLineStyle)"
project: ""
interface: "IRichLineStyle"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~DeleteCustomData.html"
---

# DeleteCustomData Method (IRichLineStyle)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the RichLineStyle.

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

[IRichLineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle.html)
[IRichLineStyle Members](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle_members.html)
[IRichLineStyle::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~GetCustomData.html)
[IRichLineStyle::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~SetCustomData.html)
[IRichLineStyle::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~Handle.html)

## Availability

DraftSight V1R1.2
