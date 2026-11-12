---
title: "Switch Documents Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Switch_Documents_Example_VBNET.htm"
---

# Switch Documents Example (VB.NET)

This example shows how to switch documents by opening documents in their own and client model windows.

```
'----------------------------------------------
' Preconditions:
' 1. Verify that the specified documents to open exist.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified documents in their own
'    and client model windows.
' 2. Closes all open documents.
' 3. Examine the Immediate window.
'----------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModelDoc As ModelDoc2
        Dim swFrame As Frame
        Dim swModelWindow As ModelWindow
        Dim modelWindows() As Object
        Dim obj As Object
        Dim errors As Integer
        Dim warnings As Integer
        Dim HWnd As Integer
        Dim fileName As String
        Dim strFolder As String

        'Open the specified documents in their own windows
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\assemblymates\knee.sldprt"
        swModelDoc = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        'Open client model window containing the active document
        swApp.CreateNewWindow()

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\assemblymates\bracket.sldprt"
        swModelDoc = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        'Open client model window containing the active document
        swApp.CreateNewWindow()

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\assemblymates\clamp.sldprt"
        swModelDoc = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        'Open client model window containing the active document
        swApp.CreateNewWindow()

        swFrame = swApp.Frame
        modelWindows = swFrame.ModelWindows
        Debug.Print("Open documents in their own windows:")
        For Each obj In modelWindows
            swModelWindow = obj
            'Get the model document in this model window
            swModelDoc = swModelWindow.ModelDoc
            'Rebuild the document
            swModelDoc.EditRebuild3()
            swModelDoc = Nothing
            'Show the model window
            Debug.Print("")
            swFrame.ShowModelWindow(swModelWindow)
            'Get and print the model window handle
            HWnd = swModelWindow.HWnd
            Debug.Print("  Model window handle: " & HWnd)
            'Get and print the model title as it is seen in the model window's title bar
            Debug.Print("  Model title as it seen in the model's window's title bar: " & swModelWindow.Title)
        Next obj

        strFolder = ""
        'Specify true to close all documents, specify false to close
        'only the documents not modified
        swApp.CloseAllDocuments(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
