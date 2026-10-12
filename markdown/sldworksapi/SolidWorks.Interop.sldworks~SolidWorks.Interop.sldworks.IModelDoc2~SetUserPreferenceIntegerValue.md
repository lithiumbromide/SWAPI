---
title: "SetUserPreferenceIntegerValue Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetUserPreferenceIntegerValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceIntegerValue.html"
---

# SetUserPreferenceIntegerValue Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::SetUserPreferenceInteger](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SetUserPreferenceInteger.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetUserPreferenceIntegerValue( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal Value As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim UserPreferenceValue As System.Integer
Dim Value As System.Integer
Dim value As System.Boolean

value = instance.SetUserPreferenceIntegerValue(UserPreferenceValue, Value)
```

### C#

```csharp
System.bool SetUserPreferenceIntegerValue(
   System.int UserPreferenceValue,
   System.int Value
)
```

### C++/CLI

```cpp
System.bool SetUserPreferenceIntegerValue(
   System.int UserPreferenceValue,
   System.int Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`: User preference value as defined in [swUserPreferenceIntegerValue_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceIntegerValue_e.html)
- `Value`: Numeric value you give to the user preference specified in UserPreferenceValue

### Return Value

True if the setting is changed successfully, false if not

## VBA Syntax

See [ModelDoc2::SetUserPreferenceIntegerValue](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetUserPreferenceIntegerValue.html).

## Examples

[Set Grid Lines (VBA)](Set_Grid_Lines_Example_VB.htm)

## Remarks

This method is equivalent to interactively setting document properties in the SOLIDWORKS Design software. See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
