---
title: "GetAddInInfo Method (IEdmAddInMgr5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddInMgr5"
member: "GetAddInInfo"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr5~GetAddInInfo.html"
---

# GetAddInInfo Method (IEdmAddInMgr5)

Obsolete. Superseded by [IEdmAddInMgr6::GetAddInInfo2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr6~GetAddInInfo2.html).

## Syntax

### Visual Basic

```vb
Sub GetAddInInfo( _
   ByVal bsPath As System.String, _
   ByRef poReserved As System.Object, _
   ByRef poInfo As EdmAddInInfo _
)
```

### C#

```csharp
void GetAddInInfo(
   System.string bsPath,
   ref System.object poReserved,
   out EdmAddInInfo poInfo
)
```

### C++/CLI

```cpp
void GetAddInInfo(
   System.String^ bsPath,
   System.Object^% poReserved,
   [Out] EdmAddInInfo poInfo
)
```

### Parameters

- `bsPath`: Path to the DLL about which to get information
- `poReserved`: Null only
- `poInfo`: [EdmAddInInfo structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo.html); returned add-in information

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmAddInMgr5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr5.html)
[IEdmAddInMgr5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr5_members.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
