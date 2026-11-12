---
title: "GetLinearizedStressValuesAlongSCL Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "GetLinearizedStressValuesAlongSCL"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~GetLinearizedStressValuesAlongSCL.html"
---

# GetLinearizedStressValuesAlongSCL Method (ICWPlot)

Calculates the membrane and bending stresses between the specified points on a planar section view of this pressure vessel stress plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLinearizedStressValuesAlongSCL( _
   ByVal NIntermediatePoints As System.Integer, _
   ByVal DPoint1X As System.Double, _
   ByVal DPoint1Y As System.Double, _
   ByVal DPoint1Z As System.Double, _
   ByVal DPoint2X As System.Double, _
   ByVal DPoint2Y As System.Double, _
   ByVal DPoint2Z As System.Double, _
   ByVal DispReferencePlane As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim NIntermediatePoints As System.Integer
Dim DPoint1X As System.Double
Dim DPoint1Y As System.Double
Dim DPoint1Z As System.Double
Dim DPoint2X As System.Double
Dim DPoint2Y As System.Double
Dim DPoint2Z As System.Double
Dim DispReferencePlane As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetLinearizedStressValuesAlongSCL(NIntermediatePoints, DPoint1X, DPoint1Y, DPoint1Z, DPoint2X, DPoint2Y, DPoint2Z, DispReferencePlane, ErrorCode)
```

### C#

```csharp
System.object GetLinearizedStressValuesAlongSCL(
   System.int NIntermediatePoints,
   System.double DPoint1X,
   System.double DPoint1Y,
   System.double DPoint1Z,
   System.double DPoint2X,
   System.double DPoint2Y,
   System.double DPoint2Z,
   System.object DispReferencePlane,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetLinearizedStressValuesAlongSCL(
   System.int NIntermediatePoints,
   System.double DPoint1X,
   System.double DPoint1Y,
   System.double DPoint1Z,
   System.double DPoint2X,
   System.double DPoint2Y,
   System.double DPoint2Z,
   System.Object^ DispReferencePlane,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NIntermediatePoints`: 0 < Number of intermediate points between the points specified by DPoint1X, DPoint1Y, DPoint1Z, DPoint2X, DPoint2Y, and DPoint2Z to define the resolution of the SCL axis < 100
- `DPoint1X`: X coordinate of Point 1 on the section view (see **Remarks**)
- `DPoint1Y`: Y coordinate of Point 1 on the section view (see **Remarks**)
- `DPoint1Z`: Z coordinate of Point 1 on the section view (see **Remarks**)
- `DPoint2X`: X coordinate of Point 2 on the section view (see **Remarks**)
- `DPoint2Y`: Y coordinate of Point 2 on the section view (see **Remarks**)
- `DPoint2Z`: Z coordinate of Point 2 on the section view (see **Remarks**)
- `DispReferencePlane`: Datum plane reference that creates a section view containing Point 1 and Point 2 (see **Remarks**)
- `ErrorCode`: Result code as defined in [swsResultStressLinearizationErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultStressLinearizationErrors_e.html)

### Return Value

Array of seven membrane and bending stress values that are linearized along Stress Classification Lines (SCL) (see **Remarks**)

## VBA Syntax

See [CWPlot::GetLinearizedStressValuesAlongSCL](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~GetLinearizedStressValuesAlongSCL.html).

## Examples

[Get Linearized Stress Results (VBA)](Get_Linearized_Stress_Results_Example_VB.htm)
[Get Linearized Stress Results (VB.NET)](Get_Linearized_Stress_Results_Example_VBNET.htm)
[Get Linearized Stress Results (C#)](Get_Linearized_Stress_Results_Example_CSharp.htm)

## Remarks

This method adheres to current ASME Pressure Vessel design codes (ASME BPVC Section VIII, Annex 5-A.4.1.2) for deriving the membrane, bending, and peak components of a stress distribution based on a local coordinate system that is defined by the orientation of Stress Classification Lines (SCL). In the SCL coordinate system, SCL axis (Tangential) is the x direction, the axis perpendicular to the section plane (Hoop) is the z direction, and the orthogonal axis (Normal) is the y direction.

This method calculates:

1. A membrane stress tensor that is comprised of the average of each stress component along the SCL.
2. Bending stresses for the hoop and normal components, but not for the tangential component that is parallel to the SCL. The bending stress tensor is comprised of the linear varying portion of each stress component along the SCL.
3. A peak stress tensor.
4. Three principal stresses (P1, P2, P3) at the ends of the SCL based on components of membrane and membrane + bending stress.
5. Equivalent stresses at the ends of the SCL based on components of membrane and membrane + bending stress.

Before calling this method:

1. Create a pressure vessel study by defining a Result Combination Setup of one static study with von Mises stress results.
2. Analyse the pressure vessel study to generate a von Mises stress results plot.
3. Specify DispReferencePlane using a reference plane that sections the stress plot.
4. Specify DPoint1X, DPoint1Y, DPoint1Z, DPoint2X, DPoint2Y, DPoint2Z with the coordinates of two points on a stress line of the section plane in step 3.

To locate valid points on the stress line of a section plane:

1. Make sure the document units are set to MKS in the graphics area.
2. Right-click the pressure vessel stress plot and select **Section Clipping**.
3. Specify Top for **Section 1 > Reference Entity**. Click OK.
4. Right-click the pressure vessel stress plot and select **Linearize**.
5. Select two points in the graphics area that fall on the sectioned plot, prefereably spanning the thickness. (The tangential line goes from the first location to the second. The hoop is the outward normal to the cutting plane. The normal completes the right--handed coordinate system.)
6. Specify 5 for **No of Intermediate Points**. Click **Calculate**.
7. Click **Save** and export results as a CSV file.
8. Open the CSV file in Excel.
9. Locate the coordinates of the start and end points of the stress line to be used to specify DPoint1X, DPoint1Y, DPoint1Z, DPoint2X, DPoint2Y, DPoint2Z. Be sure to specify DispReferencePlane using the same section plane used to locate the points.

The returned array contains the following seven values:

[ `membrane_stress`, `bending_point_1`, (`membrane_stress` + `bending_point_1`), `bending_point_2`, (`membrane_stress` + `bending_point_2`), `peak_point_1`, `peak_point_2` ]

**NOTE:** This method is valid only for solid meshes.

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)
[ICWResults::GetLinearizedStressValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetLinearizedStressValues.html)

## Availability

SOLIDWORKS Simulation API 2019 SP04
