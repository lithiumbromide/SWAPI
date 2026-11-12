---
title: "Add Balloon to Stacked Balloon Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Balloon_to_Stacked_Balloon_Example_VB.htm"
---

# Add Balloon to Stacked Balloon Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swStackedBalloons As SldWorks.StackedBalloonOptions
Dim swNote As SldWorks.Note
Dim swBalloonStack As SldWorks.BalloonStack
Dim swNote2 As SldWorks.Note
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\assem2.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension

    swModel.ViewZoomtofit2
```

```
    status = swModelDocExt.SelectByID2("", "FACE", -0.311973500811291, 3.29693343254007E-02, 9.99999999999091E-03, False, 0, Nothing, 0)
    Set swStackedBalloons = swModelDocExt.CreateStackedBalloonOptions()
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
    Set swNote = swModelDocExt.InsertStackedBalloon2(swStackedBalloons)
    status = swModelDocExt.SelectByID2("", "FACE", -0.292957708052256, 3.16192505406434E-02, 1.00000000000477E-02, False, 0, Nothing, 0)

        If swNote.IsStackedBalloon Then
        If Not swNote Is Nothing Then
           Set swBalloonStack = swNote.GetBalloonStack()
           Set swNote2 = swBalloonStack.AddTo(swBalloonTextContent_e.swBalloonTextQuantity, "12", swBalloonTextContent_e.swBalloonTextQuantity, "")
        End If
    End If
```

```
End Sub
```
