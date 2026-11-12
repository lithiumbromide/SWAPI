---
title: "DeleteCustomData Method (IRichLine)"
project: ""
interface: "IRichLine"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLine~DeleteCustomData.html"
---

# DeleteCustomData Method (IRichLine)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the RichLine.

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

[IRichLine Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLine.html)
[IRichLine Members](Interop.dsAutomation~Interop.dsAutomation.IRichLine_members.html)
[IRichLine::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRichLine~GetCustomData.html)
[IRichLine::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRichLine~SetCustomData.html)
[IRichLine::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IRichLine~Handle.html)

## Availability

DraftSight V1R1.2
