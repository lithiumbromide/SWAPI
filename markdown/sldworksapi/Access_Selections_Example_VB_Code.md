---
title: "Access Selections Example (VBA) - Code"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Access_Selections_Example_VB_Code.htm"
---

# Access Selections Example (VBA) - Code

This example doubles the length of the base extrude.

```vb
Dim swApp As SldWorks.SldWorks
Dim Model As ModelDoc2
Dim Component As Component2
Dim CurFeature As Feature
Dim isGood As Boolean
' Will become an ExtrudeFeatureData Object
Dim FeatData As Object
Dim Depth As Double
Dim SelMgr As SelectionMgr

Sub main()
    Set swApp = CreateObject("sldWorks.application")
    Set Model = swApp.ActiveDoc
    ' Make sure that the active document is a part
    If Model.GetType <> swDocPART And Model.GetType <> swDocASSEMBLY Then
        Msg = "Only allowed on parts or assemblies" ' Define message
        Style = vbOKOnly ' OK button only
        Title = "Error" ' Define title
        Call MsgBox(Msg, Style, Title) ' Display error message
        Exit Sub ' Exit this program
    End If

    ' Get the SelectionManager
    Set SelMgr = Model.SelectionManager

    ' Get the selected object (first in the group if there are more than one)
    ' At this point CurFeature is just a Feature object
    Set CurFeature = SelMgr.GetSelectedObject6(1, 0)
    If CurFeature Is Nothing Then
        ' Tell the user that nothing is selected
        swApp.SendMsgToUser2 "Please select the Base-Extrude.", swMbWarning, swMbOk
        Exit Sub
    End If
    ' Get the component of the selected feature
    ' Needed for AccessSelections()
    Set Component = SelMgr.GetSelectedObjectsComponent3(1, 0)

    ' Check the feature's type name
    ' Make sure it is an extrusion
    If Not CurFeature.GetTypeName = "Extrusion" Then
        swApp.SendMsgToUser2 "Please select the Base-Extrude.", swMbWarning, swMbOk
        Exit Sub
    End If

    ' Get the extrusion's FeatureData object
    Set FeatData = CurFeature.GetDefinition

   ' Get the access selections for the FeatureData object
   ' The component is NULL when accessing the selections of a standalone part
   ' If you are calling AccessSelections from within an assembly, then model
   ' would refer to the top-level document in the assembly and component
   ' would refer to the actual part
    isGood = FeatData.AccessSelections(Model, Component)

    ' Inform the user of an error
    If Not isGood Then
        swApp.SendMsgToUser2 "Unable to obtain access selections.", swMbWarning, swMbOk
        Exit Sub
    End If

    ' Change the depth of this extrusion to double its previous depth
    Depth = FeatData.GetDepth(True)
    FeatData.SetDepth True, Depth * 2

    ' Implement the changes to the feature
    isGood = CurFeature.ModifyDefinition(FeatData, Model, Component)

    ' If the modify definition failed
    If Not isGood Then
        swApp.SendMsgToUser2 "Unable to modify feature.", swMbWarning, swMbOk
        ' Release the selections
        FeatData.ReleaseSelectionAccess
    End If

End Sub
```
