---
title: "GetUserPreferenceIntegerValue Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetUserPreferenceIntegerValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUserPreferenceIntegerValue.html"
---

# GetUserPreferenceIntegerValue Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::GetUserPreferenceInteger](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUserPreferenceIntegerValue( _
   ByVal UserPreferenceValue As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim UserPreferenceValue As System.Integer
Dim value As System.Integer

value = instance.GetUserPreferenceIntegerValue(UserPreferenceValue)
```

### C#

```csharp
System.int GetUserPreferenceIntegerValue(
   System.int UserPreferenceValue
)
```

### C++/CLI

```cpp
System.int GetUserPreferenceIntegerValue(
   System.int UserPreferenceValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`: Value as defined in [swUserPreferenceIntegerValue_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceIntegerValue_e.html)

### Return Value

Numeric value associated with the specified UserPreferenceValue

## VBA Syntax

See [ModelDoc2::GetUserPreferenceIntegerValue](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetUserPreferenceIntegerValue.html).

## Examples

[Get Material Properties (VBA)](Get_Material_Properties_Example_VB.htm)
[Make Part Transparent (VBA)](Make_Part_Transparent_Example_VB.htm)
[Save Document as TIFF (VBA)](Save_As_Tiff_Example_VB.htm)
[Set Grid Lines (VBA)](Set_Grid_Lines_Example_VB.htm)

## Remarks

This method is equivalent to interactively getting document properties in the SOLIDWORKS Design software. See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
