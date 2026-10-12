---
title: "Get Size of Document Larger Than 2GB Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "pdmworksapi/Get_Size_of_Document_Larger_Than_2GB_Example_VB.htm"
---

# Get Size of Document Larger Than 2GB Example (VBA)

You can get the size of a document larger than 2GB by calling either:

- IPDMWDocument::GetDocumentSize
  - or -
- IPDMWDocument::SizeH and IPDMWDocument::Size and combining their return values.

This example shows how to get the size of a document larger than 2GB, using both ways.

```
' ---------------------------------------------------------------------------
' Preconditions:
' 1. Replace <your_2GB+_document> with the name of a document that is larger
'    than 2GB and that is checked into your vault.
' 2. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'-------------------------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim connection As PDMWConnection
    Dim doc As PDMWDocument
    Dim fileName As String
```

```
    Dim lSizeHi As Long
    Dim lSizeLow As Long
    Dim docSize As Double
```

```
    ' Log into vault
    Set connection = CreateObject("PDMWorks.PDMWConnection")
    connection.Login "pdmwadmin", "pdmwadmin", "localhost"
```

```
    fileName = "<your_2GB+_document>"
```

```
    ' Name of 2GB+ document in vault
    Set doc = connection.GetSpecificDocument(fileName)
```

```
    ' Using new IPDMWDocument::GetDocumentSize method
    docSize = CDbl(doc.GetDocumentSize)
    Debug.Print ("Result using IPDMWDocument::GetDocumentSize method:")
    Debug.Print ("   Size of " + fileName + " is " + Str(docSize) + " bytes")
    Debug.Print
```

```
    ' Using both IPDMWDocument::Size and IPDMWDocument::SizeH properties
    '
    ' NOTE: Because VB's long is signed, you must convert the long to
    ' a positive value for both return values
    lSizeHi = doc.SizeH
    docSize = IIf(lSizeHi < 0, 4294967296# + lSizeHi, lSizeHi)
    docSize = docSize * 4294967296#
```

```
    lSizeLow = doc.Size
    docSize = docSize + IIf(lSizeLow < 0, 4294967296# + lSizeLow, lSizeLow)
```

```
    Debug.Print ("Result using IPDMWDocument::Size and IPDMWDocument::SizeH properties:")
    Debug.Print ("   Size of " + fileName + " is " + Str(docSize) + " bytes")
    Debug.Print
```

```
    connection.Logout
```

```
End Sub
```
