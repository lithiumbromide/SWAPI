---
title: "Get What's Wrong Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_What's_Wrong_Example_VBNET.htm"
---

# Get What's Wrong Example (VB.NET)

This example shows how to get the What's Wrong information for a document.

```vb
'-----------------------------------
' Preconditions: Model document is active. Examine the Immediate
'                window after running this macro to see the What's Wrong
'                items in the model document.
'
' Postconditions: None
'------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
```

```vb
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim vFeatures As Object = Nothing
        Dim vErrorCodes As Object = Nothing
        Dim vWarnings As Object = Nothing
        Dim boolstatus As Boolean
        Dim i As Integer
        Dim nbrWhatsWrong As Integer
        Dim swFeature As Feature

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension
        nbrWhatsWrong = swModelDocExt.GetWhatsWrongCount
        Debug.Print("Number of What's Wrong items: " & nbrWhatsWrong)
        Debug.Print("")
        If nbrWhatsWrong > 0 Then
            boolstatus = swModelDocExt.GetWhatsWrong(vFeatures, vErrorCodes, vWarnings)
            For i = 0 To UBound(vFeatures)
                swFeature = vFeatures(i)
                Debug.Print("  Name of feature: " & swFeature.GetTypeName2)
                Debug.Print("  Error: " & vErrorCodes(i))
                Debug.Print("  Did SOLIDWORKS Design flag this item as a warning ? " & vWarnings(i))
                Debug.Print("")
            Next i
        Else
            Debug.Print("No What's Wrong items.")
        End If
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
