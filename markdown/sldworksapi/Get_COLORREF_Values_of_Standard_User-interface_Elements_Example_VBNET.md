---
title: "Get COLORREF Values of Standard User-interface Elements (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_COLORREF_Values_of_Standard_User-interface_Elements_Example_VBNET.htm"
---

# Get COLORREF Values of Standard User-interface Elements (VB.NET)

This example shows how to get the COLORREF values of standard SOLIDWORKS Design user-interface elements.

```
'---------------------------------------------------------
' Preconditions: Open the Immediate window.
'
' Postconditions:
' 1. Prints the names of the SOLIDWORKS Design standard
'    user-interface, elements (dimensions, backgrounds,
'    drawing paper, sketch status, annotations, etc.) and
'    their COLORREF values to the Immediate window.
' 2. Examine the Immediate window.
'--------------------------------------------------------

Imports SolidWorks.Interop.sldworks

Imports SolidWorks.Interop.swconst

Imports System

Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swColorTable As ColorTable

        Dim standardCount As Integer

        Dim count As Integer

        Dim colorName As String

        Dim colorRef As Integer

        swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS
2010\templates\part.prtdot", 0, 0, 0)

        swColorTable = swApp.GetColorTable

        standardCount = swColorTable.GetStandardCount

        Debug.Print("SOLIDWORKS Design standard
user-interface element and COLORREF value:")

        ' Iterate through standard colors

        For count = 0 To (standardCount - 1)

            ' Get the entry name

            colorName = swColorTable.GetNameAtIndex(count)

            If colorName <> "" Then

                ' Get the
entry's COLORREF

                colorRef = swColorTable.GetColorRefAtIndex(count)

                Debug.Print("  " & colorName & " : " & colorRef)

            Else

            End If

        Next count

    End Sub

    ''' <summary>

    ''' The SldWorks swApp variable is pre-assigned for you.

    ''' </summary>

    Public swApp As SldWorks

End Class
```
