---
title: "GetCustomData Method (ILayer)"
project: ""
interface: "ILayer"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~GetCustomData.html"
---

# GetCustomData Method (ILayer)

Gets the specified custom data for the Layer.

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

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ILayer~DeleteCustomData.html)
[ILayer::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ILayer~SetCustomData.html)
[ILayer::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ILayer~Handle.html)

## Availability

DraftSight V1R1.2
