---
title: "DeleteCustomData Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~DeleteCustomData.html"
---

# DeleteCustomData Method (IPolyLine)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the 2D PolyLine.

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

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetCustomData.html)
[IPolyLine::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetCustomData.html)
[IPolyLine::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Handle.html)

## Availability

DraftSight V1R1.2
