---
title: "GetCustomData Method (ILineStyle)"
project: ""
interface: "ILineStyle"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILineStyle~GetCustomData.html"
---

# GetCustomData Method (ILineStyle)

Gets the specified custom data for the simple LineStyle.

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

[ILineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html)
[ILineStyle Members](Interop.dsAutomation~Interop.dsAutomation.ILineStyle_members.html)
[ILineStyle::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyle~DeleteCustomData.html)
[ILineStyle::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyle~SetCustomData.html)
[ILineStyle::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyle~Handle.html)

## Availability

DraftSight V1R4.0
