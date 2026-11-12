---
title: "GetNextRevision Method (IEdmVersion5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVersion5"
member: "GetNextRevision"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5~GetNextRevision.html"
---

# GetNextRevision Method (IEdmVersion5)

Gets the next revision set on this version in an enumeration.

## Syntax

### Visual Basic

```vb
Function GetNextRevision( _
   ByVal poPos As IEdmPos5 _
) As IEdmRevision5
```

### C#

```csharp
IEdmRevision5 GetNextRevision(
   IEdmPos5 poPos
)
```

### C++/CLI

```cpp
IEdmRevision5^ GetNextRevision(
   IEdmPos5^ poPos
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next revision in the list

### Return Value

[IEdmRevision5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision5.html)

## Examples

[Get Revision Names for Local Version of File (C#)](Get_Revision_Names_for_Local_Version_of_File_Example_CSharp.htm)
[Get Revision Names for Local Version of File (VB.NET)](Get_Revision_Names_for_Local_Version_of_File_Example_VBNET.htm)

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first revision in the list, IEdmPos5. Call [IEdmVersion5::GetFirstRevisionPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5~GetFirstRevisionPosition.html) to obtain poPos.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the revisions in the list.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmRevision5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVersion5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5.html)
[IEdmVersion5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5_members.html)
[IEdmVersion5::HasRevision Property ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5~HasRevision.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
