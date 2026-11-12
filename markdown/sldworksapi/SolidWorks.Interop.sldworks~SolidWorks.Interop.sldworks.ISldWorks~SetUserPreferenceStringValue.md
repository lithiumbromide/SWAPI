---
title: "SetUserPreferenceStringValue Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SetUserPreferenceStringValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceStringValue.html"
---

# SetUserPreferenceStringValue Method (ISldWorks)

Sets system default user preference values.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetUserPreferenceStringValue( _
   ByVal UserPreference As System.Integer, _
   ByVal Value As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim UserPreference As System.Integer
Dim Value As System.String
Dim value As System.Boolean

value = instance.SetUserPreferenceStringValue(UserPreference, Value)
```

### C#

```csharp
System.bool SetUserPreferenceStringValue(
   System.int UserPreference,
   System.string Value
)
```

### C++/CLI

```cpp
System.bool SetUserPreferenceStringValue(
   System.int UserPreference,
   System.String^ Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreference`: User preference as defined in [swUserPreferenceStringValue_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceStringValue_e.html)
- `Value`: Value of UserPreference

### Return Value

True if UserPreference is set, false if not

## VBA Syntax

See [SldWorks::SetUserPreferenceStringValue](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~SetUserPreferenceStringValue.html).

## Examples

[Change Labels of SOLIDWORKS Triad (VBA)](Change_Labels_of_SOLIDWORKS_Triad_Example_VB.htm)
[Get and Set User Preferences (VBA)](Get_and_Set_User_Preferences_Example_VB.htm)
[Get and Set User Preferences (VB.NET)](Get_and_Set_User_Preferences_Example_VBNET.htm)
[Get and Set User Preferences (C#)](Get_and_Set_User_Preferences_Example_CSharp.htm)

## Remarks

This method is intended for user preferences of type string.

This method is equivalent to interactively setting system options in the SOLIDWORKS Design software.

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
[ISldWorks::SetUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html)
[IModelDocExtension::GetUserPreferenceDouble Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceDouble.html)
[IModelDocExtension::GetUserPreferenceDoubleValueRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceDoubleValueRange.html)
[IModelDocExtension::GetUserPreferenceInteger Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.html)
[IModelDocExtension::GetUserPreferenceString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceString.html)
[IModelDocExtension::GetUserPreferenceTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceTextFormat.html)
[IModelDocExtension::GetUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceToggle.html)
[IModelDocExtension::SetUserPreferenceDouble Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceDouble.html)
[IModelDocExtension::SetUserPreferenceInteger Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceInteger.html)
[IModelDocExtension::SetUserPreferenceString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceString.html)
[IModelDocExtension::SetUserPreferenceTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceTextFormat.html)
[IModelDocExtension::SetUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceToggle.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
