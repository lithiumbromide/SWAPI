---
title: "Recognizing Features Interactively (VBA)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "fworksapi/Recognizing_Features_Interactively.htm"
---

# Recognizing Features Interactively (VBA)

This sample application illustrates recognizing a feature interactively in a SOLIDWORKS part document, and then creating that feature.

```vb
Sub main()
    Dim swApp As Object
    Dim sample As Object
    Dim Part As Object
    Dim boolstatus As Boolean

    Dim str As String
    Set swApp = Application.SldWorks
    swApp.SetUserPreferenceIntegerValue swAutoSaveInterval, 0

    Set sample = swApp.GetAddInObject("FeatureWorks.FeatureWorksApp")
    Dim varOut As Variant
    Dim var1 As Boolean

    Set Part = swApp.ActiveDoc

    Set Part = swApp.ActiveDoc
    boolstatus = Part.Extension.SelectByID("", "FACE", 0.1165311335518, -0.006695921966639, 0.03257260156937, False, 0, Nothing)
    Dim InterOption As Integer
    str = "Fillet" 'Option to recognize interactive fillet
    InterOption = fwChainFeatures 'Turn on the chaining option.
    varOut = sample.RecognizeFeatureInteractive(str, InterOption)
    If (False = varOut) Then MsgBox ("ERROR")
    createOption = fwAllowFailFeatureCreation 'Option to allow creation of features with rebuild errors
    var1 = sample.CreateFeatures(createOption)
If (False = var1) Then MsgBox ("ERROR")
End Sub
```
