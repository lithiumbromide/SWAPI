---
title: "Suppress or Unsuppress Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Feature_Suppression_Example_VB.htm"
---

# Suppress or Unsuppress Feature Example (VBA)

This example shows how to suppress a feature in a part.

This example also shows how to perform a string comparison using Visual Basic. The first input parameter, searchStr, allows you to pass in a feature name or a portion of a feature name.

This macro cycles through all the features in the part and selects all features that contain the specified search string and suppresses those features.

```
'------------------------------------------------------
' Preconditions: Verify that the part to open exists.
'
' Postconditions:
' 1. Opens the part.
' 2. Suppresses the specified feature.
' 3. Examine the FeatureManager design tree and
'    graphics area.
'
' NOTE: Because the part is used elsewhere, do not save
' changes.
'-------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swPart As SldWorks.PartDoc
    Dim swFeature As SldWorks.Feature
    Dim featureName As String
    Dim action As String
    Dim fileName As String
    Dim searchStr As String
    Dim errors As Long
    Dim warnings As Long
    Dim msg As String
    Dim style As Long
    Dim title As String
    Dim status As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
```

```
    ' Attach to the active document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\bolt.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    searchStr = "chamf"
    action = "Suppress"    'Change to "Unsuppress" to unsuppress supressed features
```

```
    Set swModelDocExt = swModel.Extension
    Set swPart = swModel
```

```
    ' Exit if no model is active
    If swModel Is Nothing Then
        Exit Sub
    End If
```

```
    ' Do not allow drawings or assemblies
    If (swModel.GetType <> swDocPART) Then
        ' Define message
        msg = "Macro Only valid for parts"
        ' OK button only
        style = VbMsgBoxStyle.vbOKOnly
        ' Define title
        title = "Error"
        ' Display error message
        Call MsgBox(msg, style, title)
        ' Exit this program
        Exit Sub
    End If
```

```
    ' Get the first feature in part
    Set swFeature = swPart.FirstFeature
```

```
    ' While a valid feature
    Do While Not swFeature Is Nothing
        ' Get the name of the feature
        Let featureName = swFeature.Name
        ' See if the feature name contains search string
        If InStr(1, featureName, searchStr, 1) Then
            ' Select the feature
            status = swModelDocExt.SelectByID2(featureName, "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
            If (action = "Suppress") Then
                    status = swModel.EditSuppress2() ' Suppress the feature
                ElseIf (action = "Unsuppress") Then '
                    status = swModel.EditUnsuppress2() ' Unsuppress the feature
            End If
        End If
        Set swFeature = swFeature.GetNextFeature() ' Get the next feature
    Loop ' Continue looping until no more features
```

```
End Sub
```
