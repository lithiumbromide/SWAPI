---
title: "AddVaultViewTab Method (IEdmCmdMgr6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCmdMgr6"
member: "AddVaultViewTab"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr6~AddVaultViewTab.html"
---

# AddVaultViewTab Method (IEdmCmdMgr6)

Adds the specified tab to the right of the tabs in the bottom panel of a vault view before opening it in File Explorer.

## Syntax

### Visual Basic

```vb
Sub AddVaultViewTab( _
   ByVal hWnd As System.Long, _
   ByVal bsName As System.String, _
   ByVal bsIconPath As System.String, _
   ByVal bsToolTip As System.String, _
   ByVal bsUniqueID As System.String _
)
```

### C#

```csharp
void AddVaultViewTab(
   System.long hWnd,
   System.string bsName,
   System.string bsIconPath,
   System.string bsToolTip,
   System.string bsUniqueID
)
```

### C++/CLI

```cpp
void AddVaultViewTab(
   System.int64 hWnd,
   System.String^ bsName,
   System.String^ bsIconPath,
   System.String^ bsToolTip,
   System.String^ bsUniqueID
)
```

### Parameters

- `hWnd`: Handle of the .NET control to display in the tab
- `bsName`: Name of the tab
- `bsIconPath`: Full path and filename of the 16X16 PNG image to display next to bsName on the tab
- `bsToolTip`: Tool tip for the tab
- `bsUniqueID`: Unique ID for this control

## Examples

See the [IEdmCmdMgr6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr6.html) examples.

## Remarks

Call this method in your add-in's implementation of [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html) where you handle the [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_PreExploreInit notification.

## See Also

[IEdmCmdMgr6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr6.html)
[IEdmCmdMgr6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr6_members.html)

## Availability

SOLIDWORKS PDM Professional 2018
