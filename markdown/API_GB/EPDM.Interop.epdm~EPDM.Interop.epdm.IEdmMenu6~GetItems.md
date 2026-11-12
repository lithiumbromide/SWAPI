---
title: "GetItems Method (IEdmMenu6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmMenu6"
member: "GetItems"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu6~GetItems.html"
---

# GetItems Method (IEdmMenu6)

Gets the commands that appear on the toolbar.

## Syntax

### Visual Basic

```vb
Sub GetItems( _
   ByVal lEdmMenuFlags As System.Integer, _
   ByRef ppoRetItems As EdmCmdInfo() _
)
```

### C#

```csharp
void GetItems(
   System.int lEdmMenuFlags,
   out EdmCmdInfo[] ppoRetItems
)
```

### C++/CLI

```cpp
void GetItems(
   System.int lEdmMenuFlags,
   [Out] array<EdmCmdInfo> ppoRetItems
)
```

### Parameters

- `lEdmMenuFlags`: Types of item you want returned as defined in [EdmMenuFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMenuFlags.html)
- `ppoRetItems`: Array of [EdmCmdInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdInfo.html) structs of the returned items

## Examples

[Get Menu Command Items (VB.NET)](Get_Menu_Command_Items_Example_VBNET.htm)
[Get Menu Command Items (C#)](Get_Menu_Command_Items_Example_CSharp.htm)

## Remarks

Calling [IEdmMenu5::GetToolbarItemIDs](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5~GetToolbarItemIDs.html), [IEdmMenu5::GetButtonImages](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5~GetButtonImages.html), or [IEdmMenu5::GetString](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5~GetString.html) also gets the commands that should appear on the toolbar.

[Return code](ReturnCodes.htm) S_OK indicates that the method successfully executed.

## See Also

[IEdmMenu6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu6.html)
[IEdmMenu6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu6_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
