---
title: "GetISO2768PartType Method (IDimXpertBlockTolerances)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertBlockTolerances"
member: "GetISO2768PartType"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertBlockTolerances~GetISO2768PartType.html"
---

# GetISO2768PartType Method (IDimXpertBlockTolerances)

Gets the ISO 2768 part type of this DimXpert block tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetISO2768PartType( _
   ByRef Type As swDimXpertISO2768PartType_e _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertBlockTolerances
Dim Type As swDimXpertISO2768PartType_e
Dim value As System.Boolean

value = instance.GetISO2768PartType(Type)
```

### C#

```csharp
System.bool GetISO2768PartType(
   out swDimXpertISO2768PartType_e Type
)
```

### C++/CLI

```cpp
System.bool GetISO2768PartType(
   [Out] swDimXpertISO2768PartType_e Type
)
```

### Parameters

- `Type`: ISO 2768 part type of this DimXpert block tolerance as defined in [swDimXpertISO2768PartType_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertISO2768PartType_e.html)

### Return Value

True if the method call is successful; false otherwise

## VBA Syntax

See [DimXpertBlockTolerances::GetISO2768PartType](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertBlockTolerances~GetISO2768PartType.html).

## Examples

[Get DimXpert Block Tolerance Example (VBA)](Get_DimXpert_Block_Tolerance_Example_VB.htm)
[Get DimXpert Block Tolerance Example (VB.NET)](Get_DimXpert_Block_Tolerance_Example_VBNET.htm)

## See Also

[IDimXpertBlockTolerances Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertBlockTolerances.html)
[IDimXpertBlockTolerances Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertBlockTolerances_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
