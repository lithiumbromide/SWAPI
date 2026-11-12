---
title: "CreateTree Method (IEdmAddCustomRefs)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddCustomRefs"
member: "CreateTree"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~CreateTree.html"
---

# CreateTree Method (IEdmAddCustomRefs)

Computes the file reference tree.

## Syntax

### Visual Basic

```vb
Function CreateTree( _
   ByVal lEdmCreateReferenceFlags As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool CreateTree(
   System.int lEdmCreateReferenceFlags
)
```

### C++/CLI

```cpp
System.bool CreateTree(
   System.int lEdmCreateReferenceFlags
)
```

### Parameters

- `lEdmCreateReferenceFlags`: Combination of [EdmCreateReferenceFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCreateReferenceFlags.html) bits

### Return Value

True if there are file references, false if not

## Examples

[Add Custom File Reference (VB.NET)](Add_Custom_File_Reference_Example_VBNET.htm)
[Add Custom File Reference (C#)](Add_Custom_File_Reference_Example_CSharp.htm)

## Remarks

If this method returns true, call [IEdmAddCustomRefs::ShowDlg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~ShowDlg.html) to display and edit the file references.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmAddCustomRefs Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs.html)
[IEdmAddCustomRefs Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
