---
title: "GetReferences Method (IEdmRawReferenceMgr)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRawReferenceMgr"
member: "GetReferences"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRawReferenceMgr~GetReferences.html"
---

# GetReferences Method (IEdmRawReferenceMgr)

Get a list of all of the file references in the opened file.

## Syntax

### Visual Basic

```vb
Sub GetReferences( _
   ByRef ppoReferences As EdmRawReference() _
)
```

### C#

```csharp
void GetReferences(
   out EdmRawReference[] ppoReferences
)
```

### C++/CLI

```cpp
void GetReferences(
   [Out] array<EdmRawReference> ppoReferences
)
```

### Parameters

- `ppoReferences`: Array of [EdmRawReference](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRawReference.html) structs of the file references

## Examples

See the [IEdmRawReferenceMgr](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRawReferenceMgr.html) examples.

## Remarks

Before calling this method, you must call [IEdmRawReferenceMgr::Open](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRawReferenceMgr~Open.html).

[Return code](ReturnCodes.htm) S_OK indicates that the method successfully executed.

## See Also

[IEdmRawReferenceMgr Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRawReferenceMgr.html)
[IEdmRawReferenceMgr Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRawReferenceMgr_members.html)
[IEdmRawReferenceMgr::UpdateReferences Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRawReferenceMgr~UpdateReferences.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
