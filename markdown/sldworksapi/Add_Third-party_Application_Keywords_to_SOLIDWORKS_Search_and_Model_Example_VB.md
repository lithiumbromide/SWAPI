---
title: "Add Third-party Application Keywords to SOLIDWORKS Search and Model Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Third-party_Application_Keywords_to_SOLIDWORKS_Search_and_Model_Example_VB.htm"
---

# Add Third-party Application Keywords to SOLIDWORKS Search and Model Example (VBA)

This example shows how to add third-party application keywords to SOLIDWORKS Search and to a model document.

```
'-------------------------------------------------------------
' Preconditions: Create a new drawing.
'
' Postconditions:
' 1. Adds the specified keyword and value to SOLIDWORKS Search
'    for the specified application and drawing.
' 2. Click Tools > Options > Search  > Always index (may slow
'    SOLIDWORKS Design), if this check box is not selected.
' 3. Close the drawing and close SOLIDWORKS Design.
' 4. Restart SOLIDWORKS Design and open the drawing closed in step 3.
' 5. Run Get SOLIDWORKS Search Third-party Keywords Example (VBA).
' 6. Deselect the Always index (may slow SOLIDWORKS Design) check box
'    if the check box was previously not selected.
'--------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim longstatus As Long, longwarnings As Long
Dim boolstatus As Boolean
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
    ' Assign keywords and values
    boolstatus = swModelDocExt.AddOrUpdateSearchData("COSMOSWorks", "FirstName", "John")
    boolstatus = swModelDocExt.AddOrUpdateSearchData("COSMOSWorks", "MiddleName", "D")
    boolstatus = swModelDocExt.AddOrUpdateSearchData("COSMOSWorks", "LastName", "Doe")
    boolstatus = swModel.Save3(swSaveAsOptions_Silent, longstatus, longwarnings)
```

```
End Sub
```
