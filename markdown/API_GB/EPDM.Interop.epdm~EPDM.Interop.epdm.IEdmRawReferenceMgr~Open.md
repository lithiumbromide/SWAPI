---
title: "Open Method (IEdmRawReferenceMgr)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRawReferenceMgr"
member: "Open"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRawReferenceMgr~Open.html"
---

# Open Method (IEdmRawReferenceMgr)

Opens a file.

## Syntax

### Visual Basic

```vb
Function Open( _
   ByVal bsPath As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool Open(
   System.string bsPath
)
```

### C++/CLI

```cpp
System.bool Open(
   System.String^ bsPath
)
```

### Parameters

- `bsPath`: Path to the file to open

### Return Value

True if the file's format supports file references, false if not

## Examples

See the [IEdmRawReferenceMgr](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRawReferenceMgr.html) examples.

## Remarks

You must call this method before you call any of the other methods in this interface.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: The file's format does not support file references.

## See Also

[IEdmRawReferenceMgr Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRawReferenceMgr.html)
[IEdmRawReferenceMgr Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRawReferenceMgr_members.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
