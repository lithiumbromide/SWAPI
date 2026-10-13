---
title: "Get Paths of Open Documents(VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Paths_of_Open_Documents_Example_VBNET.htm"
---

# Get Paths of Open Documents(VB.NET)

## Get Paths of Open Documents (VB.NET)

This example shows how to get an array of the open documents, and their paths and filenames, in the current SOLIDWORKS Design session.

```vb
'---------------------------------------------
' Preconditions: At least one document is
'                open in SOLIDWORKS Design.
'
' Postconditions: None.
----------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim models As Object
    Dim count As Integer
    Dim index As Integer

    Public Sub main()

        count = swApp.GetDocumentCount
        Debug.Print("Number of open documents in this SOLIDWORKS Design session: " & count)
        models = swApp.GetDocuments
        For index = LBound(models) To UBound(models)
            swModel = models(index)
            Debug.Print("Path and name of open document: " & swModel.GetPathName)
        Next index

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
