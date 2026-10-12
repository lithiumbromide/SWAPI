---
title: "GetReferences Method (IEdmBatchListing3)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchListing3"
member: "GetReferences"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing3~GetReferences.html"
---

# GetReferences Method (IEdmBatchListing3)

Gets a list of referenced files.

## Syntax

### Visual Basic

```vb
Sub GetReferences( _
   ByRef ppoReferences() As EdmListRef _
)
```

### C#

```csharp
void GetReferences(
   out EdmListRef[] ppoReferences
)
```

### C++/CLI

```cpp
void GetReferences(
   [Out] array<EdmListRef>^ ppoReferences
)
```

### Parameters

- `ppoReferences`: Array of [EdmListRef](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListRef.html) structures

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchListing3 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing3.html)
[IEdmBatchListing3 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing3_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
