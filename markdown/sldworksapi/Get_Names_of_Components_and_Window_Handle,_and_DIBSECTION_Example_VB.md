---
title: "Get Names of Components, Window Handles, and DIBSECTIONs Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VB.htm"
---

# Get Names of Components, Window Handles, and DIBSECTIONs Example (VBA)

This example shows how to get:

- names of the assembly components in an open, inactive, assembly document.
- window handles and pointers to images of model documents.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified model documents to open exist.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified model documents.
' 2. Prints to the Immediate window:
'    *  paths and file names of:
'       * assembly components of the open, inactive, assembly document
'       * open, active, part document
'       * open, inactive, assembly document
'    *  whether the assembly components, part, and assembly documents
'       are visible
' 3. Prints to the Immediate window each visible document's:
'    * Microsoft window handle
'    * pointer to its image as it looks in Normal view
'      or in the print preview
' 4. Examine the Immediate window.
'
' NOTE: Because the models are used elsewhere, do not save changes.
'-------------------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModView As SldWorks.ModelView
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
```

```
    Set swApp = Application.SldWorks
```

```
    'Open assembly document, then open part document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\bowl and chute.sldasm"
    swApp.OpenDoc6 fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\switch.sldprt"
    swApp.OpenDoc6 fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings
```

```
    'NOTE: Assembly components are open, but they
    'are not visible until opened by the user.
```

```
    'Get first open document
    Set swModel = swApp.GetFirstDocument
```

```
    Do While Not swModel Is Nothing
        Debug.Print swModel.GetPathName
        'Get whether assembly component, part, or assembly is visible
        Debug.Print "    Visible? " & swModel.Visible
        Set swModView = swModel.ActiveView
        Do While Not swModView Is Nothing

            'NOTE: Model views exist only for visible model documents.

            'Get Microsoft window handle and pointer to image
            'for each visible model document
            '64-bit SOLIDWORKS
            Debug.Print "    Microsoft window handle = " & swModView.GetViewHWndx64
            Debug.Print "    Pointer to image = " & swModView.GetViewDIBx64
```

```
            Set swModView = swModView.GetNext
        Loop
        'Get next open document
        Set swModel = swModel.GetNext
    Loop
```

```
End Sub
```
