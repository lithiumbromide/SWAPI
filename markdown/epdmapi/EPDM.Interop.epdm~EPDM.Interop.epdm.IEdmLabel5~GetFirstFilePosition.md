---
title: "GetFirstFilePosition Method (IEdmLabel5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmLabel5"
member: "GetFirstFilePosition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetFirstFilePosition.html"
---

# GetFirstFilePosition Method (IEdmLabel5)

Starts an enumeration of the files set with this label.

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

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first file set with this label

## Remarks

After calling this method, pass the returned first file position to [IEdmLabel5::GetNextFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetNextFile.html) or [IEdmLabel5::GetNextFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetNextFileID.html) to get the first file in the list of files set with this label. Then call IEdmLabel5::GetNextFile or IEdmLabel5::GetNextFileID repeatedly to get the rest of the files set with this label.

C++ programmers not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmLabel5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5.html)
[IEdmLabel5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
