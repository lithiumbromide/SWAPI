---
title: "GetCustomData Method (IDimensionStyle)"
project: ""
interface: "IDimensionStyle"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetCustomData.html"
---

# GetCustomData Method (IDimensionStyle)

Gets the specified custom data for the DimensionStyle.

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

[IDimensionStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html)
[IDimensionStyle Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle_members.html)
[IDimensionStyle::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~DeleteCustomData.html)
[IDimensionStyle::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~SetCustomData.html)
[IDimensionStyle::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~Handle.html)

## Availability

DraftSight V1R1.2
