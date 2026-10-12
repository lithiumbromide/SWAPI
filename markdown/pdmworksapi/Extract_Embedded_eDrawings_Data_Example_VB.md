---
title: "Extract Embedded eDrawings Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "pdmworksapi/Extract_Embedded_eDrawings_Data_Example_VB.htm"
---

# Extract Embedded eDrawings Data Example (VBA)

This example shows how to search drawings in the SOLIDWORKS Workgroup PDM vault, check to see if the drawings of a certain lifecycle status (APPROVED), and if both criteria are met, extract the embedded eDrawings data from the drawings and save it to a local disk.

```vb
Sub main()
    On Error GoTo errorHandler
    Dim connection As PDMWConnection
    Set connection = CreateObject("PDMWorks.PDMWConnection")
    connection.Login "pdmwadmin", "pdmwadmin", "localhost"
    Dim savePath As String
    savePath = "C:\edrawings\"  ''Must be a valid path
    Dim alldocs As PDMWDocuments
    Set alldocs = connection.Documents
    Dim adoc As PDMWDocument
    For Each adoc In alldocs
        If LCase(Right(adoc.Name, 6)) = "slddrw" Then
            If adoc.GetStatus = "APPROVED" Then
                adoc.SaveEmbeddedEDW savePath
            End If
        End If
    Next
    connection.Logout
Exit Sub
errorHandler:
    Debug.Print "Error: " & adoc.Name & " : " & Err.Description
    Resume Next
End Sub
```
