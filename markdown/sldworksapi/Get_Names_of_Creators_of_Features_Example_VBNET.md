---
title: "Get Names of Creators of Features Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Names_of_Creators_of_Features_Example_VBNET.htm"
---

# Get Names of Creators of Features Example (VB.NET)

This example shows how to get the names of the creators of features in a part document.

```
'-------------------------------------------------
' Preconditions:
' 1. Verify that the specified part exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the names feature and their creators.
' 2. Examine the Immediate window.
'-------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swFeat As Feature
        Dim Filename As String
        Dim errors As Integer
        Dim warnings As Integer

        Filename = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cstick.sldprt"

        ' Open document
        swApp.OpenDoc6(Filename, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModel = swApp.ActiveDoc

        ' Get first feature in this part document
        swFeat = swModel.FirstFeature

        ' Iterate over features in this part document in
        ' FeatureManager design tree

        Do While Not swFeat Is Nothing
            ' Write the name of the feature and its
            ' creator to the Immediate window
            Debug.Print("  Feature " & swFeat.Name & " created by " & swFeat.CreatedBy)

            ' Get next feature in this part document
            swFeat = swFeat.GetNextFeature
        Loop

        swApp.CloseDoc(Filename)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
