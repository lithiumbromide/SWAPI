---
title: "Get Feature Type and Name Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Feature_Type_and_Name_Example_VBNET.htm"
---

# Get Feature Type and Name Example (VB.NET)

This example shows how to get the feature type and name of the selected feature for use with IModelDocExtension::SelectByID2.

```
'----------------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\floxpress\ball valve\ball_valve.sldasm.
' 2. Expand any component in the FeatureManager design tree
'    and select one of its features.
'
' Postconditions:
' 1. Gets the selected feature's type and name.
' 2. Examine the Immediate window.
'
' NOTE: Because this assembly document is used elsewhere, do not save changes.
'----------------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
```

```vb
 Partial Class SolidWorksMacro

     Public Sub main()

         Dim swModel As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
        Dim swSelMgr As SelectionMgr
         Dim swFeat As Feature
         Dim featName As String, featType As String

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swModelDocExt = swModel.Extension

         ' Get the selected feature
         swFeat = swSelMgr.GetSelectedObject6(1, -1)

         swModel.ClearSelection2(True)

         featType = ""
         featName = ""

         ' Get the feature's type and name
        featName = swFeat.GetNameForSelection(featType)
         swModelDocExt.SelectByID2(featName, featType, 0, 0, 0, True, 0, Nothing, 0)

         ' Print the feature's type and name
         ' to the Immediate window
         Debug.Print("Feature type: " & featType)
         Debug.Print("Feature name: " & featName)

     End Sub

    ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

End Class
```
