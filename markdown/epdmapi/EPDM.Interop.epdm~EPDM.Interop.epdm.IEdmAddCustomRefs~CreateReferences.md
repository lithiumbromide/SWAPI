---
title: "CreateReferences Method (IEdmAddCustomRefs)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddCustomRefs"
member: "CreateReferences"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~CreateReferences.html"
---

# CreateReferences Method (IEdmAddCustomRefs)

Creates the custom file references in the file vault.

## Syntax

### Visual Basic

```vb
Function CreateReferences() As System.Boolean
```

### C#

```csharp
System.bool CreateReferences()
```

### C++/CLI

```cpp
System.bool CreateReferences();
```

### Return Value

True if any file was created, false if no files were created

## Examples

[Add Custom File Reference (VB.NET)](Add_Custom_File_Reference_Example_VBNET.htm)
[Add Custom File Reference (C#)](Add_Custom_File_Reference_Example_CSharp.htm)

## Remarks

Before calling this method, you must call one of the following methods to add a file reference to another file:

- [IEdmAddCustomRefs::AddReferencesClipboard](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~AddReferencesClipboard.html)
- [IEdmAddCustomRefs2::AddReferencesID2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs2~AddReferencesID2.html)
- [IEdmAddCustomRefs2::AddReferencesPath2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs2~AddReferencesPath2.html)

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmAddCustomRefs Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs.html)
[IEdmAddCustomRefs Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
