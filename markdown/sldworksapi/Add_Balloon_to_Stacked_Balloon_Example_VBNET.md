---
title: "Add Balloon to Stacked Balloon Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Balloon_to_Stacked_Balloon_Example_VBNET.htm"
---

# Add Balloon to Stacked Balloon Example (VB.NET)

This example shows how to create a stacked balloon and add a balloon to the stacked balloon.

```
'------------------------------------------------------------
' Preconditions: Verify that the specified assembly
' document to open exists.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Selects a face on the Part4 component.
' 3. Creates a stacked balloon showing the item number
'    of Part4 and inserts that stacked balloon on the selected face.
' 4. Adds a balloon, which shows the number of seed and derived Part4
'    components in the the assembly, to the stacked balloon.
' 5. Click and drag the stacked balloon upward in the graphics area.
'------------------------------------------------------------
```

```
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swStackedBalloons As StackedBalloonOptions
        Dim swNote As Note
        Dim swBalloonStack As BalloonStack
        Dim swNote2 As Note
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\assem2.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension

        swModel.ViewZoomtofit2()

        status = swModelDocExt.SelectByID2("", "FACE", -0.311973500811291, 0.0329693343254007, 0.00999999999999091, False, 0, Nothing, 0)
        swStackedBalloons = swModelDocExt.CreateStackedBalloonOptions()
        swStackedBalloons.BalloonsPerLine = 10
        swStackedBalloons.StackDirection = swStackedBalloonDirection_e.swStackedBalloonDir_Right
        swStackedBalloons.Style = swBalloonStyle_e.swBS_Circular
        swStackedBalloons.Size = swBalloonFit_e.swBF_2Chars
        swStackedBalloons.UpperTextContent = swBalloonTextContent_e.swBalloonTextItemNumber
        swStackedBalloons.UpperText = """"
        swStackedBalloons.ShowQuantity = False
        swStackedBalloons.QuantityPlacement = swBalloonQuantityPlacement_e.swBalloonQuantityPlacement_Top
        swStackedBalloons.QuantityDenotationText = "X"
        swStackedBalloons.QuantityOverride = False
        swNote = swModelDocExt.InsertStackedBalloon2(swStackedBalloons)
        status = swModelDocExt.SelectByID2("", "FACE", -0.292957708052256, 0.0316192505406434, 0.0100000000000477, False, 0, Nothing, 0)

        If swNote.IsStackedBalloon Then
            If Not swNote Is Nothing Then
                swBalloonStack = swNote.GetBalloonStack()
                swNote2 = swBalloonStack.AddTo(swBalloonTextContent_e.swBalloonTextQuantity, "12", swBalloonTextContent_e.swBalloonTextQuantity, "")
            End If
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
