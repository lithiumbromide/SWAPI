---
title: "SaveSettings Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SaveSettings"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SaveSettings.html"
---

# SaveSettings Method (ISldWorks)

Saves the specified SOLIDWORKS settings to the specified ***.sldreg** file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveSettings( _
   ByVal FileName As System.String, _
   ByVal SystemOptions As System.Boolean, _
   ByVal ToolbarLayout As System.Integer, _
   ByVal KeyboardShortcuts As System.Boolean, _
   ByVal MouseGestures As System.Boolean, _
   ByVal MenuCustomization As System.Boolean, _
   ByVal SavedViews As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim SystemOptions As System.Boolean
Dim ToolbarLayout As System.Integer
Dim KeyboardShortcuts As System.Boolean
Dim MouseGestures As System.Boolean
Dim MenuCustomization As System.Boolean
Dim SavedViews As System.Boolean
Dim value As System.Integer

value = instance.SaveSettings(FileName, SystemOptions, ToolbarLayout, KeyboardShortcuts, MouseGestures, MenuCustomization, SavedViews)
```

### C#

```csharp
System.int SaveSettings(
   System.string FileName,
   System.bool SystemOptions,
   System.int ToolbarLayout,
   System.bool KeyboardShortcuts,
   System.bool MouseGestures,
   System.bool MenuCustomization,
   System.bool SavedViews
)
```

### C++/CLI

```cpp
System.int SaveSettings(
   System.String^ FileName,
   System.bool SystemOptions,
   System.int ToolbarLayout,
   System.bool KeyboardShortcuts,
   System.bool MouseGestures,
   System.bool MenuCustomization,
   System.bool SavedViews
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Full path and filename to which to save the settings (***.sldreg**)
- `SystemOptions`: True to save system options, false to not
- `ToolbarLayout`: Toolbar layout as defined in [swToolbarLayoutOption_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swToolbarLayoutOption_e.html)
- `KeyboardShortcuts`: True to save keyboard shortcuts, false to not
- `MouseGestures`: True to save mouse gestures, false to not
- `MenuCustomization`: True to save menu customizations, false to not
- `SavedViews`: True to save views, false to not

### Return Value

Error code as defined in [swSaveRestoreSettingsResults_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSaveRestoreSettingsResults_e.html)

## VBA Syntax

See [SldWorks::SaveSettings](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~SaveSettings.html).

## Examples

' VBA precondition:

' c:\temp exists

```
Dim swApp As SldWorks.SldWorks
Option Explicit
Sub main()
```

```
    Set swApp = Application.SldWorks

    Dim boolStatus As Long
    Dim path As String

    path = "C:\temp\swSettings2.sldreg"
    boolStatus = swApp.SaveSettings(path, True, swToolbarLayoutOption_e.swToolbarLayoutOption_AllToolbars, True, True, True, True)
```

```
End Sub
```

## Remarks

For C++ only, specify all System.bool parameters using VARIANT_TRUE (-1) and VARIANT_FALSE (0).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::RestoreSettings Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RestoreSettings.html)
[ISldWorks::LoadAdminSettingsFile Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAdminSettingsFile.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
