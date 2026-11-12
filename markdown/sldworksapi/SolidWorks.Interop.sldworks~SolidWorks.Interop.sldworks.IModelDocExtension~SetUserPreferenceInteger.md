---
title: "SetUserPreferenceInteger Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SetUserPreferenceInteger"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceInteger.html"
---

# SetUserPreferenceInteger Method (IModelDocExtension)

Sets document default user preference values. This method is intended for user preferences of type integer.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetUserPreferenceInteger( _
   ByVal UserPref As System.Integer, _
   ByVal UserPrefOption As System.Integer, _
   ByVal Value As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim UserPref As System.Integer
Dim UserPrefOption As System.Integer
Dim Value As System.Integer
Dim value As System.Boolean

value = instance.SetUserPreferenceInteger(UserPref, UserPrefOption, Value)
```

### C#

```csharp
System.bool SetUserPreferenceInteger(
   System.int UserPref,
   System.int UserPrefOption,
   System.int Value
)
```

### C++/CLI

```cpp
System.bool SetUserPreferenceInteger(
   System.int UserPref,
   System.int UserPrefOption,
   System.int Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPref`: User preference as defined in [swUserPreferenceIntegerValue_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceIntegerValue_e.html)
- `UserPrefOption`: User-preference option for customizing annotation and dimension drafting standards and as defined in [swUserPreferenceOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceOption_e.html); if not needed, then specify swDetailingNoOptionSpecified
- `Value`: Value to assign to the user preference specified in UserPref

### Return Value

True if the user preference is set, false if not

## VBA Syntax

See [ModelDocExtension::SetUserPreferenceInteger](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SetUserPreferenceInteger.html).

## Examples

[Get and Set User Preferences (VBA)](Get_and_Set_User_Preferences_Example_VB.htm)
[Get and Set User Preferences (VB.NET)](Get_and_Set_User_Preferences_Example_VBNET.htm)
[Get and Set User Preferences (C#)](Get_and_Set_User_Preferences_Example_CSharp.htm)

## Remarks

This method is equivalent to interactively setting document properties in the SOLIDWORKS Design software. See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::SetUserPreferenceDouble Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceDouble.html)
[IModelDocExtension::SetUserPreferenceString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceString.html)
[IModelDocExtension::SetUserPreferenceTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceTextFormat.html)
[IModelDocExtension::SetUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceToggle.html)
[IModelDocExtension::GetUserPreferenceDouble Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceDouble.html)
[IModelDocExtension::GetUserPreferenceDoubleValueRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceDoubleValueRange.html)
[IModelDocExtension::GetUserPreferenceInteger Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.html)
[IModelDocExtension::GetUserPreferenceString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceString.html)
[IModelDocExtension::GetUserPreferenceTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceTextFormat.html)
[IModelDocExtension::GetUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceToggle.html)
[ISldWorks::GetUserPreferenceDoubleValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceDoubleValue.html)
[ISldWorks::GetUserPreferenceIntegerValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceIntegerValue.html)
[ISldWorks::GetUserPreferenceStringListValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceStringListValue.html)
[ISldWorks::GetUserPreferenceStringValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceStringValue.html)
[ISldWorks::GetUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.html)
[ISldWorks::SetUserPreferenceDoubleValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceDoubleValue.html)
[ISldWorks::SetUserPreferenceIntegerValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceIntegerValue.html)
[ISldWorks::SetUserPreferenceStringListValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceStringListValue.html)
[ISldWorks::SetUserPreferenceStringValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceStringValue.html)
[ISldWorks::SetUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
