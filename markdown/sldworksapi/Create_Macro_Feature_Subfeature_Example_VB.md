---
title: "Create Macro Feature Subfeature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Macro_Feature_Subfeature_Example_VB.htm"
---

# Create Macro Feature Subfeature Example (VBA)

This example shows how to create a macro feature subfeature.

```vb
'---------------------------------------------------------------------------
'
' Preconditions: Model document is open and a sketch is selected.
'
' Postconditions: The sketch becomes a subfeature of the newly
'                 created macro feature named EmptyFeature.
'
' NOTE: A bitmap named FeatureIcon.bmp for the macro feature must exist.
'
'----------------------------------------------------------------------------
'Macro feature Rebuild routine
Function swmRebuild(varApp As Variant, varDoc As Variant, varFeat As Variant) As Variant
    Dim App As SldWorks.SldWorks
    Dim Doc As SldWorks.ModelDoc2
    Dim feat As SldWorks.Feature
    Dim FeatData As SldWorks.MacroFeatureData
    Dim Rebuild As Boolean

    Set App = varApp
    Set Doc = varDoc
    Set feat = varFeat

    'MsgBox "Rebuild called"

    Rebuild = True
    'If an error occurs
    'Rebuild = "Error message"
End Function

'Macro feature Edit definition routine
Function swmEditDefinition(varApp As Variant, varDoc As Variant, varFeat As Variant) As Variant
    Dim App As SldWorks.SldWorks
    Dim Doc As SldWorks.ModelDoc2
    Dim feat As SldWorks.Feature
    Dim FeatData As SldWorks.MacroFeatureData

    Set App = varApp
    Set Doc = varDoc
    Set feat = varFeat

    MsgBox "Edit Definition called"

    Set FeatData = varFeat.GetDefinition
    varFeat.ModifyDefinition FeatData, varDoc, Nothing
    EditDefinition = True
End Function

'Macro feature Security routine
Function swmSecurity(varApp As Variant, varDoc As Variant, varFeat As Variant) As Variant
    Dim App As SldWorks.SldWorks
    Dim Doc As SldWorks.ModelDoc2
    Dim feat As SldWorks.Feature
    Dim FeatData As SldWorks.MacroFeatureData

    Set App = varApp
    Set Doc = varDoc
    Set feat = varFeat

    swmSecurity = SwConst.swMacroFeatureSecurityOptions_e.swMacroFeatureSecurityByDefault
End Function

'Base routine to create the macro feature
Sub CreateSampleFeature()
    Dim swApp As SldWorks.SldWorks
    Dim Doc As SldWorks.ModelDoc2
    Dim feat As Feature
    Dim SelMan As SelectionMgr

    Set swApp = Application.SldWorks
    Set Doc = swApp.ActiveDoc
    Set SelMan = Doc.SelectionManager

    Dim ThisFile As String
    Dim Methods(8) As String
    Dim Names As Variant
    Dim Types As Variant
    Dim Values As Variant
    Dim vEditBodies As Variant
    Dim options As Long
    Dim dimTypes As Variant
    Dim dimValue As Variant
    Dim icons(2) As String

    'Define the routines to call
    ThisFile = swApp.GetCurrentMacroPathName
    Methods(0) = ThisFile: Methods(1) = "FeatureModule": Methods(2) = "swmRebuild"
    Methods(3) = ThisFile: Methods(4) = "FeatureModule": Methods(5) = "swmEditDefinition"
    Methods(6) = "": Methods(7) = "": Methods(8) = ""  'A security routine is optional

    Dim pathname As String
    pathname = swApp.GetCurrentMacroPathFolder
    icons(0) = pathname + "\FeatureIcon.bmp"
    icons(1) = pathname + "\FeatureIcon.bmp"
    icons(2) = pathname + "\FeatureIcon.bmp"

    Names = Empty
    Types = Empty
    Values = Empty

    options = swMacroFeatureByDefault

    Dim selFeat As Feature
    Dim swFeatMgr As SldWorks.FeatureManager
    Set selFeat = SelMan.GetSelectedObject6(1, -1)
    Set swFeatMgr = Doc.FeatureManager

    Set feat = swFeatMgr.InsertMacroFeature3("EmptyFeature", "", (Methods), Names, Types, Values, dimTypes, dimValue, vEditBodies, (icons), options)

    Dim boolstatus As Boolean
    boolstatus = feat.MakeSubFeature(selFeat)
End Sub
```
