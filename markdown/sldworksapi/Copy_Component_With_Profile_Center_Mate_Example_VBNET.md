---
title: "Copy Component With Profile Center Mate Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_Component_With_Profile_Center_Mate_Example_VBNET.htm"
---

# Copy Component With Profile Center Mate Example (VB.NET)

This example shows how to:

- create a new assembly.
- add two components to the assembly.
- create a profile center mate between the components.
- copy a component with that mate.

```
'--------------------------------------------------------
' Preconditions:
' 1. Open a new SOLIDWORKS Design session.
' 2. Copy install_dir\samples\tutorial\api\block20.sldprt and
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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swPart1 As PartDoc
        Dim swPart2 As PartDoc
        Dim swModel As ModelDoc2
        Dim swAssemblyDoc As AssemblyDoc
        Dim swComponent1 As Component2
        Dim swComponent2 As Component2
        Dim swModelDocExt As ModelDocExtension
        Dim swMate As Mate2
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim dispWrapperComponentArray(0) As DispatchWrapper
        Dim swComponentArray(0) As Component2
        Dim repeatArray(0) As Boolean
        Dim dispWrapperMateReferencesArray(0) As DispatchWrapper
        Dim valueArray(0) As Double
        Dim flipAlignmentArray(0) As Boolean
        Dim flipDimensionArray(0) As Boolean
        Dim lockRotationArray(0) As Boolean
        Dim orientationArray(0) As Integer

        ' Open parts for new assembly
        swPart1 = swApp.OpenDoc6("C:\temp\block20.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swPart2 = swApp.OpenDoc6("C:\temp\cylinder20.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        ' Open new assembly document
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Assembly.asmdot", 0, 0, 0)
        swApp.ActivateDoc2("Assem1", False, errors)
        swAssemblyDoc = swModel

        ' Add components to assembly document
        swComponent1 = swAssemblyDoc.AddComponent5("C:\temp\block20.sldprt", swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", False, "", 0.0522792702800426, 0.0658677995643489, 0.102016044707081)
        swComponent2 = swAssemblyDoc.AddComponent5("C:\temp\cylinder20.sldprt", swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", False, "", 0.177061497059185, -0.00151244836160913, 0.0673233033157885)
        swModel.ViewZoomtofit2()

        ' Add profile center mate
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("", "FACE", 0.0631695178495306, 0.0856797995642182, 0.137370061843797, True, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", 0.141204290267694, 0.031253551638315, 0.0843440006535161, True, 1, Nothing, 0)
        swMate = swAssemblyDoc.AddMate5(swMateType_e.swMatePROFILECENTER, swMateAlign_e.swMateAlignALIGNED, True, 0.0762, 0.0254, 0.0254, 0.0254, 0.0254, 0, 0.5235987755983, 0.5235987755983, False, True, swMateWidthOptions_e.swMateWidth_Centered, errors)
        swModel.ClearSelection2(True)

        ' Copy component with profile center mate
        swComponentArray(0) = swComponent2
        dispWrapperComponentArray(0) = New DispatchWrapper(swComponentArray(0))
        repeatArray(0) = True
        dispWrapperMateReferencesArray(0) = New DispatchWrapper(Nothing)
        valueArray(0) = 0.05
        flipAlignmentArray(0) = True
        flipDimensionArray(0) = True
        lockRotationArray(0) = False
        orientationArray(0) = 0
        status = swAssemblyDoc.CopyWithMates2(dispWrapperComponentArray, repeatArray, dispWrapperMateReferencesArray, valueArray, flipAlignmentArray, flipDimensionArray, lockRotationArray, orientationArray)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
