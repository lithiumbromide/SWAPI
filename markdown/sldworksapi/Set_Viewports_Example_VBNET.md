---
title: "Set Viewports Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Viewports_Example_VBNET.htm"
---

# Set Viewports Example (VB.NET)

This example shows how to set viewports and check and change whether they're linked.

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\introtosw\pressure_plate.sldprt.
' 2. Set some breakpoints (e.g., before and after panning the viewports).
' 3. Open the Immediate window.
' 4. Press F5 at each breakpoint.
'
' Postconditions:
' 1. Sets viewport arrangement to Two View-Horizontal (* Top viewport is
'    panned; bottom viewport also panned because it is linked to top
'    viewport).
' 3. Unlinks viewports (Top viewport is panned; bottom view isn't panned
'    because viewports were unlinked).
' 4. Sets viewport arrangement to a single viewport.
' 5. Examine the Immediate window.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'--------------------------------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelViewManager As ModelViewManager
        Dim swModelView As ModelView

        swModel = swApp.ActiveDoc

        ' Set the viewport arrangement to Two View-Horizontal
        Debug.Print("Set viewport arrangement to Two View-Horizontal...")
        swModelViewManager = swModel.ModelViewManager
        swModelViewManager.ViewportDisplay = swViewportDisplay_e.swViewportTwoViewHorizontal

        ' Check to see if the viewports are linked
        Debug.Print("Are viewports linked? " & swModelViewManager.LinkedViews)

        ' Pan the model in the top viewport
        ' The model in the bottom viewport also pans
        ' because it's linked to the top viewport
        Debug.Print("Panning the model in top viewport; model in bottom viewport also pans because the viewports are linked...")
        swModelView = swModel.ActiveView
        swModelView.TranslateBy(-0.0005535897435897, 0)
        swModelView.TranslateBy(-0.0005535897435897, 0)
        swModelView.TranslateBy(-0.0005535897435897, 0.0005535897435897)
        swModelView.TranslateBy(-0.003875128205128, 0.001660769230769)
        swModelView.TranslateBy(-0.004982307692308, 0.0005535897435897)
        swModelView.TranslateBy(-0.005535897435897, 0.0005535897435897)
        swModelView.TranslateBy(-0.007196666666667, 0)
        swModelView.TranslateBy(-0.006089487179487, 0)
        swModelView.TranslateBy(-0.006643076923077, 0)
        swModelView.TranslateBy(-0.004982307692308, 0)
        swModelView.TranslateBy(-0.005535897435897, 0)
        swModelView.TranslateBy(-0.002214358974359, 0)
        swModelView.TranslateBy(-0.0005535897435897, 0)
        swModelView.TranslateBy(0, -0.0005535897435897)
        swModelView.TranslateBy(0, -0.001107179487179)
        swModelView.TranslateBy(0.001107179487179, -0.002214358974359)
        swModelView.TranslateBy(0.001660769230769, -0.004982307692308)
        swModelView.TranslateBy(0.002214358974359, -0.006643076923077)
        swModelView.TranslateBy(0.001660769230769, -0.006089487179487)
        swModelView.TranslateBy(0.001107179487179, -0.003321538461538)
        swModelView.TranslateBy(0, -0.001107179487179)
        swModelView.TranslateBy(0, 0.0005535897435897)
        swModelView.TranslateBy(0, 0.001107179487179)
        swModelView.TranslateBy(0.0005535897435897, 0.0005535897435897)
        swModelView.TranslateBy(0.001107179487179, 0.003875128205128)
        swModelView.TranslateBy(0.002767948717949, 0.004428717948718)
        swModelView.TranslateBy(0.002214358974359, 0.006643076923077)
        swModelView.TranslateBy(0.002767948717949, 0.005535897435897)
        swModelView.TranslateBy(0.003875128205128, 0.006643076923077)
        swModelView.TranslateBy(0.002214358974359, 0.004428717948718)
        swModelView.TranslateBy(0, 0.001107179487179)
        swModelView.TranslateBy(-0.0005535897435897, 0)
        swModelView.TranslateBy(-0.0005535897435897, 0)
        swModelView.TranslateBy(-0.001660769230769, 0)
        swModelView.TranslateBy(-0.003875128205128, 0.0005535897435897)
        swModelView.TranslateBy(-0.01328615384615, 0.002767948717949)
        swModelView.TranslateBy(-0.01328615384615, 0.002767948717949)
        swModelView.TranslateBy(-0.0160541025641, 0.003321538461538)
        swModelView.TranslateBy(-0.01273256410256, 0.003321538461538)
        swModelView.TranslateBy(-0.006643076923077, 0.001660769230769)
        swModelView.TranslateBy(-0.002767948717949, 0.0005535897435897)
        swModelView.TranslateBy(0.0005535897435897, 0)
        swModelView.TranslateBy(0.002767948717949, 0)
        swModelView.TranslateBy(0.008857435897436, -0.0005535897435897)
        swModelView.TranslateBy(0.02435794871795, -0.001660769230769)
        swModelView.TranslateBy(0.03044743589744, -0.002214358974359)
        swModelView.TranslateBy(0.01826846153846, -0.004428717948718)
        swModelView.TranslateBy(0.01217897435897, -0.004982307692308)
        swModelView.TranslateBy(0.004428717948718, -0.004982307692308)
        swModelView.TranslateBy(0.001660769230769, -0.003875128205128)
        swModelView.TranslateBy(0, -0.001660769230769)
        swModelView.TranslateBy(0.0005535897435897, -0.0005535897435897)
        swModelView.TranslateBy(0.001660769230769, 0)
        swModelView.TranslateBy(0.002214358974359, 0)
        swModelView.TranslateBy(0.008303846153846, 0.001107179487179)
        swModelView.TranslateBy(0.009411025641026, 0.004428717948718)
        swModelView.TranslateBy(0.01328615384615, 0.008303846153846)
        swModelView.TranslateBy(0.003875128205128, 0.007750256410256)
        swModelView.TranslateBy(-0.002767948717949, 0.007750256410256)
        swModelView.TranslateBy(-0.006643076923077, 0.003875128205128)
        swModelView.TranslateBy(-0.006643076923077, 0)
        swModelView.TranslateBy(-0.006089487179487, 0)
        swModelView.TranslateBy(-0.008857435897436, 0)
        swModelView.TranslateBy(-0.006643076923077, -0.001107179487179)
        swModelView.TranslateBy(-0.002767948717949, -0.003321538461538)
        swModelView.TranslateBy(-0.001660769230769, -0.001660769230769)
        swModelView.TranslateBy(-0.0005535897435897, -0.001107179487179)
        swModelView.TranslateBy(0, -0.0005535897435897)
        swModelView.TranslateBy(0, 0.0005535897435897)
        swModelView.TranslateBy(0, 0.0005535897435897)

        ' Fit the model in each viewport
        swModel.ViewZoomtofit2()

        ' Unlink the viewports
        Debug.Print("Unlink the viewports...")
        swModelViewManager.LinkedViews = False
        Debug.Print("Are viewports linked? " & swModelViewManager.LinkedViews)

        ' Pan the model in the top viewport
        ' The model in the bottom viewport doesn't pan
        ' because it's no longer linked to the top viewport
        Debug.Print("Panning the model in top viewport; model in bottom viewport doesn't pan because the viewports are no longer linked...")
        swModelView = swModel.ActiveView
        swModelView.TranslateBy(-0.0005535897435897, 0)
        swModelView.TranslateBy(-0.0005535897435897, 0)
        swModelView.TranslateBy(-0.0005535897435897, 0.0005535897435897)
        swModelView.TranslateBy(-0.003875128205128, 0.001660769230769)
        swModelView.TranslateBy(-0.004982307692308, 0.0005535897435897)
        swModelView.TranslateBy(-0.005535897435897, 0.0005535897435897)
        swModelView.TranslateBy(-0.007196666666667, 0)
        swModelView.TranslateBy(-0.006089487179487, 0)
        swModelView.TranslateBy(-0.006643076923077, 0)
        swModelView.TranslateBy(-0.004982307692308, 0)
        swModelView.TranslateBy(-0.005535897435897, 0)
        swModelView.TranslateBy(-0.002214358974359, 0)
        swModelView.TranslateBy(-0.0005535897435897, 0)
        swModelView.TranslateBy(0, -0.0005535897435897)
        swModelView.TranslateBy(0, -0.001107179487179)
        swModelView.TranslateBy(0.001107179487179, -0.002214358974359)
        swModelView.TranslateBy(0.001660769230769, -0.004982307692308)
        swModelView.TranslateBy(0.002214358974359, -0.006643076923077)
        swModelView.TranslateBy(0.001660769230769, -0.006089487179487)
        swModelView.TranslateBy(0.001107179487179, -0.003321538461538)
        swModelView.TranslateBy(0, -0.001107179487179)
        swModelView.TranslateBy(0, 0.0005535897435897)
        swModelView.TranslateBy(0, 0.001107179487179)
        swModelView.TranslateBy(0.0005535897435897, 0.0005535897435897)
        swModelView.TranslateBy(0.001107179487179, 0.003875128205128)
        swModelView.TranslateBy(0.002767948717949, 0.004428717948718)
        swModelView.TranslateBy(0.002214358974359, 0.006643076923077)
        swModelView.TranslateBy(0.002767948717949, 0.005535897435897)
        swModelView.TranslateBy(0.003875128205128, 0.006643076923077)
        swModelView.TranslateBy(0.002214358974359, 0.004428717948718)
        swModelView.TranslateBy(0, 0.001107179487179)
        swModelView.TranslateBy(-0.0005535897435897, 0)
        swModelView.TranslateBy(-0.0005535897435897, 0)
        swModelView.TranslateBy(-0.001660769230769, 0)
        swModelView.TranslateBy(-0.003875128205128, 0.0005535897435897)
        swModelView.TranslateBy(-0.01328615384615, 0.002767948717949)
        swModelView.TranslateBy(-0.01328615384615, 0.002767948717949)
        swModelView.TranslateBy(-0.0160541025641, 0.003321538461538)
        swModelView.TranslateBy(-0.01273256410256, 0.003321538461538)
        swModelView.TranslateBy(-0.006643076923077, 0.001660769230769)
        swModelView.TranslateBy(-0.002767948717949, 0.0005535897435897)
        swModelView.TranslateBy(0.0005535897435897, 0)
        swModelView.TranslateBy(0.002767948717949, 0)
        swModelView.TranslateBy(0.008857435897436, -0.0005535897435897)
        swModelView.TranslateBy(0.02435794871795, -0.001660769230769)
        swModelView.TranslateBy(0.03044743589744, -0.002214358974359)
        swModelView.TranslateBy(0.01826846153846, -0.004428717948718)
        swModelView.TranslateBy(0.01217897435897, -0.004982307692308)
        swModelView.TranslateBy(0.004428717948718, -0.004982307692308)
        swModelView.TranslateBy(0.001660769230769, -0.003875128205128)
        swModelView.TranslateBy(0, -0.001660769230769)
        swModelView.TranslateBy(0.0005535897435897, -0.0005535897435897)
        swModelView.TranslateBy(0.001660769230769, 0)
        swModelView.TranslateBy(0.002214358974359, 0)
        swModelView.TranslateBy(0.008303846153846, 0.001107179487179)
        swModelView.TranslateBy(0.009411025641026, 0.004428717948718)
        swModelView.TranslateBy(0.01328615384615, 0.008303846153846)
        swModelView.TranslateBy(0.003875128205128, 0.007750256410256)
        swModelView.TranslateBy(-0.002767948717949, 0.007750256410256)
        swModelView.TranslateBy(-0.006643076923077, 0.003875128205128)
        swModelView.TranslateBy(-0.006643076923077, 0)
        swModelView.TranslateBy(-0.006089487179487, 0)
        swModelView.TranslateBy(-0.008857435897436, 0)
        swModelView.TranslateBy(-0.006643076923077, -0.001107179487179)
        swModelView.TranslateBy(-0.002767948717949, -0.003321538461538)
        swModelView.TranslateBy(-0.001660769230769, -0.001660769230769)
        swModelView.TranslateBy(-0.0005535897435897, -0.001107179487179)
        swModelView.TranslateBy(0, -0.0005535897435897)
        swModelView.TranslateBy(0, 0.0005535897435897)
        swModelView.TranslateBy(0, 0.0005535897435897)

        ' Change the viewport arrangement back to a single viewport
        swModelViewManager.ViewportDisplay = swViewportDisplay_e.swViewportSingle

        ' Fit the model in the viewport
        swModel.ViewZoomtofit2()

    End Sub
    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
