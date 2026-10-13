---
title: "Create Library Feature Data Object and Library Feature With References Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Library_Feature_With_References_Example_VBNET.htm"
---

# Create Library Feature Data Object and Library Feature With References Example (VB.NET)

This example shows how to create a library feature with references in order to position the library feature on a model.

```
'------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template and library feature
'    exist.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a new part containing a boss extrude.
' 2. Creates a library feature data object.
'    a. Initializes the newly created library feature using
'       the specified library feature.
'    b. Gets the type of references required for the library
'       feature.
'    c. Sets the name of the active library feature configuration.
'    d. Selects the face where to create the library feature.
'    e. Creates the library feature.
'    f. Accesses the library feature and selects the edges where to
'       position the it.
'    g. Sets the references for positioning the library feature.
'    h. Updates the definition of the library feature.
'    i. Unsuppresses the library feature.
' 3. Examine the Immediate window, FeatureManager design tree, and
'    graphics area.
'-------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Imports System.Runtime.InteropServices

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swFeature As Feature
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchManager As SketchManager
        Dim swSelectionManager As SelectionMgr
        Dim swFeatureManager As FeatureManager
        Dim swLibFeat As LibraryFeatureData
        Dim status As Boolean
        Dim sketchLines() As Object
        Dim selectedObjects() As Object
        Dim Refs As Object = Nothing
        Dim RefTypes As Object = Nothing
        Dim RefType As Object
        Dim RefCount As Integer
        Dim LibRefs() As DispatchWrapper

        ' Create part
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
        swSketchManager = swModel.SketchManager
        sketchLines = swSketchManager.CreateCornerRectangle(0, 0, 0, 1, 0.5, 0)
        swModel.ShowNamedView2("*Trimetric", 8)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        swFeatureManager = swModel.FeatureManager
        swFeature = swFeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.01, 0.01, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, True, True, True, 0, 0, False)
        swSelectionManager = swModel.SelectionManager
        swSelectionManager.EnableContourSelection = False

        ' Create library feature
        swLibFeat = swFeatureManager.CreateDefinition(swFeatureNameID_e.swFmLibraryFeature)

        ' Initialize newly created library feature using the specified library part
        status = swLibFeat.Initialize("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2016\design library\features\metric\slots\straight slot.sldlfp")

        ' Get the type of references required for the library feature
        RefCount = swLibFeat.GetReferencesCount
        Refs = swLibFeat.GetReferences2(swLibFeatureData_e.swLibFeatureData_FeatureRespect, RefTypes)

        If Not IsNothing(RefTypes) Then
            Debug.Print("Types of references required (edge = 1): ")
            For Each RefType In RefTypes
                Debug.Print(vbTab + CStr(RefType))
            Next
        End If

        ' Set the name of the active library feature configuration
        swLibFeat.ConfigurationName = "Default"

        ' Select the face where to create the library feature
        status = swModelDocExt.SelectByID2("", "FACE", 0.522458766456054, 0.288038964184011, 0.00999999999987722, False, 0, Nothing, 0)

        ' Create the library feature
        swFeature = swFeatureManager.CreateFeature(swLibFeat)

        ' Access the library feature to position it on the part
        swLibFeat = Nothing
        swLibFeat = swFeature.GetDefinition
        status = swLibFeat.AccessSelections(swModel, Nothing)

        ' Select the edges where to position the library feature
        status = swModelDocExt.SelectByID2("", "EDGE", 0.960865149149924, 0.497807163546383, 0.0131011390528215, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.99866860703213, 0.481385806014544, 0.0113313929676906, True, 0, Nothing, 0)

        Dim selCount As Integer
        selCount = swSelectionManager.GetSelectedObjectCount2(-1)

        ReDim selectedObjects(selCount)

        Dim i As Integer
        For i = 0 To (selCount - 1)
            selectedObjects(i) = swSelectionManager.GetSelectedObject6(i + 1, -1)
        Next i

        ReDim Preserve selectedObjects(selCount - 1)

        ' Convert the .NET array to IDispatch
        LibRefs = ObjectArrayToDispatchWrapperArray(selectedObjects)

        ' Set the references for positioning the library feature on the part
        swLibFeat.SetReferences(LibRefs)

        ' Update the definition of the library feature
        status = swFeature.ModifyDefinition(swLibFeat, swModel, Nothing)

        ' Unsuppress the library feature
        status = swModelDocExt.SelectByID2("straight slot<1>", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.EditUnsuppress2()

        swModel.ClearSelection2(True)

    End Sub

    Function ObjectArrayToDispatchWrapperArray(ByVal Objects As Object()) As DispatchWrapper()
        Dim ArraySize As Integer
        ArraySize = Objects.GetUpperBound(0)
        Dim d(ArraySize) As DispatchWrapper
        Dim ArrayIndex As Integer
        For ArrayIndex = 0 To ArraySize
            d(ArrayIndex) = New DispatchWrapper(Objects(ArrayIndex))
        Next
        Return d
    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
