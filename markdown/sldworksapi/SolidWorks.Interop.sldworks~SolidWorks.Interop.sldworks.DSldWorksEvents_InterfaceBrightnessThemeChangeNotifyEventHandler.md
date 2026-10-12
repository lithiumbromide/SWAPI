---
title: "DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler.html"
---

# DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies an add-in when the SOLIDWORKS background changes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler( _
   ByVal ThemeType As System.Integer, _
   ByRef Colors As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler(
   System.int ThemeType,
   ref System.object Colors
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler(
   System.int ThemeType,
   System.Object^% Colors
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ThemeType`: SOLIDWORKS background as defined in [swInterfaceBrightnessTheme_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInterfaceBrightnessTheme_e.html)
- `Colors`: Array of RGB (Red, Green, Blue) decimal values (see **Remarks**)

## VBA Syntax

See [InterfaceBrightnessThemeChangeNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~InterfaceBrightnessThemeChangeNotify_EV.html).

## Examples

[Add Shortcut Menus to Add-ins (VB.NET)](Add_Shortcut_Menus_to_Add-ins_VBNET.htm)
[Add Shortcut Menus to Add-ins (C#)](Add_Shortcut_Menus_to_Add-ins_CSharp.htm)

## Remarks

The Colors array is indexed by [swInterfaceBrightnessColor_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInterfaceBrightnessColor_e.html).

To get the SOLIDWORKS background:

- theme, use [ISwHtmlInterface::GetInterfaceBrightnessTheme](ms-its:swhtmlcontrolapi.chm::/SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface~GetInterfaceBrightnessTheme.html).
- theme and colors, [ISldWorks::GetInterfaceBrightnessThemeColors](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetInterfaceBrightnessThemeColors.html).

If developing a C++ application, use [swAppInterfaceBrightnessThemeChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2016 SP1, Revision Number 24.1
