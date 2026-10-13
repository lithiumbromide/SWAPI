---
title: "AddReferencesPath2 Method (IEdmAddCustomRefs2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddCustomRefs2"
member: "AddReferencesPath2"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs2~AddReferencesPath2.html"
---

# AddReferencesPath2 Method (IEdmAddCustomRefs2)

Adds file references by file system path and quantity.

## Syntax

### Visual Basic

```vb
Sub AddReferencesPath2( _
   ByVal lRootFile As System.Integer, _
   ByRef ppoReferences() As System.String, _
   ByRef plQuantity() As System.Integer _
)
```

### C#

```csharp
void AddReferencesPath2(
   System.int lRootFile,
   ref System.string[] ppoReferences,
   ref System.int[] plQuantity
)
```

### C++/CLI

```cpp
void AddReferencesPath2(
   System.int lRootFile,
   System.array<String^>^% ppoReferences,
   System.array<int>^% plQuantity
)
```

### Parameters

- `lRootFile`: ID of file to which to add file references
- `ppoReferences`: Array of paths to reference files
- `plQuantity`: Array of times that the files in ppoReferences are referenced in lRootFile

## Remarks

This method supersedes [IEdmAddCustomRefs::AddReferencesPath](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~AddReferencesPath.html), which adds reference files only by file system path.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmAddCustomRefs2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs2.html)
[IEdmAddCustomRefs2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs2_members.html)

## Availability

Version 2013 of SOLIDWORKS PDM Professional
