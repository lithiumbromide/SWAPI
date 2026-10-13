---
title: "GetVersion Method (IEdmEnumeratorVersion5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVersion5"
member: "GetVersion"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetVersion.html"
---

# GetVersion Method (IEdmEnumeratorVersion5)

Gets a version object with the specified version number.

## Syntax

### Visual Basic

```vb
Function GetVersion( _
   ByVal lVersionNo As System.Integer _
) As IEdmVersion5
```

### C#

```csharp
IEdmVersion5 GetVersion(
   System.int lVersionNo
)
```

### C++/CLI

```cpp
IEdmVersion5^ GetVersion(
   System.int lVersionNo
)
```

### Parameters

- `lVersionNo`: Number of version to get

### Return Value

[IEdmVersion5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5.html)

## Examples

[Get Revision Names for Local Version of File (C#)](Get_Revision_Names_for_Local_Version_of_File_Example_CSharp.htm)
[Get Revision Names for Local Version of File (VB.NET)](Get_Revision_Names_for_Local_Version_of_File_Example_VBNET.htm)

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_INVALID_REVISION_NUMBER: The version number is invalid.

## See Also

[IEdmEnumeratorVersion5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5.html)
[IEdmEnumeratorVersion5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
