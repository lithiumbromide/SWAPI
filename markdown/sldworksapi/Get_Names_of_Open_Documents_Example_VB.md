---
title: "Get Names of Open Documents Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Names_of_Open_Documents_Example_VB.htm"
---

# Get Names of Open Documents Example (VBA)

This example shows how to get the names of the open documents, the names of the referenced model documents, and their visibility.

```
'-------------------------------------
' Preconditions:
' 1. Open multiple model documents.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the names of the open and referenced model documents.
' 2. Examine the Immediate window.
'-------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelTitle As SldWorks.ModelDoc2
    Dim swModelPath As SldWorks.ModelDoc2
    Dim cTitle As New Collection
    Dim vTitle As Variant
    Dim cPath As New Collection
    Dim vPath As Variant
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.GetFirstDocument
```

```
    While Not swModel Is Nothing
        ' Assembly components are opened, but are not visible
        ' until opened by the user
        Debug.Print swModel.GetPathName & "  [" & swModel.Visible & "]"
        Debug.Print "  " & swModel.GetTitle & " [" & swModel.GetType & "]"
```

```
        ' The document name contains a filename extension
        ' if the document has been saved
        ' and is subject to Microsoft File Explorer setting;
        ' the document name does not contain a
        ' filename extension if the document has not been saved;
        ' ModelDoc2::GetPathName is blank until the file is saved
        cTitle.Add swModel.GetTitle
        cPath.Add swModel.GetPathName
        Set swModel = swModel.GetNext
    Wend
```

```
    Debug.Print " "
```

```
    For Each vTitle In cTitle
        Set swModelTitle = swApp.GetOpenDocument(vTitle): Debug.Assert Not swModelTitle Is Nothing
        Debug.Print swModelTitle.GetPathName & "  [" & swModelTitle.Visible & "]"
        Debug.Print "  " & swModelTitle.GetTitle & " [" & swModelTitle.GetType & "]"
    Next vTitle
```

```
    Debug.Print " "
```

```
    For Each vPath In cPath
        Set swModelPath = swApp.GetOpenDocument(vPath)
        If Not swModelPath Is Nothing Then
        Debug.Print swModelPath.GetPathName & "  [" & swModelPath.Visible & "]"
            Debug.Print "  " & swModelPath.GetTitle & " [" & swModelPath.GetType & "]"
        End If
    Next vPath
```

```
End Sub
```
