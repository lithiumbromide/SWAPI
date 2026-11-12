---
title: "CreateTree Method (IEdmBatchItemGeneration)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchItemGeneration"
member: "CreateTree"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration~CreateTree.html"
---

# CreateTree Method (IEdmBatchItemGeneration)

Computes the file reference tree for the items added to the batch using [IEdmBatchItemGeneration::AddSelection](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration~AddSelection.html).

## Syntax

### Visual Basic

```vb
Function CreateTree( _
   ByVal lParentWnd As System.Integer, _
   ByVal lEdmItemGenerationCmdFlags As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool CreateTree(
   System.int lParentWnd,
   System.int lEdmItemGenerationCmdFlags
)
```

### C++/CLI

```cpp
System.bool CreateTree(
   System.int lParentWnd,
   System.int lEdmItemGenerationCmdFlags
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `lEdmItemGenerationCmdFlags`: Combination of [EdmItemGenerationFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmItemGenerationFlags.html) bits

### Return Value

True if there is at least one item to create; false if there are none

## Examples

[Add Items (C#)](Add_Items_Example_CSharp.htm)
[Add Items (VB.NET)](Add_Items_Example_VBNET.htm)

## Remarks

After calling this method, call [IEdmBatchItemGeneration::GenerateItems](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration~GenerateItems.html) and, optionally, [IEdmBatchItemGeneration::ShowDlg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration~ShowDlg.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchItemGeneration Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration.html)
[IEdmBatchItemGeneration Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
