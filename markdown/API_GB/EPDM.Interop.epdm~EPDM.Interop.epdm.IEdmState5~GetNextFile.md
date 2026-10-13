---
title: "GetNextFile Method (IEdmState5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmState5"
member: "GetNextFile"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5~GetNextFile.html"
---

# GetNextFile Method (IEdmState5)

Gets the next file in this workflow state.

## Syntax

### Visual Basic

```vb
Function GetNextFile( _
   ByVal poPosition As IEdmPos5 _
) As IEdmFile5
```

### C#

```csharp
IEdmFile5 GetNextFile(
   IEdmPos5 poPosition
)
```

### C++/CLI

```cpp
IEdmFile5^ GetNextFile(
   IEdmPos5^ poPosition
)
```

### Parameters

- `poPosition`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next file in this workflow state (see **Remarks**)

### Return Value

[IEdmFile5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)

## Examples

[Get Files in Workflow State (VB.NET)](Get_Files_in_State_Example_VBNET.htm)
[Get Files in Workflow State (C#)](Get_Files_in_State_Example_CSharp.htm)

## Remarks

Before calling this method the first time, you must populate poPosition with the interface to the position of the first file, IEdmPos5. Call [IEdmState5::GetFirstFilePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5~GetFirstFilePosition.html) to start an enumeration and obtain IEdmPos5.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the files.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

C++ programmers must free the interface returned, IEdmFile5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: You have gone past the end of the list.

## See Also

[IEdmState5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5.html)
[IEdmState5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
