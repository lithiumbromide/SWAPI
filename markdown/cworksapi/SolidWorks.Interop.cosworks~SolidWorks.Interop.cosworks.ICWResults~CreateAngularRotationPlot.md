---
title: "CreateAngularRotationPlot Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "CreateAngularRotationPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateAngularRotationPlot.html"
---

# CreateAngularRotationPlot Method (ICWResults)

Creates an angular rotation plot for the specified reference axis.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateAngularRotationPlot( _
   ByVal NUnits As System.Integer, _
   ByVal DispReferenceAxis As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWPlot
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NUnits As System.Integer
Dim DispReferenceAxis As System.Object
Dim ErrorCode As System.Integer
Dim value As CWPlot

value = instance.CreateAngularRotationPlot(NUnits, DispReferenceAxis, ErrorCode)
```

### C#

```csharp
CWPlot CreateAngularRotationPlot(
   System.int NUnits,
   System.object DispReferenceAxis,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWPlot^ CreateAngularRotationPlot(
   System.int NUnits,
   System.Object^ DispReferenceAxis,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NUnits`: Units of angular rotation as defined in [swsRotationUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRotationUnit_e.html)
- `DispReferenceAxis`: Reference axis for angular rotation (see **Remarks**)
- `ErrorCode`: Error code as defined by [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

### Return Value

[ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)

## VBA Syntax

See [CWResults::CreateAngularRotationPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~CreateAngularRotationPlot.html).

## Examples

'----------------------------------------------------

'Preconditions:

' 1. Open a model that has:

' - A reference axis about which angular rotation can be measured (rename it Axis1 or create a reference axis, Axis1, after the model is opened.)

' - A static or non-linear study defined with:

' - Material applied to the model

' - A Fixture

' - An External Load

'

'Postconditions:

'1. Study is meshed and run.

'2. Displacement1 (-Ang disp-)is created.

'3. Examine the graphics area.

'-------------------------------------------------

Dim SwApp As SldWorks.SldWorks

Dim Part As SldWorks.ModelDoc2

Dim boolstatus As Boolean

Option Explicit

Sub main()

Set SwApp = Application.SldWorks

Set Part = SwApp.ActiveDoc

Dim COSMOSWORKSObj As Object

Dim CWAddinCallBackObj As Object

Dim StudyManagerObj As Object

Dim ActiveDocObj As Object

Set CWAddinCallBackObj = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")

Set COSMOSWORKSObj = CWAddinCallBackObj.COSMOSWORKS

Dim LoadsAndRestraintsManagerObj As Object

Dim ErrorCodeObj As Long

Dim ContactManagerObj As Object

Set ActiveDocObj = COSMOSWORKSObj.ActiveDoc()

Set StudyManagerObj = ActiveDocObj.StudyManager()

StudyManagerObj.ActiveStudy = 0

Dim StudyObj As Object

Set StudyObj = StudyManagerObj.**GetStudy**(0)

ErrorCodeObj = StudyObj.**CreateMesh**(2, 0.00255069, 0.00255069)

ErrorCodeObj = StudyObj.**RunAnalysis**()

Part.GraphicsRedraw2

boolstatus = Part.Extension.SelectByID2("Axis1", "AXIS", 0, 0, 0, True, 0, Nothing, 0)

Dim DispatchObj As Object

Set DispatchObj = Part.SelectionManager.GetSelectedObject6(1, -1)

Dim ResultPlotObj As Object

Part.GraphicsRedraw2

Dim StudyResultsObj As Object

Set StudyResultsObj = StudyObj.**Results**

'Dim nUnit As Long

'nUnit = swsRotationUnit_e.swsRotationUnit_Degrees

'Create angular rotation plot

Set ResultPlotObj = StudyResultsObj.**CreateAngularRotationPlot**(0, DispatchObj, ErrorCodeObj)

'Activate plot

Dim ActivationStatus As Boolean

Dim SPlotName As String

Dim value As Long

value = ResultPlotObj.**GetPlotName**(SPlotName)

ActivationStatus = StudyResultsObj.**ActivatePlot**(SPlotName)

'Get min/max angle from plot

Dim minmax As Variant

minmax = ResultPlotObj.**GetMinMaxResultValues**(ErrorCodeObj)

End Sub

## Remarks

DispReferenceAxis is a required parameter.

The angular rotation plot is a displacement plot that is only available for static and non-linear studies. This method creates an angular rotation plot, but only if the following prerequisites are satisfied:

- A model with a reference axis for angular rotation is open. (Browse the `public_documents`**\samples\Simulation Examples** folders for a suitable model with angular rotation potential, e.g., **tutor1.sldprt**.)
- A static or non-linear study exists for the model.
- The study has material applied to the model, a fixture, and an external load.
- The study is meshed and analyzed successfully.

To create an angular rotation plot from the user interface:

1. Open a model that contains a reference axis for angular rotation of the model.
2. Load the Simulation add-in.
3. Create a static study with the following:

  1. Brass material applied to the model.
  2. A Fixed Geometry fixture on the face of the model.
  3. An external Torque load of 100 N.m. applied to a face of the model.
4. Mesh and run the study.
5. RMB on the Results folder and select **Define Displacement Plot**.
6. In the Displacement plot PMP, on the Definition tab, select AR: Angular Rotation in the Display dropdown.
7. Click on Advanced Options - Axis. In the graphics area select the angular rotation reference axis for the model.
8. Click **OK** (green check mark).

For more information about angular rotation plots, see the **Simulation user-interface help > Viewing Analysis Results > Plotting Results > Displacement Plot PropertyManager** topics.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0
