---
title: "GetAddInInfo2 Method (IEdmAddInMgr6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddInMgr6"
member: "GetAddInInfo2"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr6~GetAddInInfo2.html"
---

# GetAddInInfo2 Method (IEdmAddInMgr6)

Gets information about an add-in.

## Syntax

### Visual Basic

```vb
Sub GetAddInInfo2( _
   ByVal bsPath As System.String, _
   ByVal oReserved As System.Object, _
   ByRef poInfo As EdmAddInInfo2 _
)
```

### C#

```csharp
void GetAddInInfo2(
   System.string bsPath,
   System.object oReserved,
   out EdmAddInInfo2 poInfo
)
```

### C++/CLI

```cpp
void GetAddInInfo2(
   System.String^ bsPath,
   System.Object^ oReserved,
   [Out] EdmAddInInfo2 poInfo
)
```

### Parameters

- `bsPath`: Path to the DLL about which to get information
- `oReserved`: Must be empty
- `poInfo`: [EdmAddInInfo2 structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo2.html); returned add-in information

## Examples

See the [IEdmAddInMgr5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr5.html) examples.

## Remarks

This method supersedes [IEdmAddInMgr5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr5~GetAddInInfo.html) which returned less information about the add-in.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmAddInMgr6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr6.html)
[IEdmAddInMgr6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr6_members.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
