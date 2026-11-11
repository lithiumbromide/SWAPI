---
title: "GetCustomData Method (IRegion)"
project: ""
interface: "IRegion"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRegion~GetCustomData.html"
---

# GetCustomData Method (IRegion)

Gets the specified custom data for the Region.

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

[IRegion Interface](Interop.dsAutomation~Interop.dsAutomation.IRegion.html)
[IRegion Members](Interop.dsAutomation~Interop.dsAutomation.IRegion_members.html)
[IRegion::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRegion~DeleteCustomData.html)
[IRegion::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRegion~SetCustomData.html)
[IRegion::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IRegion~Handle.html)

## Availability

DraftSight V1R2.0
