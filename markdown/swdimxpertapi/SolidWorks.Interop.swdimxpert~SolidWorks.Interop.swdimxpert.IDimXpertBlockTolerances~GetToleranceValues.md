---
title: "GetToleranceValues Method (IDimXpertBlockTolerances)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertBlockTolerances"
member: "GetToleranceValues"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertBlockTolerances~GetToleranceValues.html"
---

# GetToleranceValues Method (IDimXpertBlockTolerances)

Gets block tolerance settings for a given document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetToleranceValues( _
   ByRef Linear1 As System.Double, _
   ByRef Linear1Prec As System.Integer, _
   ByRef Linear2 As System.Double, _
   ByRef Linear2Prec As System.Integer, _
   ByRef Linear3 As System.Double, _
   ByRef Linear3Prec As System.Integer, _
   ByRef Angular As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertBlockTolerances
Dim Linear1 As System.Double
Dim Linear1Prec As System.Integer
Dim Linear2 As System.Double
Dim Linear2Prec As System.Integer
Dim Linear3 As System.Double
Dim Linear3Prec As System.Integer
Dim Angular As System.Double
Dim value As System.Boolean

value = instance.GetToleranceValues(Linear1, Linear1Prec, Linear2, Linear2Prec, Linear3, Linear3Prec, Angular)
```

### C#

```csharp
System.bool GetToleranceValues(
   out System.double Linear1,
   out System.int Linear1Prec,
   out System.double Linear2,
   out System.int Linear2Prec,
   out System.double Linear3,
   out System.int Linear3Prec,
   out System.double Angular
)
```

### C++/CLI

```cpp
System.bool GetToleranceValues(
   [Out] System.double Linear1,
   [Out] System.int Linear1Prec,
   [Out] System.double Linear2,
   [Out] System.int Linear2Prec,
   [Out] System.double Linear3,
   [Out] System.int Linear3Prec,
   [Out] System.double Angular
)
```

### Parameters

- `Linear1`: Length unit dimension for Tolerance 1
- `Linear1Prec`: Number of decimal places for Tolerance 1
- `Linear2`: Length unit dimension for Tolerance 2
- `Linear2Prec`: Number of decimal places for Tolerance 2
- `Linear3`: Length unit dimension for Tolerance 3
- `Linear3Prec`: Number of decimal places for Tolerance 3
- `Angular`: Angular unit dimensions

### Return Value

True if the method call is successful; false otherwise

## VBA Syntax

See [DimXpertBlockTolerances::GetToleranceValues](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertBlockTolerances~GetToleranceValues.html).

## Examples

[Get DimXpert Block Tolerance Example (VBA)](Get_DimXpert_Block_Tolerance_Example_VB.htm)
[Get DimXpert Block Tolerance Example (VB.NET)](Get_DimXpert_Block_Tolerance_Example_VBNET.htm)

## Remarks

This method gets the DimXpert block tolerance values that are set in the [SOLIDWORKS System Options and Document Properties dialog (Tools > Options > Document Properties > DimXpert)](sldworksapiprogguide.chm::/Overview/System_Options_And_Document_Properties.htm).

## See Also

[IDimXpertBlockTolerances Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertBlockTolerances.html)
[IDimXpertBlockTolerances Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertBlockTolerances_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
