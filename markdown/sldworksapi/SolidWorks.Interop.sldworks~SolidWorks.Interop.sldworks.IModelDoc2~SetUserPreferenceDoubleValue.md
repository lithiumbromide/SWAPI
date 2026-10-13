---
title: "SetUserPreferenceDoubleValue Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetUserPreferenceDoubleValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceDoubleValue.html"
---

# SetUserPreferenceDoubleValue Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::SetUserPreferenceDouble](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SetUserPreferenceDouble.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetUserPreferenceDoubleValue( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal Value As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim UserPreferenceValue As System.Integer
Dim Value As System.Double
Dim value As System.Boolean

value = instance.SetUserPreferenceDoubleValue(UserPreferenceValue, Value)
```

### C#

```csharp
System.bool SetUserPreferenceDoubleValue(
   System.int UserPreferenceValue,
   System.double Value
)
```

### C++/CLI

```cpp
System.bool SetUserPreferenceDoubleValue(
   System.int UserPreferenceValue,
   System.double Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`: User preference value as defined in [swUserPreferenceDoubleValue_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceDoubleValue_e.html)
- `Value`: Numeric value to give to the user preference specified in UserPreferenceValue

### Return Value

True if the user preference is set successfully, false if not

## VBA Syntax

See [ModelDoc2::SetUserPreferenceDoubleValue](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetUserPreferenceDoubleValue.html).

## Examples

[Get and Set Material Density (VBA)](Get_and_Set_Material_Density_Example_VB.htm)
[Get Excel Cell Value for Density (VBA)](Get_Excel_Cell_Value_for_Density_Example_VB.htm)

## Remarks

This method is equivalent to interactively setting document properties in the SOLIDWORKS Design software. See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
