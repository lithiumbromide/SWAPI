---
title: "GetToleranceValue Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "GetToleranceValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetToleranceValue.html"
---

# GetToleranceValue Method (IModeler)

Gets the current tolerance value of the given tolerance ID.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetToleranceValue( _
   ByVal ToleranceID As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim ToleranceID As System.Integer
Dim value As System.Double

value = instance.GetToleranceValue(ToleranceID)
```

### C#

```csharp
System.double GetToleranceValue(
   System.int ToleranceID
)
```

### C++/CLI

```cpp
System.double GetToleranceValue(
   System.int ToleranceID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ToleranceID`: Type of tolerance that you want to obtain as defined by [swTolerances_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolerances_e.html)

### Return Value

Tolerance value for the specified ToleranceID

## VBA Syntax

See [Modeler::GetToleranceValue](ms-its:sldworksapivb6.chm::/sldworks~Modeler~GetToleranceValue.html).

## Examples

[Get Length of Spline or Elliptical Edge (VBA)](Get_Length_of_Spline_or_Elliptical_Edge_Example_VB.htm)
[Get Parameters and Spline Points for Curve (VBA)](Get_Parameters_and_Spline_Points_for_Curve_Example_VB.htm)
[Get Tolerance (VBA)](Get_Tolerance_Example_VB.htm)

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::UnsetTolerances Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~UnsetTolerances.html)
[IModeler::SetToleranceValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetToleranceValue.html)

## Availability

SOLIDWORKS 2000 SP03, Revision Number 8.3
