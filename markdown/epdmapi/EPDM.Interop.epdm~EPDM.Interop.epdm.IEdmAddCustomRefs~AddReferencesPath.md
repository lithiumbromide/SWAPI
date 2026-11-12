---
title: "AddReferencesPath Method (IEdmAddCustomRefs)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddCustomRefs"
member: "AddReferencesPath"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~AddReferencesPath.html"
---

# AddReferencesPath Method (IEdmAddCustomRefs)

Obsolete. Superseded by [IEdmAddCustomRefs2::AddReferencesPath2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs2~AddReferencesPath2.html).

## Syntax

### Visual Basic

```vb
Sub AddReferencesPath( _
   ByVal lRootFile As System.Integer, _
   ByRef ppoReferences() As System.String _
)
```

### C#

```csharp
void AddReferencesPath(
   System.int lRootFile,
   ref System.string[] ppoReferences
)
```

### C++/CLI

```cpp
void AddReferencesPath(
   System.int lRootFile,
   System.array<String^>^% ppoReferences
)
```

### Parameters

- `lRootFile`: ID of file to which to add file references
- `ppoReferences`: Array of paths to reference files to add to lRootFile

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmAddCustomRefs Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs.html)
[IEdmAddCustomRefs Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
