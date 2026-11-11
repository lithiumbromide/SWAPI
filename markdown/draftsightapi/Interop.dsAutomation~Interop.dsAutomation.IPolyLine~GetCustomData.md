---
title: "GetCustomData Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetCustomData.html"
---

# GetCustomData Method (IPolyLine)

Gets the specified custom data for the 2D PolyLine.

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

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~DeleteCustomData.html)
[IPolyLine::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetCustomData.html)
[IPolyLine::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Handle.html)

## Availability

DraftSight V1R1.2
