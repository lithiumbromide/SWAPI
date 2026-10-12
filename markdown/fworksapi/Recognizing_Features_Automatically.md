---
title: "Recognizing Features Automatically (VBA)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "fworksapi/Recognizing_Features_Automatically.htm"
---

# Recognizing Features Automatically (VBA)

This sample application illustrates recognizing features automatically in a SOLIDWORKS part document, and then creating those features.

```vb
Sub main()
Dim swApp As Object
Dim sample As Object
Dim Part As Object
Dim boolstatus As Boolean
Dim inp As Boolean

Dim str1 As String
' Get the SOLIDWORKS object
Set swApp = CreateObject("SldWorks.Application")

' CLSID of FeatureWorks : 16B0AE50-0817-11d7-A7F8-0006299907FB
' Get the FeatureWorks object
Set sample = swApp.GetAddInObject("FeatureWorks.FeatureWorksApp")

Dim varOut As Variant
Dim var1 As Boolean
Dim unused As Integer
Dim options As Long

unused = 0
Dim str1 As String
' Get the SOLIDWORKS part document
Set Part = swApp.ActiveDoc
' Select the faces to fillet
boolstatus = Part.Extension.SelectByID("", "FACE", 0.1023433561252, 0.06999999999994, 0.05499949188089, False, 8, Nothing)

' Turn on the specified automatic feature recognition options
option = fwChamfils + fwExtrudeOption
varOut = sample.RecognizeFeatureAutomatic(option )

' Create the recognized features
createOption = fwAllowFailFeatureCreation 'Option to allow creation of features with reubild errors
var1 = sample.CreateFeatures(createOption)
End Sub
```
