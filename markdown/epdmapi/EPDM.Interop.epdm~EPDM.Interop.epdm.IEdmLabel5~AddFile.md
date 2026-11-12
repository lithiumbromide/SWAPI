---
title: "AddFile Method (IEdmLabel5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmLabel5"
member: "AddFile"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~AddFile.html"
---

# AddFile Method (IEdmLabel5)

Sets this label on the latest version of the specified file.

## Syntax

### Visual Basic

```vb
Sub AddFile( _
   ByVal lFileID As System.Integer _
)
```

### C#

```csharp
void AddFile(
   System.int lFileID
)
```

### C++/CLI

```cpp
void AddFile(
   System.int lFileID
)
```

### Parameters

- `lFileID`: ID of file to set label on

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmLabel5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5.html)
[IEdmLabel5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
