---
title: "GetFreeBodyForcesAndMoments Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetFreeBodyForcesAndMoments"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetFreeBodyForcesAndMoments.html"
---

# GetFreeBodyForcesAndMoments Method (ICWResults)

Gets the x-, y-, and z-component and resultant free body forces and moments for the specified entities and the entire model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFreeBodyForcesAndMoments( _
   ByVal DispPlane As System.Object, _
   ByVal SelectedRefPoint As System.Object, _
   ByVal ArraySelectedEntities As System.Object, _
   ByVal NUnits As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim DispPlane As System.Object
Dim SelectedRefPoint As System.Object
Dim ArraySelectedEntities As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetFreeBodyForcesAndMoments(DispPlane, SelectedRefPoint, ArraySelectedEntities, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetFreeBodyForcesAndMoments(
   System.object DispPlane,
   System.object SelectedRefPoint,
   System.object ArraySelectedEntities,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetFreeBodyForcesAndMoments(
   System.Object^ DispPlane,
   System.Object^ SelectedRefPoint,
   System.Object^ ArraySelectedEntities,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `DispPlane`: Plane, axis, or coordinate system relative to which the results are listed
- `SelectedRefPoint`: Reference point used to list the moments for the forces that are available in ArraySelectedEntities; NULL to not list the moments
- `ArraySelectedEntities`: Selected faces, edges, vertices, and components
- `NUnits`: Output units as defined in [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

If SelectedRefPoint is NULL:

Array of eight doubles of the free body forces for all selections in ArraySelectedEntities and for the entire model:

- Summation of x-components of free body force for all selections
- Summation of y-components of free body force for all selections
- Summation of z-components of free body force for all selections
- Resultant free body force for all selections
- Summation of x-components of free body moment for the entire model
- Summation of y-components of free body moment for the entire model
- Summation of z-components of free body moment for the entire model
- Resultant free body moment for the entire model

If SelectedRefPoint is not NULL:

Array of sixteen doubles of the free body forces and moments for all selections in ArraySelectedEntities and for the entire model:

- Summation of x-components of free body force for all selections
- Summation of y-components of free body force for all selections
- Summation of z-components of free body force for all selections
- Resultant free body force for all selections
- Summation of x-components of free body moment for all selections
- Summation of y-components of free body moment for all selections
- Summation of z-components of free body moment for all selections
- Resultant free body moment for all selections
- Summation of x-components of free body force for the entire model
- Summation of y-components of free body force for the entire model
- Summation of z-components of free body force for the entire model
- Resultant free body force for the entire model
- Summation of x-components of free body moment for the entire model
- Summation of y-components of free body moment for the entire model
- Summation of z-components of free body moment for the entire model
- Resultant free body moment for the entire model

## VBA Syntax

See [CWResults::GetFreeBodyForcesAndMoments](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetFreeBodyForcesAndMoments.html).

## Examples

[Get Free Body Forces and Moments (VBA)](Get_Free_Body_Forces_and_Moments_Example_VB.htm)
[Get Free Body Forces and Moments (VB.NET)](Get_Free_Body_Forces_and_Moments_Example_VBNET.htm)
[Get Free Body Forces and Moments (C#)](Get_Free_Body_Forces_and_Moments_Example_CSharp.htm)

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetFreeBodyForcesAndMomentsForAStep Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetFreeBodyForcesAndMomentsForAStep.html)

## Availability

SOLIDWORKS Simulation API 2013 SP0
