---
title: "GetCustomData Method (IRichLine)"
project: ""
interface: "IRichLine"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLine~GetCustomData.html"
---

# GetCustomData Method (IRichLine)

Gets the specified custom data for the RichLine.

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

[IRichLine Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLine.html)
[IRichLine Members](Interop.dsAutomation~Interop.dsAutomation.IRichLine_members.html)
[IRichLine::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRichLine~DeleteCustomData.html)
[IRichLine::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRichLine~SetCustomData.html)
[IRichLine::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IRichLine~Handle.html)

## Availability

DraftSight V1R1.2
