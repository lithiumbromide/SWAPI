---
title: "UpdateReferences Method (IEdmRawReferenceMgr)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRawReferenceMgr"
member: "UpdateReferences"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRawReferenceMgr~UpdateReferences.html"
---

# UpdateReferences Method (IEdmRawReferenceMgr)

Updates the include paths for the file references.

## Syntax

### Visual Basic

```vb
Sub UpdateReferences( _
   ByVal poReferences() As EdmRawReference _
)
```

### C#

```csharp
void UpdateReferences(
   EdmRawReference[] poReferences
)
```

### C++/CLI

```cpp
void UpdateReferences(
   array<EdmRawReference>^ poReferences
)
```

### Parameters

- `poReferences`: Array of [EdmRawReference](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRawReference.html) structs of the references to update (see **Remarks**)

## Examples

See the [IEdmRawReferenceMgr](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRawReferenceMgr.html) examples.

## Remarks

Use [IEdmRawReferenceMgr::GetReferences](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRawReferenceMgr~GetReferences.html) to get the array of EdmRawReference structs to pass to this method.

[Return code](ReturnCodes.htm) S_OK indicates that the method successfully executed.

## See Also

[IEdmRawReferenceMgr Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRawReferenceMgr.html)
[IEdmRawReferenceMgr Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRawReferenceMgr_members.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
