---
title: "EdmAddInMenuInfo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmAddInMenuInfo"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInMenuInfo.html"
---

# EdmAddInMenuInfo Structure

Contains information about a menu command implemented by an add-in.

## Syntax

### Visual Basic

```vb
Public Structure EdmAddInMenuInfo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmAddInMenuInfo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmAddInMenuInfo : public System.ValueType
```

## Examples

struct EdmAddInMenuInfo{
integer [mlCmdID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInMenuInfo~mlCmdID.html);
integer [mlEdmMenuFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInMenuInfo~mlEdmMenuFlags.html);
integer [mlToolbarButtonIndex](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInMenuInfo~mlToolbarButtonIndex.html);
integer [mlToolbarImageID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInMenuInfo~mlToolbarImageID.html);
string [mbsMenuStr](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInMenuInfo~mbsMenuStr.html);
string [mbsStatusBarHelp](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInMenuInfo~mbsStatusBarHelp.html);
string [mbsToolbarToolTip](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInMenuInfo~mbsToolbarToolTip.html);
};

## Examples

[Install Add-in (VB.NET)](Load_Addin_Example_VBNET.htm)
[Install Add-in (C#)](Load_Addin_Example_CSharp.htm)

## Remarks

Returned by [IEdmAddInMgr8::GetInstalledAddIn](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr8~GetInstalledAddIn.html).

## See Also

[EdmAddInMenuInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInMenuInfo_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2010
