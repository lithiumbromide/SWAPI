---
title: "GetCustomData Method (ITextStyle)"
project: ""
interface: "ITextStyle"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITextStyle~GetCustomData.html"
---

# GetCustomData Method (ITextStyle)

Gets the specified custom data for the TextStyle.

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

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to discover what custom data names are in use.

## See Also

[ITextStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html)
[ITextStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITextStyle_members.html)
[ITextStyle::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ITextStyle~DeleteCustomData.html)
[ITextStyle::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ITextStyle~SetCustomData.html)
[ITextStyle::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ITextStyle~Handle.html)

## Availability

DraftSight V1R1.2
