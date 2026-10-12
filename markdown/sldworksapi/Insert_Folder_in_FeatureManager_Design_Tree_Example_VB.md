---
title: "Insert Folder in FeatureManager Design Tree Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Folder_in_FeatureManager_Design_Tree_Example_VB.htm"
---

# Insert Folder in FeatureManager Design Tree Example (VBA)

This examples shows how to insert a new folder in the FeatureManager design tree above the selected folder. T

```
'--------------------------------------------
' Precondition:
' 1. Open a model document.
' 2. Select the folder above which you want to
'    insert a new folder.
'
' Postconditions:
' 1. Inserts a new folder in the FeatureManager
'    design tree above the selected folder. The
'    selected folder is now a sub-folder to the
'    new folder, Folder1_NEW.
' 2. Expand Folder1_NEW to verify step 1.
'---------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swFeatMgr As SldWorks.FeatureManager
    Dim swFeat As SldWorks.Feature
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swFeatMgr = swModel.FeatureManager
    Set swFeat = swFeatMgr.InsertFeatureTreeFolder2(swFeatureTreeFolder_Containing)
```

```
    ' Return Nothing if unable to create the folder
    If Not swFeat Is Nothing Then
        swFeat.Name = swFeat.Name & "_NEW"
    End If
```

```
End Sub
```
