---
title: "GetLinearizedStressValues Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetLinearizedStressValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetLinearizedStressValues.html"
---

# GetLinearizedStressValues Method (ICWResults)

Obsolete. Superseded by [ICWPlot::GetLinearizedStressValuesAlongSCL](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~GetLinearizedStressValuesAlongSCL.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLinearizedStressValues( _
   ByVal NComponent As System.Integer, _
   ByVal DPoint1X As System.Double, _
   ByVal DPoint1Y As System.Double, _
   ByVal DPoint1Z As System.Double, _
   ByVal DPoint2X As System.Double, _
   ByVal DPoint2Y As System.Double, _
   ByVal DPoint2Z As System.Double, _
   ByVal NIntermPoints As System.Integer, _
   ByVal NUnits As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NComponent As System.Integer
Dim DPoint1X As System.Double
Dim DPoint1Y As System.Double
Dim DPoint1Z As System.Double
Dim DPoint2X As System.Double
Dim DPoint2Y As System.Double
Dim DPoint2Z As System.Double
Dim NIntermPoints As System.Integer
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetLinearizedStressValues(NComponent, DPoint1X, DPoint1Y, DPoint1Z, DPoint2X, DPoint2Y, DPoint2Z, NIntermPoints, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetLinearizedStressValues(
   System.int NComponent,
   System.double DPoint1X,
   System.double DPoint1Y,
   System.double DPoint1Z,
   System.double DPoint2X,
   System.double DPoint2Y,
   System.double DPoint2Z,
   System.int NIntermPoints,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetLinearizedStressValues(
   System.int NComponent,
   System.double DPoint1X,
   System.double DPoint1Y,
   System.double DPoint1Z,
   System.double DPoint2X,
   System.double DPoint2Y,
   System.double DPoint2Z,
   System.int NIntermPoints,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Stress component for which to get linearized values (see **Remarks**)
- `DPoint1X`: X coordinate of first point on the section view (see **Remarks**)
- `DPoint1Y`: Y coordinate of first point on the section view (see **Remarks**)
- `DPoint1Z`: Z coordinate of first point on the section view (see **Remarks**)
- `DPoint2X`: X coordinate of second point on the section view (see **Remarks**)
- `DPoint2Y`: Y coordinate of second point on the section view (see **Remarks**)
- `DPoint2Z`: Z coordinate of second point on the section view (see **Remarks**)
- `NIntermPoints`: Number of intermediate points between the points specified by DPoint1X, DPoint1Y, DPoint1Z, DPoint2X, DPoint2Y, and DPoint2Z to define the resolution of the line
- `NUnits`: Units as defined in [swsStrengthUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStrengthUnit_e.html) (see **Remarks**)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of seven linearized membrane and bending stress values for the specified NComponent (see **Remarks**)

## VBA Syntax

See [CWResults::GetLinearizedStressValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetLinearizedStressValues.html).

## Remarks

Before calling this method:

1. Create a pressure vessel study using the results of two static studies.
2. Analyse the pressure vessel study to generate a stress results plot.
3. Create a planar section view of the stress results plot.

  1. Right-click the stress results plot and click **Section Clipping** to open the Section PropertyManager.
  2. In Section 1, click **Plane**.
  3. In Options, click **Union** and select **Show mesh on section plane** and **Plot on section only**.
  4. Click **OK**.
4. Specify DPoint1X, DPoint1Y, DPoint1Z, DPoint2X, DPoint2Y, DPoint2Z with the coordinates of two points on the planar section view you created in step 3.
5. Specify NComponent with one of the following values:

- 0 = Normal stress in X-direction
- 1 = Normal stress in Y-direction
- 2 = Normal stress in Z-direction
- 3 = Shear stress in the Y direction acting in the YZ plane
- 4 = Shear stress in the Z direction acting in the YZ plane
- 5 = Shear stress in the Z direction acting in the XZ plane
- 6 = Von Mises stress
- 7 = Stress intensity (P1 - P3)
- 8 = Normal stress in the first principal direction (P1)
- 9 = Normal stress in the second principal direction (P2)
- 10 = Normal stress in the third principal direction (P3)

The returned array contains the following seven values in the specified NUnits for the specified NComponent:

{ `membrane_stress`, `bending_point_1`, (`membrane_stress` + `bending_point_1`), `bending_point_2`, (`membrane_stress` + `bending_point_2`), `peak_point_1`, `peak_point_2` }

**NOTE:** This method is valid only for solid meshes.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
