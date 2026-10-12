---
title: "Delete Selected Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Selected_Feature_Example_VB.htm"
---

# Delete Selected Feature Example (VBA)

This example shows how to delete a selected feature. You can specify to delete the absorbed or children features or both types of features. This example does not ask you to confirm the deletion.

```
'--------------------------------------
' Preconditions:
' 1. Open a model document.
' 2. Select the feature to delete.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Deletes the selected feature.
' 2. Examine the Immediate window, graphics
'    area, and FeatureManager design tree.
'--------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim DeleteOption As Long
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension
```

```
    ' To delete absorbed features, use enum swDeleteSelectionOptions_e.swDelete_Absorbed
    ' To delete children features, use enum swDeleteSelectionOptions_e.swDelete_Children
    ' To keep absorbed features and children features, set DeleteOption = 0
    DeleteOption = swDeleteSelectionOptions_e.swDelete_Absorbed

    'Comment out the previous statement and uncomment one of the
    'following statements to change how to delete the selected feature
    'DeleteOption = swDeleteSelectionOptions_e.swDelete_Children
    'DeleteOption = 0
    'DeleteOption =swDeleteSelectionOptions_e.swDelete_Absorbed + swDeleteSelectionOptions_e.swDelete_Children
```

```
    status = swModelDocExt.DeleteSelection2(DeleteOption)
    Debug.Print "Feature deleted? " & status
```

```
End Sub
```
