---
title: "Get SOLIDWORKS Search Third-party Keywords Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_SOLIDWORKS_Search_Third-party_Keywords_Example_VB.htm"
---

# Get SOLIDWORKS Search Third-party Keywords Example (VBA)

This example shows how to get the SOLIDWORKS Search third-party keywords for a model document.

```
'-----------------------------------------------------
' Preconditions:
' 1. Open a model document that was previously assigned
'    SOLIDWORKS Search third-party keywords
'    and which have been indexed in SOLIDWORKS Design
'    - or -
'    run Add Third-party Application Keywords to SOLIDWORKS Search and Model Example (VBA).
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the number of Search third-party keywords
'    assigned to the open model document and the keywords
'    and values.
' 2. Examine the Immediate window.
'-----------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim vAppName As Variant, vKeywordNames As Variant, vKeywordValues As Variant
Dim i As Long, lNbrKeywords As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    lNbrKeywords = swModelDocExt.GetSearchData("COSMOSWorks", vAppName, vKeywordNames, vKeywordValues)
    Debug.Print "Number of keywords: " & lNbrKeywords
    For i = 0 To lNbrKeywords - 1
        Debug.Print "Keyword: " & vKeywordNames(i)
        Debug.Print "  Value: " & vKeywordValues(i)
    Next i
```

```
End Sub
```
