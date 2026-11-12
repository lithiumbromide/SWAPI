---
title: "ShowThirdPartyPopupMenu Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ShowThirdPartyPopupMenu"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowThirdPartyPopupMenu.html"
---

# ShowThirdPartyPopupMenu Method (ISldWorks)

Sets where to show a third-party pop-up (shortcut) menu.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowThirdPartyPopupMenu( _
   ByVal RegisterId As System.Integer, _
   ByVal Posx As System.Integer, _
   ByVal Posy As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim RegisterId As System.Integer
Dim Posx As System.Integer
Dim Posy As System.Integer
Dim value As System.Boolean

value = instance.ShowThirdPartyPopupMenu(RegisterId, Posx, Posy)
```

### C#

```csharp
System.bool ShowThirdPartyPopupMenu(
   System.int RegisterId,
   System.int Posx,
   System.int Posy
)
```

### C++/CLI

```cpp
System.bool ShowThirdPartyPopupMenu(
   System.int RegisterId,
   System.int Posx,
   System.int Posy
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RegisterId`: ID of shortcut menu from [ISldWorks::RegisterThirdPartyPopupMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RegisterThirdPartyPopupMenu.html)
- `Posx`: x coordinate for shortcut menu
- `Posy`: y coordinate for shortcut menu

### Return Value

True to show shortcut menu, false to not

## Examples

[Add Shortcut Menus to Add-ins (VB.NET)](Add_Shortcut_Menus_to_Add-ins_VBNET.htm)
[Add Shortcut Menus to Add-ins (C#)](Add_Shortcut_Menus_to_Add-ins_CSharp.htm)

## Remarks

Read about [Add-in Shortcut Menus](ms-its:sldworksapiprogguide.chm::/OVERVIEW/Add-in_Shortcut_Menus.htm).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
