---
title: "Pack and Go Part and Linked Equation Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Pack_and_Go_Part_and_Linked_Equation_Example_vbnet.htm"
---

# Pack and Go Part and Linked Equation Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swEqnMgr As EquationMgr
        Dim swPackAndGo As PackAndGo
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer
        Dim i As Integer
        Dim nCount As Integer
        Dim eqnLinked As Boolean
        Dim pgFileNames As Object = Nothing
        Dim status As Boolean
        Dim statuses As Object
        Dim myPath As String

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\microphonehousing.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        Debug.Print("File = " & swModel.GetPathName)
        Debug.Print(" ")

        ' Get Equation manager object
        swEqnMgr = swModel.GetEquationMgr

        ' List the equations, get whether they're linked
        ' to files, make sure any equations are up to date,
        ' and get the paths where they're stored
        nCount = swEqnMgr.GetCount
        For i = 0 To nCount - 1
            Debug.Print("  Equation #" & i & " = " & swEqnMgr.Equation(i))

            eqnLinked = swEqnMgr.LinkToFile
            Debug.Print("  Equation linked to file? " & eqnLinked)

            If eqnLinked Then

                'Make sure equations are up to date
                swEqnMgr.UpdateValuesFromExternalEquationFile()

                'Get path and name of linked equation file
                Debug.Print("  Path and file name of linked equation: " & swEqnMgr.FilePath)

            End If
        Next i

        Debug.Print(" ")

        ' Get Pack and Go object
        Debug.Print("  Pack and Go")
        swPackAndGo = swModelDocExt.GetPackAndGo

        ' Get current paths and names of the documents
        status = swPackAndGo.GetDocumentNames(pgFileNames)
        Debug.Print("    Add these SOLIDWORKS Design files to Pack and Go: ")
        If Not pgFileNames Is Nothing Then
            For i = 0 To UBound(pgFileNames)
                Debug.Print("      The file to pack up is: " & pgFileNames(i))
            Next i
        End If

        ' Set document paths and names for Pack and Go
        status = swPackAndGo.SetDocumentSaveToNames(pgFileNames)

        ' Override path where to save documents
        myPath = "c:\temp\"
        status = swPackAndGo.SetSaveToName(True, myPath)

        ' Pack and Go both SOLIDWORKS Design and non-SOLIDWORKS-Design files
        statuses = swModelDocExt.SavePackAndGo(swPackAndGo)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
