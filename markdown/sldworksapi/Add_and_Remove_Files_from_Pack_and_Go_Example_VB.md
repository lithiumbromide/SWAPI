---
title: "Add and Remove Files from Pack and Go Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_and_Remove_Files_from_Pack_and_Go_Example_VB.htm"
---

# Add and Remove Files from Pack and Go Example (VBA)

This example shows how to add SOLIDWORKS, render reference, and
non-SOLIDWORKS files to Pack and Go. This example also shows how to remove a
non-SOLIDWORKS file from Pack and Go.

```
'-------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly exists.
' 2. Create c:\PackAndGo.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the names of SOLIDWORKS, render reference, and
'    non-SOLIDWORKS files for Pack and Go.
' 2. Gets the the name of non-SOLIDWORKS file to remove.
' 3. Packs up SOLIDWORKS, render reference, and
'    non-SOLIDWORKS files and copies them to c:\PackAndGo.
' 4. Examine c:\PackAndGo and the Immediate window.
'-------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swPackAndGo As SldWorks.PackAndGo
Dim openFile As String
Dim errors As Long
Dim warnings As Long
Dim status As Boolean
Dim pgFileNames As Variant
Dim i As Long
Dim renderReferences As Variant
Dim otherFiles(1) As String
Dim delOtherFiles(0) As String
Dim myPath As String
Dim statuses As Variant
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
```

```
' Open assembly document
openFile = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2025\samples\tutorial\EDraw\claw\claw-mechanism.sldasm"
Set swModel = swApp.OpenDoc6(openFile, swDocASSEMBLY, swOpenDocOptions_Silent, "", errors, warnings)
Set swModelDocExt = swModel.Extension
```

```
' Get Pack and Go object
Debug.Print "Pack and Go"
Set swPackAndGo = swModelDocExt.GetPackAndGo
```

```
' Get current paths and filenames of the assembly's documents
status = swPackAndGo.GetDocumentNames(pgFileNames)
Debug.Print ""
Debug.Print "  Add SOLIDWORKS files' paths and filenames: "
If (Not (IsEmpty(pgFileNames))) Then
    For i = 0 To UBound(pgFileNames)
        Debug.Print "    The path and filename is: " & pgFileNames(i)
    Next i
End If
```

```
' Set document paths and names for Pack and Go
status = swPackAndGo.SetDocumentSaveToNames(pgFileNames)
```

```
' Get the render stock references in this assembly
' and print them to the Immediate window
Debug.Print " "
renderReferences = swModelDocExt.GetRenderStockReferences
Debug.Print "  Add render references:"
For i = 0 To UBound(renderReferences)
    Debug.Print "    The path and filename is: " & renderReferences(i)
Next i
```

```
' Add render stock files to Pack and Go
status = swPackAndGo.AddExternalDocuments(renderReferences)
```

```
' Add other non-SOLIDWORKS files to Pack and Go
otherFiles(0) = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2025\samples\tutorial\edraw\claw\claw-mechanism.easm"
otherFiles(1) = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2025\samples\tutorial\edraw\claw\claw-mechanism.emodel_debugonly.xml"
Debug.Print " "
Debug.Print "  Add non-SOLIDWORKS files:"
For i = 0 To UBound(otherFiles)
    Debug.Print "    The path and filename is: " & otherFiles(i)
Next i
status = swPackAndGo.AddExternalDocuments(otherFiles)
```

```
' Remove one of the non-SOLIDWORKS files from Pack and Go
Debug.Print " "
Debug.Print "  Remove non-SOLIDWORKS file:"
delOtherFiles(0) = otherFiles(0)
Debug.Print "    The path and filename is: " & delOtherFiles(0)
status = swPackAndGo.RemoveExternalDocuments(delOtherFiles)
```

```
' Override path where to save documents
myPath = "c:\PackAndGo\"
status = swPackAndGo.SetSaveToName2(True, myPath)
```

```
' Pack and Go both SOLIDWORKS and non-SOLIDWORKS files
statuses = swModelDocExt.SavePackAndGo(swPackAndGo)
```

```
End Sub
```
