---
title: "SetUserPreferenceStringValue Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetUserPreferenceStringValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceStringValue.html"
---

# SetUserPreferenceStringValue Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::SetUserPreferenceString](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SetUserPreferenceString.html).

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
Dim instance As IModelDoc2
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

- `UserPreference`: User preference value as defined in [swUserPreferenceStringValue_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceStringValue_e.html)
- `Value`: Value of the user preference specified in UserPreference

### Return Value

True if user preference value is changed, false if not

## VBA Syntax

See [ModelDoc2::SetUserPreferenceStringValue](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetUserPreferenceStringValue.html).

## Remarks

This method is equivalent to interactively setting document properties in the SOLIDWORKS Design software. See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
