---
title: "GenerateItems Method (IEdmBatchItemGeneration)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchItemGeneration"
member: "GenerateItems"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration~GenerateItems.html"
---

# GenerateItems Method (IEdmBatchItemGeneration)

Creates the items added to the batch by [IEdmBatchItemGeneration::AddSelection](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration~AddSelection.html).

## Syntax

### Visual Basic

```vb
Sub GenerateItems( _
   ByVal lParentWnd As System.Integer, _
   ByRef ppoRetItems() As EdmGenItemInfo, _
   ByRef pbOpen As System.Boolean, _
   Optional ByVal poCallback As System.Object _
)
```

### C#

```csharp
void GenerateItems(
   System.int lParentWnd,
   out EdmGenItemInfo[] ppoRetItems,
   out System.bool pbOpen,
   System.object poCallback
)
```

### C++/CLI

```cpp
void GenerateItems(
   System.int lParentWnd,
   [Out] array<EdmGenItemInfo>^ ppoRetItems,
   [Out] System.bool pbOpen,
   System.Object^ poCallback
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `ppoRetItems`: Array of [EdmGenItemInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGenItemInfo.html) structures, one structure for each new item
- `pbOpen`: True, if the following occurred:

  - [EdmItemGenerationFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmItemGenerationFlags.html).Eigcf_OpenItemsCheckbox was set in [IEdmBatchItemGeneration::CreateTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration~CreateTree.html).
  - The user selected the checkbox to open items after creation in the dialog box displayed by [IEdmBatchItemGeneration::ShowDlg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration~ShowDlg.html).

  False, if not
- `poCallback`: Null; reserved for future use

## Examples

[Add Items (C#)](Add_Items_Example_CSharp.htm)
[Add Items (VB.NET)](Add_Items_Example_VBNET.htm)

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchItemGeneration Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration.html)
[IEdmBatchItemGeneration Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
