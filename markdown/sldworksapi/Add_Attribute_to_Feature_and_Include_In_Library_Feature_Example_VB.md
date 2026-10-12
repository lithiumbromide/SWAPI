---
title: "Add Attribute to Feature and Include In Library Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Attribute_to_Feature_and_Include_In_Library_Feature_Example_VB.htm"
---

# Add Attribute to Feature and Include In Library Feature Example (VBA)

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
```

```
Option Explicit
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelectionMgr As SldWorks.SelectionMgr
    Dim swFeature As SldWorks.Feature
    Dim swAttribute As SldWorks.Attribute
    Dim swAttributeDef As SldWorks.AttributeDef
    Dim swFace As SldWorks.Face2
    Dim swParameter as SldWorks.Parameter
    Dim Faces As Variant
    Dim bool As Boolean
```

```
    Sub main()
```

```
        Set swApp = Application.SldWorks
        Set swModel = swApp.ActiveDoc
        Set swModelDocExt = swModel.Extension
        Set swSelectionMgr = swModel.SelectionManager
```

```
        ' Create attribute
        Set swAttributeDef = swApp.DefineAttribute("TestPropagationOfAttribute")
        bool = swAttributeDef.AddParameter("TestAttribute", swParamTypeDouble, 2#, 0)
        bool = swAttributeDef.Register

        ' Select the feature to which to add the attribute
        bool = swModelDocExt.SelectByID2("Cut-Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        Debug.Print ("Name of feature to which to add attribute: " & swFeature.Name)
```

```
        ' Add the attribute to one of the feature's faces
        Faces = swFeature.GetFaces
        Set swFace = Faces(0)
        Set swAttribute = swAttributeDef.CreateInstance5(swModel, swFace, "TestAttribute", 0, swAllConfiguration)
        swAttribute.IncludeInLibraryFeature = True
        Debug.Print ("Include attribute in library feature? " & swAttribute.IncludeInLibraryFeature)
        Debug.Print ("Name of attribute: " & swAttribute.GetName)
```

```
        ' Add the attribute to one of the feature's faces
        Set swParameter = swAttribute.GetParameter("TestAttribute")
        Debug.Print ("Name of parameter: " & swParameter.GetName)
```

```
        swModel.ForceRebuild3 (False)
```

```
End Sub
```
