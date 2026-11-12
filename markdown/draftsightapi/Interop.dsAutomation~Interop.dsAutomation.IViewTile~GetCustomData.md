---
title: "GetCustomData Method (IViewTile)"
project: ""
interface: "IViewTile"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewTile~GetCustomData.html"
---

# GetCustomData Method (IViewTile)

Gets the specified custom data for this ViewTile.

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

[IViewTile Interface](Interop.dsAutomation~Interop.dsAutomation.IViewTile.html)
[IViewTile Members](Interop.dsAutomation~Interop.dsAutomation.IViewTile_members.html)
[IViewTile::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewTile~DeleteCustomData.html)
[IViewTile::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewTile~SetCustomData.html)
[IViewTile::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IViewTile~Handle.html)

## Availability

DraftSight V1R6.0
