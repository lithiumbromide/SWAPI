---
title: "GetCustomData Method (IRay)"
project: ""
interface: "IRay"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRay~GetCustomData.html"
---

# GetCustomData Method (IRay)

Gets the specified custom data for the Ray.

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

[IRay Interface](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
[IRay Members](Interop.dsAutomation~Interop.dsAutomation.IRay_members.html)
[IRay::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRay~DeleteCustomData.html)
[IRay::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRay~SetCustomData.html)
[IRay::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IRay~Handle.html)

## Availability

DraftSight V1R1.2
