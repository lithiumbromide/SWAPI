---
title: "DeleteCustomData Method (ITextStyle)"
project: ""
interface: "ITextStyle"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITextStyle~DeleteCustomData.html"
---

# DeleteCustomData Method (ITextStyle)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the TextStyle.

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

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to discover what custom data names are in use.

## See Also

[ITextStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html)
[ITextStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITextStyle_members.html)
[ITextStyle::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ITextStyle~GetCustomData.html)
[ITextStyle::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ITextStyle~SetCustomData.html)
[ITextStyle::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ITextStyle~Handle.html)

## Availability

DraftSight V1R1.2
