---
title: "SetCustomData Method (IEdmReference5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmReference5"
member: "SetCustomData"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~SetCustomData.html"
---

# SetCustomData Method (IEdmReference5)

Stores an arbitrary piece of data in this object.

## Syntax

### Visual Basic

```vb
Sub SetCustomData( _
   ByVal lDataID As System.Integer, _
   ByRef poData As System.Object _
)
```

### C#

```csharp
void SetCustomData(
   System.int lDataID,
   ref System.object poData
)
```

### C++/CLI

```cpp
void SetCustomData(
   System.int lDataID,
   System.Object^% poData
)
```

### Parameters

- `lDataID`: User-defined ID of data to store
- `poData`: Data to store

## Remarks

The data is only stored in memory and is kept as long as [IEdmReference5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5.html) is add-referenced. You can get the stored data by calling [IEdmReference5::GetCustomData](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~GetCustomData.html).

[Return code](ReturnCodes.htm) S_OK indicates that the method successfully executed.

## See Also

[IEdmReference5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5.html)
[IEdmReference5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5_members.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional
