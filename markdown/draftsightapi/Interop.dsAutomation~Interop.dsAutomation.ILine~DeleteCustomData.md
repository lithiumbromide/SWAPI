---
title: "DeleteCustomData Method (ILine)"
project: ""
interface: "ILine"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILine~DeleteCustomData.html"
---

# DeleteCustomData Method (ILine)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the Line.

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

[ILine Interface](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
[ILine Members](Interop.dsAutomation~Interop.dsAutomation.ILine_members.html)
[ILine::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ILine~GetCustomData.html)
[ILine::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ILine~SetCustomData.html)
[ILine::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ILine~Handle.html)

## Availability

DraftSight V1R1.2
