---
title: "Pack and Go Part and Linked Equation Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Pack_and_Go_Part_and_Linked_Equation_Example_vb.htm"
---

# Pack and Go Part and Linked Equation Example (VBA)

## Pack and Go Part and Linked Equation Example(VBA)

This example shows how to determine if a part document includes any equations and whether those equations are linked files. The example also shows how to add the part document and any linked equations to Pack and Go.

```
'----------------------------------------
' Preconditions:
' 1. Verify that the specified part and equation documents
'    exist.
' 2. Verify that c:\temp exists.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Adds the part and linked equation documents
'    to Pack and Go and copies the files to
'    c:\temp.
' 3. To verify, examine c:\temp.
'
' NOTE: Because the model is used elsewhere,
' do not save changes.
'-----------------------------------------
```

```
Option Explicit
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swEqnMgr As SldWorks.EquationMgr
    Dim swPackAndGo As SldWorks.PackAndGo
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
    Dim i As Long
    Dim nCount As Long
    Dim eqnLinked As Boolean
    Dim pgFileNames As Variant
    Dim status As Boolean
    Dim statuses As Variant
    Dim myPath As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\microphonehousing.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print " "
```

```
    ' Get Equation manager object
    Set swEqnMgr = swModel.GetEquationMgr
```

```
    ' List the equations, get whether they're linked
    ' to files, make sure any equations are up to date,
    ' and get the paths where they're stored
    nCount = swEqnMgr.GetCount
    For i = 0 To nCount - 1
        Debug.Print "  Equation #" & i & " = " & swEqnMgr.Equation(i)
```

```
        eqnLinked = swEqnMgr.LinkToFile
        Debug.Print "  Equation linked to file? " & eqnLinked
```

```
        If eqnLinked Then
```

```
            'Make sure equations are up to date
             swEqnMgr.UpdateValuesFromExternalEquationFile

            'Get path and name of linked equation file
            Debug.Print "  Path and file name of linked equation: " & swEqnMgr.FilePath
        End If
    Next i
```

```
    Debug.Print " "
```

```
    ' Get Pack and Go object
    Debug.Print "  Pack and Go"
    Set swPackAndGo = swModelDocExt.GetPackAndGo
```

```
    ' Get current paths and names of the documents
    status = swPackAndGo.GetDocumentNames(pgFileNames)
    Debug.Print "    Add these SOLIDWORKS Design files to Pack and Go: "
    If (Not (IsEmpty(pgFileNames))) Then
    For i = 0 To UBound(pgFileNames)
        Debug.Print "      The file to pack up is: " & pgFileNames(i)
    Next i
    End If
```

```
    ' Set document paths and names for Pack and Go
    status = swPackAndGo.SetDocumentSaveToNames(pgFileNames)
```

```
    ' Override path where to save documents
    myPath = "c:\temp\"
    status = swPackAndGo.SetSaveToName(True, myPath)
```

```
    ' Pack and Go both SOLIDWORKS Design and non-SOLIDWORKS-Design files
    statuses = swModelDocExt.SavePackAndGo(swPackAndGo)
```

```
End Sub
```
