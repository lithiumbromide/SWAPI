---
title: "GetCustomData Method (ILine)"
project: ""
interface: "ILine"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILine~GetCustomData.html"
---

# GetCustomData Method (ILine)

Gets the specified custom data for the Line.

## Syntax

### Visual Basic

```vb
Function GetCustomData( _
   ByVal ApplicationName As System.String _
) As CustomData
```

### C#

```csharp
CustomData GetCustomData(
   System.string ApplicationName
)
```

### JScript

```
function GetCustomData(
   ApplicationName : System.String
) : CustomData;
```

### Managed Extensions for C++

```
CustomData* GetCustomData(
   System.string* ApplicationName
)
```

### C++/CLI

```cpp
CustomData^ GetCustomData(
   System.String^ ApplicationName
)
```

### Parameters

- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)

### Return Value

[Custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[ILine Interface](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
[ILine Members](Interop.dsAutomation~Interop.dsAutomation.ILine_members.html)
[ILine::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ILine~DeleteCustomData.html)
[ILine::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ILine~SetCustomData.html)
[ILine::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ILine~Handle.html)

## Availability

DraftSight V1R1.2
