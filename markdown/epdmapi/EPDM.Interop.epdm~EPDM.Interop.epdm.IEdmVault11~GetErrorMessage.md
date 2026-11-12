---
title: "GetErrorMessage Method (IEdmVault11)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault11"
member: "GetErrorMessage"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~GetErrorMessage.html"
---

# GetErrorMessage Method (IEdmVault11)

Gets a description for the specified error code.

## Syntax

### Visual Basic

```vb
Function GetErrorMessage( _
   ByVal lHRESULT As System.Integer _
) As System.String
```

### C#

```csharp
System.string GetErrorMessage(
   System.int lHRESULT
)
```

### C++/CLI

```cpp
System.String^ GetErrorMessage(
   System.int lHRESULT
)
```

### Parameters

- `lHRESULT`: Error code for which to get a description

### Return Value

Description of the error code

## Examples

[Add Items (C#)](Add_Items_Example_CSharp.htm)
[Add Items (VB.NET)](Add_Items_Example_VBNET.htm)
[Add Users (C#)](Add_Users_Example_CSharp.htm)
[Add Users (VB.NET)](Add_Users_Example_VBNET.htm)

## Remarks

This method returns a readable error message for HRESULT error codes. For example, if lHRESULT is 0x80040204, then this method returns "You have not logged in to the file vault."

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVault11 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11.html)
[IEdmVault11 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11_members.html)
[IEdmVault11::GetErrorName Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~GetErrorName.html)

## Availability

SOLIDWORKS PDM Professional 2010
