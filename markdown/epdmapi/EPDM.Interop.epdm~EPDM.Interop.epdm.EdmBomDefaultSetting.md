---
title: "EdmBomDefaultSetting Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBomDefaultSetting"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomDefaultSetting.html"
---

# EdmBomDefaultSetting Structure

Contains the default view settings of a computed BOM.

## Syntax

### Visual Basic

```vb
Public Structure EdmBomDefaultSetting
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmBomDefaultSetting : System.ValueType
```

### C++/CLI

```cpp
public value class EdmBomDefaultSetting : public System.ValueType
```

## Examples

struct EdmBomDefaultSetting{
integer [mlBomDisplayType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomDefaultSetting~mlBomDisplayType.html);
integer [mlBomRefVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomDefaultSetting~mlBomRefVersion.html);
integer [mlBomSelectedFile](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomDefaultSetting~mlBomSelectedFile.html);
integer [mlBomTreeView](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomDefaultSetting~mlBomTreeView.html);
integer [mlBOMViewSettings](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomDefaultSetting~mlBOMViewSettings.html);
integer [mlBOMWeldmentCutListType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomDefaultSetting~mlBOMWeldmentCutListType.html);
};

## Remarks

Returned by [IEdmBomMgr4::GetBomDefaultSetting](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr4~GetBomDefaultSetting.html).

## See Also

[EdmBomDefaultSetting Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomDefaultSetting_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2025
