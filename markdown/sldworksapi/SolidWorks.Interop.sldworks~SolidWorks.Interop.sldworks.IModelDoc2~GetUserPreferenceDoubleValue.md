---
title: "GetUserPreferenceDoubleValue Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetUserPreferenceDoubleValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUserPreferenceDoubleValue.html"
---

# GetUserPreferenceDoubleValue Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::GetUserPreferenceDouble](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceDouble.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUserPreferenceDoubleValue( _
   ByVal UserPreferenceValue As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim UserPreferenceValue As System.Integer
Dim value As System.Double

value = instance.GetUserPreferenceDoubleValue(UserPreferenceValue)
```

### C#

```csharp
System.double GetUserPreferenceDoubleValue(
   System.int UserPreferenceValue
)
```

### C++/CLI

```cpp
System.double GetUserPreferenceDoubleValue(
   System.int UserPreferenceValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`: Value as defined in [swUserPreferenceDoubleValue_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceDoubleValue_e.html)

### Return Value

Numeric value of the user preference specified in UserPreferenceValue

## VBA Syntax

See [ModelDoc2::GetUserPreferenceDoubleValue](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetUserPreferenceDoubleValue.html).

## Examples

[Get and Set Material Density (VBA)](Get_and_Set_Material_Density_Example_VB.htm)
[Get Mass Properties of Assembly Component (VBA)](Get_Mass_Properties_of_Assembly_Component_Example_VB.htm)

## Remarks

This method is equivalent to interactively getting document properties in the SOLIDWORKS Design software. See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

If you want to retrieve the current, minimum, and maximum values for a document user preference, use [IModelDoc2::GetUserPreferenceDoubleValueRange](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceDoubleValueRange.html). Be sure to read that method's **Remarks** section because its implementation is limited.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
