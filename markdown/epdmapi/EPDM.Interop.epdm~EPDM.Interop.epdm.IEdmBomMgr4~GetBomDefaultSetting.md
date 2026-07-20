---
title: "GetBomDefaultSetting Method (IEdmBomMgr4)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomMgr4"
member: "GetBomDefaultSetting"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr4~GetBomDefaultSetting.html"
---

# GetBomDefaultSetting Method (IEdmBomMgr4)

Gets the specified computed BOM's default view settings as specified in the Conisio Admin tool.

## Syntax

### Visual Basic

```vb
Function GetBomDefaultSetting( _
   ByVal lLayoutId As System.Integer _
) As EdmBomDefaultSetting
```

### C#

```csharp
EdmBomDefaultSetting GetBomDefaultSetting(
   System.int lLayoutId
)
```

### C++/CLI

```cpp
EdmBomDefaultSetting GetBomDefaultSetting(
   System.int lLayoutId
)
```

### Parameters

- `lLayoutId`: BOM layout ID

### Return Value

[EdmBomDefaultSetting](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomDefaultSetting.html)

## Examples

See the

[IEdmBomMgr4](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr4.html)

example.

## Remarks

To specify lLayoutId, use

[IEdmBomMgr2::GetBomLayouts2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr2~GetBomLayouts2.html)

to find the layout ID of the BOM whose default settings you want to see.

## See Also

[IEdmBomMgr4 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr4.html)

[IEdmBomMgr4 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr4_members.html)

## Availability

SOLIDWORKS PDM Professional 2025
