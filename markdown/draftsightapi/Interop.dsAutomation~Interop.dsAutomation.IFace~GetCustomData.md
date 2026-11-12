---
title: "GetCustomData Method (IFace)"
project: ""
interface: "IFace"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IFace~GetCustomData.html"
---

# GetCustomData Method (IFace)

Gets the specified custom data for the Face.

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

[IFace Interface](Interop.dsAutomation~Interop.dsAutomation.IFace.html)
[IFace Members](Interop.dsAutomation~Interop.dsAutomation.IFace_members.html)
[IFace::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IFace~DeleteCustomData.html)
[IFace::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IFace~SetCustomData.html)
[IFace::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IFace~Handle.html)

## Availability

DraftSight V1R1.3
