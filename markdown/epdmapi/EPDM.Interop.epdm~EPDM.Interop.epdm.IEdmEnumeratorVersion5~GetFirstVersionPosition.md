---
title: "GetFirstVersionPosition Method (IEdmEnumeratorVersion5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVersion5"
member: "GetFirstVersionPosition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetFirstVersionPosition.html"
---

# GetFirstVersionPosition Method (IEdmEnumeratorVersion5)

Starts an enumeration of the versions of this file.

## Syntax

### Visual Basic

```vb
Function GetFirstVersionPosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstVersionPosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstVersionPosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first version of this file

## Examples

[Get File Version Information (C#)](Get_File_Version_Information_Example_CSharp.htm)
[Get File Version Information (VB.NET)](Get_File_Version_Information_Example_VBNET.htm)

## Remarks

After calling this method, pass the returned first version position to [IEdmEnumeratorVersion5::GetNextVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetNextVersion.html) to get the first version. Then call IEdmEnumeratorVersion5::GetNextVersion to get the rest of the versions of this file.

C++ programmers not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: An argument is invalid.

## See Also

[IEdmEnumeratorVersion5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5.html)
[IEdmEnumeratorVersion5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
