---
title: "EdmCmdInfo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCmdInfo"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdInfo.html"
---

# EdmCmdInfo Structure

Contains information about menu command items.

## Syntax

### Visual Basic

```vb
Public Structure EdmCmdInfo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmCmdInfo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmCmdInfo : public System.ValueType
```

## Examples

struct EdmCmdInfo{
integer [mlCmdID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdInfo~mlCmdID.html);
string [mbsCmdStr](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdInfo~mbsCmdStr.html);
string [mbsTooltip](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdInfo~mbsTooltip.html);
string [mbsStatusBarHelp](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdInfo~mbsStatusBarHelp.html);
integer [mlEdmMenuFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdInfo~mlEdmMenuFlags.html);
object [moData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdInfo~moData.html);
};

## Examples

[Get Menu Command Items (VB.NET)](Get_Menu_Command_Items_Example_VBNET.htm)
[Get Menu Command Items (C#)](Get_Menu_Command_Items_Example_CSharp.htm)

## Remarks

Used in [IEdmMenu6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu6.html).

## See Also

[EdmCmdInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdInfo_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2009
