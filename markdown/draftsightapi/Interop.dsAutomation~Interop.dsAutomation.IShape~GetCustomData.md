---
title: "GetCustomData Method (IShape)"
project: ""
interface: "IShape"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IShape~GetCustomData.html"
---

# GetCustomData Method (IShape)

Gets the specified custom data for the shape.

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

[IShape Interface](Interop.dsAutomation~Interop.dsAutomation.IShape.html)
[IShape Members](Interop.dsAutomation~Interop.dsAutomation.IShape_members.html)
[IShape::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IShape~DeleteCustomData.html)
[IShape::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IShape~SetCustomData.html)
[IShape::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IShape~Handle.html)

## Availability

DraftSight V1R4.0
