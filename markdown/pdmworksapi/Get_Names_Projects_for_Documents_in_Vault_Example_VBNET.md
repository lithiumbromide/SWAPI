---
title: "Get Names of Projects for All Documents in Vault (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "pdmworksapi/Get_Names_Projects_for_Documents_in_Vault_Example_VBNET.htm"
---

# Get Names of Projects for All Documents in Vault (VB.NET)

This example shows how to get the names of the projects for all of the documents in the vault. The total number of documents and the names of their projects are written to the console window.

Imports PDMWorks

Module Module1

Sub Main()

Dim PDMW_conn As PDMWorks.PDMWConnection

PDMW_conn = CreateObject("PDMWorks.PDMWConnection")

PDMW_conn.**Login**("pdmwadmin", "pdmwadmin", "localhost")

Dim allDocs As PDMWDocuments

allDocs = PDMW_conn.**Documents**

Console.WriteLine("Total Documents: " + allDocs.**Count**.ToString)

' Given a PDMWDocuments collection called doc

For Each doc As PDMWDocument In allDocs

Dim Project As String

Project = doc.**project**

Console.WriteLine("Document Project: " + Project)

Next

PDMW_conn.**Logout**()

End Sub

End Module
