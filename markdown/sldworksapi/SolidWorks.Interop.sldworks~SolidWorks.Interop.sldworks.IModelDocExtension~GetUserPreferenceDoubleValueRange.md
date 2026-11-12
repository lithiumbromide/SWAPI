---
title: "GetUserPreferenceDoubleValueRange Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetUserPreferenceDoubleValueRange"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceDoubleValueRange.html"
---

# GetUserPreferenceDoubleValueRange Method (IModelDocExtension)

Gets the current document default user preference value, and the minimum and maximum valid document user preference values.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUserPreferenceDoubleValueRange( _
   ByVal UserPref As System.Integer, _
   ByRef Value As System.Double, _
   ByRef MinValue As System.Double, _
   ByRef MaxValue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim UserPref As System.Integer
Dim Value As System.Double
Dim MinValue As System.Double
Dim MaxValue As System.Double
Dim value As System.Integer

value = instance.GetUserPreferenceDoubleValueRange(UserPref, Value, MinValue, MaxValue)
```

### C#

```csharp
System.int GetUserPreferenceDoubleValueRange(
   System.int UserPref,
   out System.double Value,
   out System.double MinValue,
   out System.double MaxValue
)
```

### C++/CLI

```cpp
System.int GetUserPreferenceDoubleValueRange(
   System.int UserPref,
   [Out] System.double Value,
   [Out] System.double MinValue,
   [Out] System.double MaxValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPref`: User preference as defined in [swUserPreferenceDoubleValue_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceDoubleValue_e.html)
- `Value`: Current value of UserPref; if the return value >= 0, see **Remarks**
- `MinValue`: Minimum value of UserPref; if the return value = 0, see Remarks
- `MaxValue`: Maximum value of UserPref; if the return value= 0, see Remarks

### Return Value

Status upon return from this method; see Remarks

## VBA Syntax

See [ModelDocExtension::GetUserPreferenceDoubleValueRange](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetUserPreferenceDoubleValueRange.html).

## Remarks

This method is equivalent to interactively getting document properties in the SOLIDWORKS Design software.

The return value indicates the status upon return from this method:

- 0 indicates that the current, minimum, and maximum user preference values were retrieved.
- 1 indicates that the current user preference value was retrieved, but the minimum and maximum user preference values were not. This most likely occurred because the SOLIDWORKS API code was not implemented to retrieve the minimum and maximum allowed values, so the return value is warning you that not all information was returned. It does not indicate a fatal error. The SOLIDWORKS API code is only implemented for returning the minimum and maximum value in cases where those values are not obvious to the user, such as with user preference swImageQualityShadedDeviation.
- -1 indicates that the current user preference value could not be retrieved. This most likely occurred because UserPref was not recognized as a valid user preference value.

If you want to retrieve the current user preference value only (i.e., you do not want to retrieve the valid minimum and maximum user preference values), use [IModelDocExtension::GetUserPreferenceDouble](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceDouble.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
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
[IModelDocExtension::GetUserPreferenceDouble Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceDouble.html)
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

SOLIDWORKS 2007 FCS, Revision Number 15.0
