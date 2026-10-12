---
title: "GetDirectionVector Method (IDimXpertDistanceBetweenDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertDistanceBetweenDimTol"
member: "GetDirectionVector"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDistanceBetweenDimTol~GetDirectionVector.html"
---

# GetDirectionVector Method (IDimXpertDistanceBetweenDimTol)

Gets the direction vector for this DimXpert distance-between dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDirectionVector( _
   ByRef I As System.Double, _
   ByRef J As System.Double, _
   ByRef K As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertDistanceBetweenDimTol
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetDirectionVector(I, J, K)
```

### C#

```csharp
System.bool GetDirectionVector(
   out System.double I,
   out System.double J,
   out System.double K
)
```

### C++/CLI

```cpp
System.bool GetDirectionVector(
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `I`: I component of the direction vector
- `J`: J component of the direction vector
- `K`: K component of the direction vector

### Return Value

True if the method call is successful; false otherwise

## VBA Syntax

See [DimXpertDistanceBetweenDimTol::GetDirectionVector](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertDistanceBetweenDimTol~GetDirectionVector.html).

## Examples

[Get and Set Location Dimension Example (C#)](Get_and_Set_Location_Dimension_Example_CSharp.htm)
[Get and Set Location Dimension Example (VB.NET)](Get_and_Set_Location_Dimension_Example_VBNET.htm)
[Get and Set Location Dimension Example (VBA)](Get_and_Set_Location_Dimension_Example_VB.htm)
[Get DimXpert Tolerance2 Example (VBA)](Get_DimXpert_Tolerance2_Example_VB.htm)
[Get DimXpert Tolerance2 Example (VB.NET)](Get_DimXpert_Tolerance2_Example_VBNET.htm)

## See Also

[IDimXpertDistanceBetweenDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDistanceBetweenDimTol.html)
[IDimXpertDistanceBetweenDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDistanceBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
