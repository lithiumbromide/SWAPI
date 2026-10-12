---
title: "List Assemblies Where Part Used Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "pdmworksapi/List_Assemblies_Where_Part_Used_Example_VB.htm"
---

# List Assemblies Where Part Used Example (VBA)

This example shows how to look at each part in the SOLIDWORKS Workgroup PDM vault and list the assemblies in which the part is used.

```vb
Sub main()
    Dim connection As PDMWConnection
    Set connection = CreateObject("PDMWorks.PDMWConnection")
    connection.Login "pdmwadmin", "pdmwadmin", "localhost"
    Dim alldocs As PDMWDocuments
    Set alldocs = connection.Documents
    Dim adoc As PDMWDocument
    Dim msgBoxStr As String
    For Each adoc In alldocs
        If LCase(Right(adoc.Name, 6)) = "sldprt" Then
            msgBoxStr = msgBoxStr & "Part: " & adoc.Name & vbNewLine
            msgBoxStr = msgBoxStr & "Assemblies where it is used:" & vbNewLine
            Dim whereUsedList As PDMWLinks
            Set whereUsedList = adoc.WhereUsed
            Dim l As PDMWLink
            For Each l In whereUsedList
                If LCase(Right(l.Document.Name, 6)) = "sldasm" Then
                    msgBoxStr = msgBoxStr & "    " & l.Document.Name & vbNewLine
               ' Stop
                End If
            Next
            msgBoxStr = msgBoxStr & "----" & vbNewLine
        End If
    Next
    Output.Data = msgBoxStr
    Output.Show
    connection.Logout
End Sub
```
