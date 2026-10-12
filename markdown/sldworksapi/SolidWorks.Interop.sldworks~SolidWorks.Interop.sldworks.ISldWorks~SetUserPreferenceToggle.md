---
title: "SetUserPreferenceToggle Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SetUserPreferenceToggle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html"
---

# SetUserPreferenceToggle Method (ISldWorks)

Sets system default user preference values.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetUserPreferenceToggle( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal OnFlag As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim UserPreferenceValue As System.Integer
Dim OnFlag As System.Boolean

instance.SetUserPreferenceToggle(UserPreferenceValue, OnFlag)
```

### C#

```csharp
void SetUserPreferenceToggle(
   System.int UserPreferenceValue,
   System.bool OnFlag
)
```

### C++/CLI

```cpp
void SetUserPreferenceToggle(
   System.int UserPreferenceValue,
   System.bool OnFlag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`: User preference as defined in [swUserPreferenceToggle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceToggle_e.html)
- `OnFlag`: True to toggle UserPreferenceValue on, false to toggle UserPreferenceValue off

## VBA Syntax

See [SldWorks::SetUserPreferenceToggle](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~SetUserPreferenceToggle.html).

## Examples

[Display Shadows in Shaded Mode (C++)](Display_Shadows_in_Shaded_Mode_Example_CPlusPlus_COM.htm)
[Change Labels of SOLIDWORKS Triad (VBA)](Change_Labels_of_SOLIDWORKS_Triad_Example_VB.htm)
[Rename Assembly Components (VBA)](Rename_Assembly_Components_Example_VB.htm)
[Save Drawing Sheets As DXF (VBA)](Save_Drawing_Sheets_as_DXF_Example_VB.htm)
[Suppress Rebuild Error Dialogs (VBA)](Suppress_Rebuild_Error_Dialogs_Example_VB.htm)
[Get and Set User Preferences (VBA)](Get_and_Set_User_Preferences_Example_VB.htm)
[Get and Set User Preferences (VB.NET)](Get_and_Set_User_Preferences_Example_VBNET.htm)
[Get and Set User Preferences (C#)](Get_and_Set_User_Preferences_Example_CSharp.htm)

## Remarks

This method is intended for user preferences that can be toggled.

This method is equivalent to interactively setting system options in the SOLIDWORKS Design software.

To use this method, choose one of the available items from the swUserPreferenceToggle_e enumeration. Pass true to turn the item on, and false to turn the item off.

For example, the following command forces the SOLIDWORKS Design application to use the Search Folders when loading files:

```vb
swapp.SetUserPreferenceToggle swUseFolderSearchRules, True
```

See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetUserPreferenceDoubleValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceDoubleValue.html)
[ISldWorks::GetUserPreferenceIntegerValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceIntegerValue.html)
[ISldWorks::GetUserPreferenceStringListValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceStringListValue.html)
[ISldWorks::GetUserPreferenceStringValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceStringValue.html)
[ISldWorks::GetUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.html)
[ISldWorks::SetUserPreferenceDoubleValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceDoubleValue.html)
[ISldWorks::SetUserPreferenceIntegerValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceIntegerValue.html)
[ISldWorks::SetUserPreferenceStringListValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceStringListValue.html)
[ISldWorks::SetUserPreferenceStringValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceStringValue.html)
[IModelDocExtension::SetUserPreferenceDouble Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceDouble.html)
[IModelDocExtension::SetUserPreferenceInteger Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceInteger.html)
[IModelDocExtension::SetUserPreferenceString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceString.html)
[IModelDocExtension::SetUserPreferenceTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceTextFormat.html)
[IModelDocExtension::SetUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceToggle.html)
[IModelDocExtension::GetUserPreferenceDouble Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceDouble.html)
[IModelDocExtension::GetUserPreferenceDoubleValueRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceDoubleValueRange.html)
[IModelDocExtension::GetUserPreferenceInteger Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.html)
[IModelDocExtension::GetUserPreferenceString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceString.html)
[IModelDocExtension::GetUserPreferenceTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceTextFormat.html)
[IModelDocExtension::GetUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceToggle.html)
