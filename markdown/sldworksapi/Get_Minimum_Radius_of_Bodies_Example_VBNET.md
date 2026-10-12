---
title: "Get Minimum Radius of Bodies Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Minimum_Radius_of_Bodies_Example_VBNET.htm"
---

# Get Minimum Radius of Bodies Example (VB.NET)

This example shows how to get the minimum radius of each body in a multibody part.

```
'----------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document
'    to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document as read only.
' 2. Gets the minimum radius of each body.
' 3. Examine the Immediate window.
'----------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swPart As PartDoc
        Dim bodies() As Object
        Dim vbody As Body2
        Dim radius As Double
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer
        Dim i As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_inter.sldprt"
        swPart = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_ReadOnly, "", errors, warnings)
        bodies = swPart.GetBodies2(swBodyType_e.swAllBodies, False)
        i = 1
        For Each vbody In bodies
            radius = vbody.MinimumRadius()
            Debug.Print(vbody.Name & "'s " & "minimum radius: " & radius)
            i = i + 1
        Next vbody

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
