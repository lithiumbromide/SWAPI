---
title: "Create Search Criteria and Search Vault Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "pdmworksapi/Create_Search_Criteria_and_Search_Vault_Example_VB.htm"
---

# Create Search Criteria and Search Vault Example (VBA)

This example shows how to create a search criteria and search the SOLIDWORKS Workgroup PDM vault using that criteria.

```vb
Private Sub Command1_Click()
Dim Options As PDMWorks.PDMWSearchOptions
Dim Criteria As PDMWorks.PDMWSearchCriteria
Dim Results As PDMWorks.PDMWSearchResults
Dim Result As PDMWorks.PDMWSearchResult
Dim i As Integer
Dim cnt As Integer
    On Error Resume Next

    Set Options = Connection.GetSearchOptionsObject
    If Not Options Is Nothing Then
        Options.IgnoreCase = True
        Options.IgnoreLinks = False
        Options.IncludeHiddenDocuments = True
        Options.SearchConfigSpecificProperties = False
        Options.SearchOnlyChildrenOf = ""
        Options.SearchCriteria.AddCriteria pdmwOr, pdmwDocumentName, , Contains, "sldprt"
        Options.SearchCriteria.AddCriteria pdmwAnd, PDMWConfiguration, "", Contains, "default"

        Options.SearchCriteria.SaveToFile "c:\temp\cri_test.sqy"
        Options.SearchCriteria.LoadFromFile "c:\temp\cri_test.sqy"

        Set Results = Connection.Search(Options)
        If Not Results Is Nothing Then
            cnt = Results.Count

            For i = 0 To cnt - 1
                Set Result = Results(i)
                AddItemToGrid Result
            Next i
        End If
    End If

End Sub
```
