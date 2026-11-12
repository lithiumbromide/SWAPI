---
title: "EdmCardViewFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCardViewFlag"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardViewFlag.html"
---

# EdmCardViewFlag Enumeration

Options for appearance and functionality of card views created with [IEdmVault10::CreateCardViewEx2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault10~CreateCardViewEx2.html) and [IEdmFolder10::CreateCardView2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder10~CreateCardView2.html). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmCardViewFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmCardViewFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmCardViewFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmCvf_3StateCheckboxes | 2 = Permit three-state checkboxes |
| EdmCvf_CallSaveOnCtrlReturn | 512 = Save on CTRL-Enter |
| EdmCvf_ComputeDefaultValues | 8 = Compute default values in the card |
| EdmCvf_DisableButtons | 256 = Disable all buttons in the card |
| EdmCvf_Normal | 253 = Default (1+4+8+16+32+64+128) |
| EdmCvf_Nothing | 0 = Nothing |
| EdmCvf_PermitComputedValues | 64 = Permit controls to receive values from input formulas |
| EdmCvf_PermitControlledTabs | 1 = Permit controlling tab controls with variables |
| EdmCvf_PermitReadOnlyFields | 32 = Permit the card to have read-only fields |
| EdmCvf_RunFormulas | 4 = Evaluate input formulas in the card |
| EdmCvf_RunFormulasOnOpen | 1024 = Force execution of formulas on all controls when opened |
| EdmCvf_SearchMode | 130 = Search tool mode (2+128) |
| EdmCvf_SerNoMenu | 1048576 = Show shortcut menu for serial numbers |
| EdmCvf_TextureBackground | 128 = Fade the card background |
| EdmCvf_VerifyValues | 16 = Check mandatory and unique values during save |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
