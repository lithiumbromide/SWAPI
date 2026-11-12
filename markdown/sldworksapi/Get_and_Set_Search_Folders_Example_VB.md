---
title: "Get and Set Search Folders Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Search_Folders_Example_VB.htm"
---

# Get and Set Search Folders Example (VBA)

This example shows how to get and set the file locations in which SOLIDWORKS Design searches for reference documents.

```
'----------------------------------------------------------------------------
' Preconditions: Open the Immediate window.
'
' Postconditions:
' 1. Adds c:\; to the beginning of the search folder path for reference
'    documents.
' 2. Inspect the Immediate window.
'
' NOTE: This macro changes your SOLIDWORKS Design search folders system settings.
'---------------------------------------------------------------------------
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim searchFolders As String
Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set Part = swApp.ActiveDoc
```

```
    swApp.SetUserPreferenceToggle swUserPreferenceToggle_e.swUseFolderSearchRules, False
```

```
    searchFolders = swApp.GetSearchFolders(swSearchFolderTypes_e.swDocumentType)
    Debug.Print "Current search path: " & searchFolders
    searchFolders = "c:\;" & searchFolders
    boolstatus = swApp.SetSearchFolders(swSearchFolderTypes_e.swDocumentType, searchFolders)
    searchFolders = swApp.GetSearchFolders(swSearchFolderTypes_e.swDocumentType)
    Debug.Print "New search path: " & searchFolders
```

```
End Sub
```
