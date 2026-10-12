---
title: "Add Attribute to Feature and Include in Library Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_VBNET.htm"
---

# Add Attribute to Feature and Include in Library Feature Example (VB.NET)

This example shows how to add an attribute to a feature and include that attribute with the feature if the feature is saved as a library feature. This example also includes instructions on how to verify that the attribute is included on each instance of the library feature.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Open a new part document.
' 2. Sketch a rectangle and extrude it.
' 3. Sketch a straight slot that fits on a face of
'    of the just-created extrude and cut-extrude the slot.
'
'    NOTE: The cut-extrude feature must be named Cut-Extrude1.
'
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Adds the cut-extrude feature to the part document with
'    an attribute of TestAttribute, which is visible in the
'    FeatureManager design tree.
' 2. Examine the Immediate window.
' 3. To verify that the attribute is included in a library feature:
'    a. Click Design Library on the Task Pane.
'       1. Click Add to Library.
'       2. Click Cut-Extrude1 in the flyout FeatureManager design tree.
'       3. Type a file name for the library feature.
'       4. Select the folder where to save the library feature.
'       5. Click OK.
'    b. Open an existing model document and drag-and-drop the
'       just-created library feature on the model and click OK.
'    c. Expand the just-dropped library feature in the FeatureManager
'       design tree to verify that Cut-Extrude1 and TestAttribute appear
'       beneath the just-dropped library feature in the FeatureManager
'       design tree.
'-------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Diagnostics
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelectionMgr As SelectionMgr
        Dim swFeature As Feature
        Dim swAttribute As SolidWorks.Interop.sldworks.Attribute
        Dim swAttributeDef As AttributeDef
        Dim swFace As Face2
        Dim swParameter as Parameter
        Dim Faces As Object
        Dim bool As Boolean

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension
        swSelectionMgr = swModel.SelectionManager

        ' Create attribute
        swAttributeDef = swApp.DefineAttribute("TestPropagationOfAttribute")
        bool = swAttributeDef.AddParameter("TestAttribute", swParamType_e.swParamTypeDouble, 2.0#, 0)
        bool = swAttributeDef.Register

        ' Select the feature to which to add the attribute
        bool = swModelDocExt.SelectByID2("Cut-Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        Debug.Print("Name of feature to which to add attribute: " & swFeature.Name)

        ' Add the attribute to one of the feature's faces
        Faces = swFeature.GetFaces
        swFace = Faces(0)
        swAttribute = swAttributeDef.CreateInstance5(swModel, swFace, "TestAttribute", 0, swInConfigurationOpts_e.swAllConfiguration)
        swAttribute.IncludeInLibraryFeature = True
        Debug.Print("Include attribute in library feature? " & swAttribute.IncludeInLibraryFeature)
        Debug.Print("Name of attribute: " & swAttribute.GetName)
```

```
        ' Get name of parameter
        swParameter = swAttribute.GetParameter("TestAttribute")
        Debug.Print("Name of parameter: " & swParameter.GetName)

        swModel.ForceRebuild3(False)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
