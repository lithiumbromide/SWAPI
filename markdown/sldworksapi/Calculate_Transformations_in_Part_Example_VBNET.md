---
title: "Calculate Transformations in Part Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Calculate_Transformations_in_Part_Example_VBNET.htm"
---

# Calculate Transformations in Part Example (VB.NET)

This example shows how to calculate transformations between solid bodies in a part, which would make one solid body coincide with another solid body if the transformation matrix is applied.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Ensure that the specified part file to
'    open exists.
' 2. Open the Immediate window.
' 3. Run the macro.
'
' Postconditions:
' 1. Opens the specified part file.
' 2. Gets the solid bodies in the specified part file.
' 3. Iterates through the solid bodies in the part
'    and calculates transformations between solid
'    bodies.
' 4. Examine the Immediate window.
'----------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelMgr As SelectionMgr
        Dim file As String
        Dim status As Integer
        Dim warnings As Integer

        file = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\routing-pipes\routes\Framework (Done).SLDPRT"
        swModel = swApp.OpenDoc6(file, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", status, warnings)
        If swModel Is Nothing Then Exit Sub

        swModelDocExt = swModel.Extension
        swSelMgr = swModel.SelectionManager
        Dim swPart As PartDoc
        swPart = swModel

        Dim bodies As Object
        Dim swBody_A As Body2
        Dim swBody_B As Body2

        'Get solid bodies
        Dim bodyType As swBodyType_e
        Dim visibleOnly As Boolean
        bodyType = swBodyType_e.swSolidBody
        visibleOnly = True
        bodies = swPart.GetBodies2(bodyType, visibleOnly)
        'Iterate through the solid bodies in the part
        'and calculate the transformation matrix between
        'swBody_A and swBody_B
        If Not (IsNothing(bodies)) Then
            Dim i As Integer
            Dim j As Integer
            Dim maxIndex As Integer
            maxIndex = UBound(bodies)
            For i = 0 To maxIndex
                swBody_A = bodies(i)
                For j = 0 To maxIndex
                    If i <> j Then
                        swBody_B = bodies(j)

                        Dim swXfm As MathTransform
                        Dim bResult As Boolean
                        swXfm = Nothing
                        bResult = False
                        bResult = swBody_A.GetCoincidenceTransform2(swBody_B, swXfm)

                        Debug.Print(i & " -> " & j, swBody_A.Name & " -> " & swBody_B.Name)

                        If bResult <> False Then
                            Debug.Print(vbTab & "Can coincide.")
                            Dim vXfm As Object
                            vXfm = swXfm.ArrayData
                            Debug.Print(vbTab & "Rotation:")
                            Debug.Print(vbTab & vXfm(0), vXfm(1), vXfm(2))
                            Debug.Print(vbTab & vXfm(3), vXfm(4), vXfm(5))
                            Debug.Print(vbTab & vXfm(6), vXfm(7), vXfm(8))
                            Debug.Print(vbTab & "Translation:")
                            Debug.Print(vbTab & vXfm(9), vXfm(10), vXfm(11))
                            Debug.Print(vbTab & "Scaling: " & vXfm(12))

                        Else
                            Debug.Print(vbTab & "Cannot coincide.")
                        End If
                    End If
                Next j
            Next i
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
