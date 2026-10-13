---
title: "GetFreeBodyForcesAndMomentsForAStep Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetFreeBodyForcesAndMomentsForAStep"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetFreeBodyForcesAndMomentsForAStep.html"
---

# GetFreeBodyForcesAndMomentsForAStep Method (ICWResults)

Gets the x-, y-, and z-component and resultant free body forces and moments for the specified entities for the specified step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFreeBodyForcesAndMomentsForAStep( _
   ByVal DispPlane As System.Object, _
   ByVal SelectedRefPoint As System.Object, _
   ByVal ArraySelectedEntities As System.Object, _
   ByVal NUnits As System.Integer, _
   ByVal NStepNumber As System.Integer, _
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
Dim NStepNumber As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetFreeBodyForcesAndMomentsForAStep(DispPlane, SelectedRefPoint, ArraySelectedEntities, NUnits, NStepNumber, ErrorCode)
```

### C#

```csharp
System.object GetFreeBodyForcesAndMomentsForAStep(
   System.object DispPlane,
   System.object SelectedRefPoint,
   System.object ArraySelectedEntities,
   System.int NUnits,
   System.int NStepNumber,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetFreeBodyForcesAndMomentsForAStep(
   System.Object^ DispPlane,
   System.Object^ SelectedRefPoint,
   System.Object^ ArraySelectedEntities,
   System.int NUnits,
   System.int NStepNumber,
   [Out] System.int ErrorCode
)
```

### Parameters

- `DispPlane`: Plane, axis, or coordinate system relative to which the results are listed
- `SelectedRefPoint`: Reference point used to list the moments for the forces that are available in ArraySelectedEntities; NULL to not list the moments
- `ArraySelectedEntities`: Selected faces, edges, vertices, and components
- `NUnits`: Output units as defined in [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)
- `NStepNumber`: Step number
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

See [CWResults::GetFreeBodyForcesAndMomentsForAStep](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetFreeBodyForcesAndMomentsForAStep.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetFreeBodyForcesAndMoments Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetFreeBodyForcesAndMoments.html)

## Availability

SOLIDWORKS Simulation API 2020 SP0
