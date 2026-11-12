---
title: "AddFile Method (IEdmHistory)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmHistory"
member: "AddFile"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory~AddFile.html"
---

# AddFile Method (IEdmHistory)

Adds a file to the history listing.

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

- `lFileID`: ID of file to add

## Examples

See the [IEdmHistory](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmHistory Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory.html)
[IEdmHistory Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.4
