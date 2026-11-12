---
title: "Traverse Features By Reverse Position Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_Features_By_Reverse_Position_Example_VBNET.htm"
---

# Traverse Features By Reverse Position Example (VB.NET)

This example shows how to traverse backwards through the list of features in the FeatureManager design tree. Features are obtained by their position using IModelDoc2::FeatureByPositionReverse.

```
'------------------------------------
' Preconditions:
' 1. A part document is open in SOLIDWORKS Design.
' 2. Open the Immediate window.
' 3. Run the macro.
'
' Postconditions: Examine the Immediate window for
' the position and names of the features in the
' FeatureManager design tree in reverse
' chronological order.
'--------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Runtime.InteropServices
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim Part As ModelDoc2
    Dim theFeature As Feature
    Dim featCount As Integer
    Dim featName As String
    Dim i As Integer

    Sub Main()

        Part = swApp.ActiveDoc

        featCount = Part.GetFeatureCount
        For i = featCount To 1 Step -1
            theFeature = Part.FeatureByPositionReverse(featCount - i)
            If Not theFeature Is Nothing Then
                featName = theFeature.Name
                Debug.Print("Feature " + Str(i) + " is " + featName)
            End If
        Next

        Part = Nothing

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
