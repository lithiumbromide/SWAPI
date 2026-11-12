---
title: "GetFirstRevisionPosition Method (IEdmVersion5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVersion5"
member: "GetFirstRevisionPosition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5~GetFirstRevisionPosition.html"
---

# GetFirstRevisionPosition Method (IEdmVersion5)

Starts an enumeration of the revisions of this version.

## Syntax

### Visual Basic

```vb
Function GetFirstRevisionPosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstRevisionPosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstRevisionPosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first revision in the enumeration

## Examples

[Get Revision Names for Local Version of File (C#)](Get_Revision_Names_for_Local_Version_of_File_Example_CSharp.htm)
[Get Revision Names for Local Version of File (VB.NET)](Get_Revision_Names_for_Local_Version_of_File_Example_VBNET.htm)

## Remarks

After calling this method, pass the returned position of the first revision to [IEdmVersion5::GetNextRevision](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5~GetNextRevision.html) to get the first revision in this list. Then call IEdmVersion5::GetNextRevision repeatedly to get the rest of the revisions.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVersion5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5.html)
[IEdmVersion5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5_members.html)
[IEdmRevision5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision5.html)
[IEdmEnumeratorVersion5::GetFirstRevisionPosition Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetFirstRevisionPosition.html)
[IEdmVersion5::HasRevision Property ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5~HasRevision.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
