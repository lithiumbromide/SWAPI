---
title: "Get Features in Reverse Order Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Features_in_Reverse_Order_Example_VBNET.htm"
---

# Get Features in Reverse Order Example (VB.NET)

This example shows how to get the names and types of features in the FeatureManager design tree in reverse chronological order.

```
'--------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the names and types of features
'    in the FeatureManager design tree in
'    reverse chronological order.
' 2. Examine the Immediate window and
'    FeatureManager design tree.
'--------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Runtime.InteropServices
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swFeat As Feature
        Dim i As Integer

        swModel = swApp.ActiveDoc

        Debug.Print("File = " & swModel.GetPathName)
        Debug.Print("")
        Debug.Print("Feature Name and Type")
        Debug.Print("=====================")
        For i = 0 To swModel.GetFeatureCount - 1
            swFeat = swModel.FeatureByPositionReverse(i)
            If Not swFeat Is Nothing Then
                Debug.Print(swFeat.Name & " [" & swFeat.GetTypeName & "]")
            End If
        Next i

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
