---
title: "GetCustomData Method (ISheet)"
project: ""
interface: "ISheet"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISheet~GetCustomData.html"
---

# GetCustomData Method (ISheet)

Gets the specified custom data for the Sheet.

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

[ISheet Interface](Interop.dsAutomation~Interop.dsAutomation.ISheet.html)
[ISheet Members](Interop.dsAutomation~Interop.dsAutomation.ISheet_members.html)
[ISheet::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ISheet~DeleteCustomData.html)
[ISheet::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ISheet~SetCustomData.html)
[ISheet::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ISheet~Handle.html)

## Availability

DraftSight V1R1.2
