---
title: "GetUserPreferenceStringValue Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetUserPreferenceStringValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceStringValue.html"
---

# GetUserPreferenceStringValue Method (ISldWorks)

Gets system default user preference values.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUserPreferenceStringValue( _
   ByVal UserPreference As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim UserPreference As System.Integer
Dim value As System.String

value = instance.GetUserPreferenceStringValue(UserPreference)
```

### C#

```csharp
System.string GetUserPreferenceStringValue(
   System.int UserPreference
)
```

### C++/CLI

```cpp
System.String^ GetUserPreferenceStringValue(
   System.int UserPreference
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreference`: User preference as defined in [swUserPreferenceStringValue_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceStringValue_e.html)

### Return Value

Value of UserPreference

## VBA Syntax

See [SldWorks::GetUserPreferenceStringValue](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetUserPreferenceStringValue.html).

## Examples

[Get Locations and Names of Document Templates (VBA)](Get_Locations_and_Names_of_Document_Templates_Example_VB.htm)
[Get or Set the Backup Directory (VBA)](Get_or_Set_the_Backup_Directory_Example_VB.htm)
[Get and Set User Preferences (VBA)](Get_and_Set_User_Preferences_Example_VB.htm)
[Get and Set User Preferences (VB.NET)](Get_and_Set_User_Preferences_Example_VBNET.htm)
[Get and Set User Preferences (C#)](Get_and_Set_User_Preferences_Example_CSharp.htm)
[Insert Model Annotations (C#)](Insert_Model_Annotations_Example_CSharp.htm)
[Insert Model Annotations (VB.NET)](Insert_Model_Annotations_Example_VBNET.htm)
[Insert Model Annotations (VBA)](Insert_Model_Annotations_Example_VB.htm)
[Fill Holes in Part (C#)](Fill_Holes_in_Part_Example_CSharp.htm)
[Fill Holes in Part (VB.NET)](Fill_Holes_in_Part_Example_VBNET.htm)
[Fill Holes in Part (VBA)](Fill_Holes_in_Part_Example_VB.htm)

## Remarks

This method is intended for user preferences of type string and is equivalent to interactively getting system options in the SOLIDWORKS Design software. See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetUserPreferenceDoubleValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceDoubleValue.html)
[ISldWorks::GetUserPreferenceIntegerValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceIntegerValue.html)
[ISldWorks::GetUserPreferenceStringListValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceStringListValue.html)
[ISldWorks::GetUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.html)
[ISldWorks::SetUserPreferenceDoubleValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceDoubleValue.html)
[ISldWorks::SetUserPreferenceIntegerValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceIntegerValue.html)
[ISldWorks::SetUserPreferenceStringListValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceStringListValue.html)
[ISldWorks::SetUserPreferenceStringValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceStringValue.html)
[ISldWorks::SetUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html)
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

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
