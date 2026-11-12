---
title: "GetCustomData Method (IEdmReference5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmReference5"
member: "GetCustomData"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~GetCustomData.html"
---

# GetCustomData Method (IEdmReference5)

Gets data stored with [IEdmReference5::SetCustomData](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~SetCustomData.html) in this file reference.

## Syntax

### Visual Basic

```vb
Function GetCustomData( _
   ByVal lDataID As System.Integer, _
   ByRef poData As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool GetCustomData(
   System.int lDataID,
   out System.object poData
)
```

### C++/CLI

```cpp
System.bool GetCustomData(
   System.int lDataID,
   [Out] System.Object^ poData
)
```

### Parameters

- `lDataID`: User-defined ID of data to get
- `poData`: Buffer in which to return data

### Return Value

True if the data was found, false if not

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: The data was not found (pbFoundlt returned false).

## See Also

[IEdmReference5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5.html)
[IEdmReference5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5_members.html)
[IEdmReference5::SetCustomData Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~SetCustomData.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional
