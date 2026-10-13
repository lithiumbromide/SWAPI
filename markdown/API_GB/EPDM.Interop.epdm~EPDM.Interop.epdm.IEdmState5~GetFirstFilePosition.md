---
title: "GetFirstFilePosition Method (IEdmState5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmState5"
member: "GetFirstFilePosition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5~GetFirstFilePosition.html"
---

# GetFirstFilePosition Method (IEdmState5)

Starts an enumeration of all the files in this workflow state.

## Syntax

### Visual Basic

```vb
Function GetFirstFilePosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstFilePosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstFilePosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position in the list of the first file in this workflow state (see **Remarks**)

## Examples

[Get Files in Workflow State (VB.NET)](Get_Files_in_State_Example_VBNET.htm)
[Get Files in Workflow State (C#)](Get_Files_in_State_Example_CSharp.htm)

## Remarks

After calling this method, pass the returned position of the first file in this workflow state to [IEdmState5::GetNextFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5~GetNextFile.html) to get the first file in this workflow state. Then call IEdmState5::GetNextFile repeatedly to get the rest of the files in this workflow state.

C++ programmers not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

Use [IEdmSearch5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5.html) to perform more elaborate searches.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmState5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5.html)
[IEdmState5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
