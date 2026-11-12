---
title: "Get Names of Creators of Features Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Names_of_Creators_of_Features_Example_VB.htm"
---

# Get Names of Creators of Features Example (VBA)

This example shows how to get the names of the creators of the features in multiple part documents.

```
'---------------------------------------------------------------------------------
' Preconditions: Create the input file c:\temp\SOLIDWORKSFilenames.txt
' in a text editor and add the paths and file names of the
' part documents for which you want the creators of the
' features identified.
'
' Postconditions:
' 1. Opens c:\temp\SOLIDWORKSFilenames.txt.
' 2. Creates and opens c:\temp\SOLIDWORKSFilenamesFeatureCreators.txt.
' 2. Reads the name of the first part document.
' 3. Writes the name of the part document to
'    c:\temp\SOLIDWORKSFilenamesFeatureCreators.txt.
' 4. Opens the part document and iterates over its FeatureManager design tree
'    and writes the name of each feature and its creator to
'    c:\temp\SOLIDWORKSFilenamesFeatureCreators.txt.
' 5. Closes the part document.
' 6. Repeats steps 2 - 5 for each subsequent part document in
'    c:\temp\SOLIDWORKSFilenamesFeatureCreators.txt.
' 7. Closes c:\temp\SOLIDWORKSFilenamesFeatureCreators.txt and
'    c:\temp\SOLIDWORKSFilenamesFeatureCreators.txt.
' 8. Open c:\temp\SOLIDWORKSFilenamesFeatureCreators.txt in a text editor
'    and examine the contents of the file.
'---------------------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim Filename As String
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swFeat As SldWorks.Feature
    Dim fileerror As Long
    Dim filewarning As Long
```

```
    ' Disable Visual Basic error on implicit Query Interface
    On Error Resume Next
```

```
    Set swApp = Application.SldWorks
```

```
    ' Open the input file with the list of part documents to
    ' open and get feature and name of its creator
    Open "C:\temp\SOLIDWORKSFilenames.txt" For Input As #1
```

```
    ' Create and open the output file where to write the
    ' name of the part document and its features and their creators
    Open "C:\temp\SOLIDWORKSFilenamesFeatureCreators.txt" For Output As #2
       ' While not at the end of the input file, read the name of
       ' the part document to open
       Do While Not EOF(1)
            Line Input #1, Filename
            'Write the name of the part document to open to the output file
            Write #2, "============================================================================="
            Write #2, Filename
```

```
            ' Open document
            swApp.OpenDoc6 Filename, swDocPART, swOpenDocOptions_Silent, "", fileerror, filewarning
            Set swModel = swApp.ActiveDoc
```

```
            ' Get first feature in this part document
            Set swFeat = swModel.FirstFeature
            ' Iterate over features in this part document in FeatureManager design tree
            Do While Not swFeat Is Nothing
                ' Write the name of the feature and its creator to the output file
                Write #2, "  Feature " & swFeat.Name & " created by " & swFeat.CreatedBy
                ' Get next feature in this part document
                Set swFeat = swFeat.GetNextFeature
            Loop
            ' Close part document
            swApp.CloseDoc Filename
       Loop
```

```
    ' Close the input file
    Close #1
```

```
    'Close the output file
    Write #2, "============================================================================="
    Close #2
```

```
End Sub
```
