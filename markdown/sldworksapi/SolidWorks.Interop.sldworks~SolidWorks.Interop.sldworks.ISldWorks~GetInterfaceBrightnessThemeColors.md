---
title: "GetInterfaceBrightnessThemeColors Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetInterfaceBrightnessThemeColors"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetInterfaceBrightnessThemeColors.html"
---

# GetInterfaceBrightnessThemeColors Method (ISldWorks)

Gets the theme and colors of the SOLIDWORKS background.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInterfaceBrightnessThemeColors( _
   ByRef Colors As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Colors As System.Object
Dim value As System.Integer

value = instance.GetInterfaceBrightnessThemeColors(Colors)
```

### C#

```csharp
System.int GetInterfaceBrightnessThemeColors(
   out System.object Colors
)
```

### C++/CLI

```cpp
System.int GetInterfaceBrightnessThemeColors(
   [Out] System.Object^ Colors
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Colors`: Array of nine RGB (Red, Green, Blue) decimal values corresponding to the nine color types of the SOLIDWORKS background as defined in [swInterfaceBrightnessColor_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInterfaceBrightnessColor_e.html)

### Return Value

SOLIDWORKS background theme as defined in [swInterfaceBrightnessTheme_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInterfaceBrightnessTheme_e.html)

## VBA Syntax

See [SldWorks::GetInterfaceBrightnessThemeColors](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetInterfaceBrightnessThemeColors.html).

## Remarks

A SOLIDWORKS add-in can:

- use this method to determine the current theme and colors of the SOLIDWORKS background.
- be notified when the theme and colors in the SOLIDWORKS background change by registering for the [DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler.html) event.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISwHtmlInterface::GetInterfaceBrightnessTheme](ms-its:swhtmlcontrolapi.chm::/SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface~GetInterfaceBrightnessTheme.html)

## Availability

SOLIDWORKS 2016 SP2, Revision Number 24.2
