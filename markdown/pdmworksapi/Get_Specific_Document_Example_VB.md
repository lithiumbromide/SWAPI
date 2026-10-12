---
title: "Get Specific Document Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "pdmworksapi/Get_Specific_Document_Example_VB.htm"
---

# Get Specific Document Example (VBA)

This example shows how to log into a SOLIDWORKS Workgroup PDM vault, get a collection of documents, and get a specific document.

```vb
Sub main()
    Dim connection As PDMWConnection
    Set connection = CreateObject("PDMWorks.PDMWConnection")
    connection.Login "pdmwadmin", "pdmwadmin", "localhost"

    Dim alldocs As PDMWDocuments
    Dim doc1 As PDMWDocument
    Dim doc2 As PDMWDocument
    Dim doc3 As PDMWDocument
    Set alldocs = connection.Documents
    Set doc1 = connection.Documents.Item(0)
    Set doc2 = connection.GetSpecificDocument("bracket.sldprt")
    ''Look at alldocs, doc1, and doc2 in the debugger
    Set doc3 = alldocs("bracket.sldprt")

    connection.Logout
End Sub
```
