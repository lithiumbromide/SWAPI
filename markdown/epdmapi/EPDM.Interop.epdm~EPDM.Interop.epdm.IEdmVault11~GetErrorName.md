---
title: "GetErrorName Method (IEdmVault11)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault11"
member: "GetErrorName"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~GetErrorName.html"
---

# GetErrorName Method (IEdmVault11)

Gets an internal error code name for the specified error code.

## Syntax

### Visual Basic

```vb
Function GetErrorName( _
   ByVal lHRESULT As System.Integer _
) As System.String
```

### C#

```csharp
System.string GetErrorName(
   System.int lHRESULT
)
```

### C++/CLI

```cpp
System.String^ GetErrorName(
   System.int lHRESULT
)
```

### Parameters

- `lHRESULT`: Error code for which to get the internal name

### Return Value

Internal error code name

## Examples

[Get and Set Item References (C#)](Get_and_Set_Item_References_Example_CSharp.htm)
[Get and Set Item References (VB.NET)](Get_and_Set_Item_References_Example_VBNET.htm)

## Remarks

This method returns the internal error code name for an HRESULT error code. For example, if lHRESULT is 0x80040204, this method returns "E_EDM_NOT_LOGGED_IN".

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVault11 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11.html)
[IEdmVault11 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11_members.html)
[IEdmVault11::GetErrorMessage Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~GetErrorMessage.html)

## Availability

SOLIDWORKS PDM Professional 2010
