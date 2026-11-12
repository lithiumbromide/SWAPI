---
title: "AddReferencesClipboard Method (IEdmAddCustomRefs)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddCustomRefs"
member: "AddReferencesClipboard"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~AddReferencesClipboard.html"
---

# AddReferencesClipboard Method (IEdmAddCustomRefs)

Adds a file reference that has been copied to the Windows clipboard to another checked-out file.

## Syntax

### Visual Basic

```vb
Sub AddReferencesClipboard( _
   ByVal lRootFile As System.Integer _
)
```

### C#

```csharp
void AddReferencesClipboard(
   System.int lRootFile
)
```

### C++/CLI

```cpp
void AddReferencesClipboard(
   System.int lRootFile
)
```

### Parameters

- `lRootFile`: ID of file to which to add the file reference that is on the Windows clipboard

## Examples

[Add Custom File Reference (VB.NET)](Add_Custom_File_Reference_Example_VBNET.htm)
[Add Custom File Reference (C#)](Add_Custom_File_Reference_Example_CSharp.htm)

## Remarks

This method is valid only after the user has copied a file to the Windows clipboard. A file reference on the clipboard is in CF_HDROP format.

After calling this method, you must call [IEdmAddCustomRefs::CreateReferences](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~CreateReferences.html) to create the custom file reference in the vault.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmAddCustomRefs Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs.html)
[IEdmAddCustomRefs Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
