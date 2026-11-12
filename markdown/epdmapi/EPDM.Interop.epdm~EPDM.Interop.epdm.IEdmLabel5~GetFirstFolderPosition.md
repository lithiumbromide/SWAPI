---
title: "GetFirstFolderPosition Method (IEdmLabel5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmLabel5"
member: "GetFirstFolderPosition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetFirstFolderPosition.html"
---

# GetFirstFolderPosition Method (IEdmLabel5)

Starts an enumeration of the folders set with this label.

## Syntax

### Visual Basic

```vb
Function GetFirstFolderPosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstFolderPosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstFolderPosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first folder set with this label

## Remarks

After calling this method, pass the returned first folder position to [IEdmLabel5::GetNextFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetNextFolder.html) or [IEdmLabel5::GetNextFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetNextFolderID.html) to get the first folder in the list of folders set with this label. Then call IEdmLabel5::GetNextFolder or IEdmLabel5::GetNextFolderID repeatedly to get the rest of the folders set with this label.

C++ programmers not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmLabel5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5.html)
[IEdmLabel5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
