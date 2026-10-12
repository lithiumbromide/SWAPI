---
title: "Copy Component With Profile Center Mate Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_Component_With_Profile_Center_Mate_Example_VB.htm"
---

# Copy Component With Profile Center Mate Example (VBA)

This example shows how to:

- create a new assembly.
- add two components to the assembly.
- create a profile center mate between the components.
- copy a component with that mate.

```
'--------------------------------------------------------
' Preconditions:
' 1. Open a new SOLIDWORKS Design session.
' 2. Copy public_documents\samples\tutorial\api\block20.sldprt and
'    cylinder20.sldprt to c:\temp.
' 3. Verify that the specified assembly document template exists.
'
' Postconditions:
' 1. Opens both parts.
' 2. Creates a new assembly.
' 3. Inserts both parts into the new assembly.
' 4. Creates a profile center mate between the two components.
' 5. Copies a component and the profile center mate.
' 6. To verify steps 4 and 5:
'    * Examine the graphics area and FeatureManager design tree.
'    * Expand Mates in the FeatureManager design tree.
'---------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swPart1 As SldWorks.PartDoc
Dim swPart2 As SldWorks.PartDoc
Dim swModel As SldWorks.ModelDoc2
Dim swAssemblyDoc As SldWorks.AssemblyDoc
Dim swComponent1 As SldWorks.Component2
Dim swComponent2 As SldWorks.Component2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swMate As SldWorks.Mate2
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim swComponentArray(0) As SldWorks.Component2
Dim repeatArray(0) As Boolean
Dim mateReferencesArray(0) As Object
Dim valueArray(0) As Double
Dim flipAlignmentArray(0) As Boolean
Dim flipDimensionArray(0) As Boolean
Dim lockRotationArray(0) As Boolean
Dim orientationArray(0) As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Open parts for new assembly
    Set swPart1 = swApp.OpenDoc6("C:\temp\block20.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swPart2 = swApp.OpenDoc6("C:\temp\cylinder20.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

    'Open new assembly document
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Assembly.asmdot", 0, 0, 0)
    swApp.ActivateDoc2 "Assem1", False, errors
    Set swAssemblyDoc = swModel
```

```
    ' Add components to assembly document
    Set swComponent1 = swAssemblyDoc.AddComponent5("C:\temp\block20.sldprt", swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", False, "", 5.22792702800426E-02, 6.58677995643489E-02, 0.102016044707081)
    Set swComponent2 = swAssemblyDoc.AddComponent5("C:\temp\cylinder20.sldprt", swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", False, "", 0.177061497059185, -1.51244836160913E-03, 6.73233033157885E-02)
    swModel.ViewZoomtofit2
```

```
    ' Add profile center mate
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("", "FACE", 6.31695178495306E-02, 8.56797995642182E-02, 0.137370061843797, True, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", 0.141204290267694, 0.031253551638315, 8.43440006535161E-02, True, 1, Nothing, 0)
    Set swMate = swAssemblyDoc.AddMate5(swMateType_e.swMatePROFILECENTER, swMateAlign_e.swMateAlignALIGNED, True, 0.0762, 0.0254, 0.0254, 0.0254, 0.0254, 0, 0.5235987755983, 0.5235987755983, False, True, swMateWidthOptions_e.swMateWidth_Centered, errors)
    swModel.ClearSelection2 True

    ' Copy component with profile center mate
    Set swComponentArray(0) = swComponent2
    repeatArray(0) = True
    Set mateReferencesArray(0) = Nothing
    valueArray(0) = 0.05
    flipAlignmentArray(0) = True
    flipDimensionArray(0) = True
    lockRotationArray(0) = False
    orientationArray(0) = 0
    status = swAssemblyDoc.CopyWithMates2(swComponentArray, repeatArray, mateReferencesArray, valueArray, flipAlignmentArray, flipDimensionArray, lockRotationArray, orientationArray)
```

```
End Sub
```
