---
title: "Switch Documents Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Switch_Documents_Example_VB.htm"
---

# Switch Documents Example (VBA)

## Switch Documents (VBA)

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
' 2. Click Window on the main menu to see a list of the
'    open documents.
' 3. Press F5 to continue.
' 4. Closes all open documents.
' 5. Examine the Immediate window.
'----------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModelDoc As SldWorks.ModelDoc2
Dim swFrame As SldWorks.Frame
Dim swModelWindow As SldWorks.ModelWindow
Dim modelWindows As Variant
Dim obj As Variant
Dim errors As Long
Dim warnings As Long
Dim HWnd As Long
Dim fileName As String
Dim strFolder As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open the specified documents in their own windows
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\assemblymates\knee.sldprt"
    Set swModelDoc = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    'Open client model window containing the active document
    swApp.CreateNewWindow
```

```
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\assemblymates\bracket.sldprt"
    Set swModelDoc = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    'Open client model window containing the active document
    swApp.CreateNewWindow
```

```
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\assemblymates\clamp.sldprt"
    Set swModelDoc = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    'Open client model window containing the active document
    swApp.CreateNewWindow
```

```
    Set swFrame = swApp.Frame
    modelWindows = swFrame.modelWindows
    Debug.Print "Open documents in their own windows:"
    For Each obj In modelWindows
        Set swModelWindow = obj
        'Get the model document in this model window
        Set swModelDoc = swModelWindow.ModelDoc
        'Rebuild the document
        swModelDoc.EditRebuild3
        Set swModelDoc = Nothing
        'Show the model window
        Debug.Print ""
        swFrame.ShowModelWindow swModelWindow
        'Get and print the model window handle
        HWnd = swModelWindow.HWnd
        Debug.Print ("  Model window handle: " & HWnd)
        'Get and print the model title as it is seen in the model window's title bar
        Debug.Print ("  Model title as it seen in the model's window's title bar: " & swModelWindow.Title)
    Next obj
```

```
    Stop
    'Click Window on the main menu to see a list of the
    'open documents in their own windows
    'Press F5 to continue
```

```
    strFolder = ""
    'Specify true to close all documents, specify false to close
    'only the documents not modified
    swApp.CloseAllDocuments True
```

```
End Sub
```
