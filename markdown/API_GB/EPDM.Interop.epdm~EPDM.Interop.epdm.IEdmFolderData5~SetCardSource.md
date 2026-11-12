---
title: "SetCardSource Method (IEdmFolderData5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolderData5"
member: "SetCardSource"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolderData5~SetCardSource.html"
---

# SetCardSource Method (IEdmFolderData5)

Sets the specified file card ID to use for the specified file extensions.

## Syntax

### Visual Basic

```vb
Sub SetCardSource( _
   ByVal lCardID As System.Integer, _
   Optional ByVal bsExtensions As System.String _
)
```

### C#

```csharp
void SetCardSource(
   System.int lCardID,
   System.string bsExtensions
)
```

### C++/CLI

```cpp
void SetCardSource(
   System.int lCardID,
   System.String^ bsExtensions
)
```

### Parameters

- `lCardID`: ID of card to use
- `bsExtensions`: Semicolon-delimited list of extensions; e.g., "DOC;XLS"

## Examples

See the [IEdmFolderData5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolderData5.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmFolderData5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolderData5.html)
[IEdmFolderData5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolderData5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
