---
title: "Create Library Feature Data Object and Library Feature With References Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Library_Feature_With_References_Example_VB.htm"
---

# Create Library Feature Data Object and Library Feature With References Example (VBA)

This example shows how to create a library feature with references in order to position the library feature on a model.

```
'-------------------------------------------------------------------
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
'------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchManager As SldWorks.SketchManager
Dim swFeature As SldWorks.Feature
Dim swFeatureManager As SldWorks.FeatureManager
Dim swSelectionManager As SldWorks.SelectionMgr
Dim swLibFeat As SldWorks.LibraryFeatureData
Dim sketchLines As Variant
Dim status As Boolean
Dim obj() As Object
Dim vRefs As Variant
Dim vRefTypes As Variant
Dim refType As Variant
Dim nRefCount As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Create part
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
    status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
    Set swSketchManager = swModel.SketchManager
    sketchLines = swSketchManager.CreateCornerRectangle(0, 0, 0, 1, 0.5, 0)
```

```
    swModel.ShowNamedView2 "*Trimetric", 8
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    Set swFeatureManager = swModel.FeatureManager
    Set swFeature = swFeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.01, 0.01, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)
    Set swSelectionManager = swModel.SelectionManager
    swSelectionManager.EnableContourSelection = False
```

```
    ' Create library feature data object
    Set swLibFeat = swFeatureManager.CreateDefinition(swFmLibraryFeature)
```

```
    ' Initialize newly created library feature using the specified library part
    status = swLibFeat.Initialize("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2016\design library\features\metric\slots\straight slot.sldlfp")
```

```
    ' Get the type of references required for the library feature
    nRefCount = swLibFeat.GetReferencesCount
    vRefs = swLibFeat.GetReferences2(swLibFeatureData_FeatureRespect, vRefTypes)
    If Not IsEmpty(vRefTypes) Then
        Debug.Print "Types of references required (edge = 1): "
        For Each refType In vRefTypes
            Debug.Print "   " & CStr(refType)
        Next
    End If
```

```
    ' Set the name of the active library feature configuration
    swLibFeat.ConfigurationName = "Default"
```

```
    ' Select the face where to create the library feature
     status = swModelDocExt.SelectByID2("", "FACE", 0.522458766456054, 0.288038964184011, 9.99999999987722E-03, False, 0, Nothing, 0)
```

```
   ' Create the library feature
    Set swFeature = swFeatureManager.CreateFeature(swLibFeat)
```

```
    ' Access the library feature to position it on the part
    Set swLibFeat = Nothing
    Set swLibFeat = swFeature.GetDefinition
    status = swLibFeat.AccessSelections(swModel, Nothing)
```

```
    ' Select the edges where to position the library feature
    status = swModelDocExt.SelectByID2("", "EDGE", 0.960865149149924, 0.497807163546383, 1.31011390528215E-02, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "EDGE", 0.99866860703213, 0.481385806014544, 1.13313929676906E-02, True, 0, Nothing, 0)
```

```
    Dim selCount As Long
    selCount = swSelectionManager.GetSelectedObjectCount2(-1)
    selCount = selCount - 1
    ReDim obj(selCount) As Object
    Dim i As Long
    For i = 0 To selCount
        Set obj(i) = swSelectionManager.GetSelectedObject6(i + 1, -1)
    Next
```

```
    ' Set the references for positioning the library feature on the part
    Dim vLibRefs As Variant
    vLibRefs = obj
    swLibFeat.SetReferences (vLibRefs)
```

```
    ' Update the definition of the library feature
    status = swFeature.ModifyDefinition(swLibFeat, swModel, Nothing)
```

```
    ' Unsuppress the library feature
    status = swModelDocExt.SelectByID2("straight slot<1>", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    swModel.EditUnsuppress2
```

```
    swModel.ClearSelection2 True
```

```
End Sub
```
