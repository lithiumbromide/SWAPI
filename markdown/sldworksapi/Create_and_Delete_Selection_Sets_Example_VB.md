---
title: "Create and Delete Selection Sets Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Delete_Selection_Sets_Example_VB.htm"
---

# Create and Delete Selection Sets Example (VBA)

This example shows how to:

- create selection sets.
- get the Selection Sets folder.
- get the selection sets in the Selection Sets folder.
- get and then delete the items in the selection sets, which deletes the selection sets.

```
'--------------------------------------------------------------------
' Preconditions:
' 1. Verify that the assembly to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the assembly.
' 2. Creates two selection sets.
' 3. Traverses the FeatureManager design tree. If the feature is the
'    Selection Sets folder, then:
'    a. Gets its name.
'    b. Gets each selection set in the Selection Sets folder.
'    c. Gets and then deletes each selection set item in the
'       selection set, which deletes the selection set.
' 4. Examine the Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'--------------------------------------------------------------------
Option Explicit
```

```
Sub TraverseFeatureFeatures(swFeat As SldWorks.Feature)
```

```
    Dim swSelectionSetFolder As SldWorks.SelectionSetFolder
    Dim selectionSetArray As Variant
    Dim selectionSetItemArray As Variant
    Dim selectionSetItemArrayTypes As Variant
    Dim swSelectionSet As SldWorks.SelectionSet
    Dim swSelectionSetItem As SldWorks.SelectionSetItem
    Dim i As Long
    Dim j As Long
```

```
    While Not swFeat Is Nothing
        If swFeat.Name = "Selection Sets" Then
            Debug.Print "    " & swFeat.Name & " [" & swFeat.GetTypeName & "]"
            'Get Selection Sets folder
            Set swSelectionSetFolder = swFeat.GetSpecificFeature2
            'Get selection sets in Selection Sets folder
            selectionSetArray = swSelectionSetFolder.GetSelectionSets
            For i = 0 To UBound(selectionSetArray)
                Set swSelectionSet = selectionSetArray(i)
                Debug.Print "      Selection set[" & i & "] name: " & swSelectionSet.GetName
                'Get the items in this selection set
                selectionSetItemArray = swSelectionSet.GetSelectionSetItems
 		selectionSetItemArrayTypes = swSelectionSet.GetSelectionSetItemTypes
                For j = 0 To UBound(selectionSetItemArray)
                    Set swSelectionSetItem = selectionSetItemArray(j)
                    Debug.Print "        Item[" & j & "] in this selection set is this entity type as defined in swSelectType_e: " & selectionSetItemArrayTypes(j)
                    'Delete each item in this selection set
                    swSelectionSetItem.RemoveFromSelectionSet
                    Debug.Print ("          Selection set item[" & j & "] deleted")
                Next
            Next
        End If
        Set swFeat = swFeat.GetNextFeature
    Wend
```

```
End Sub
```

```
Sub TraverseModelFeatures(swModel As SldWorks.ModelDoc2)

    Dim swFeat As SldWorks.Feature

    Set swFeat = swModel.FirstFeature
    TraverseFeatureFeatures swFeat
```

```
End Sub

Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExtension As SldWorks.ModelDocExtension
    Dim swSelectionSet1 As SldWorks.SelectionSet
    Dim swSelectionSet2 As SldWorks.SelectionSet
    Dim status As Boolean
    Dim errors As Long
    Dim warnings As Long
    Dim fileName As String
```

```
    Set swApp = CreateObject("SldWorks.Application")
```

```
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\wrench.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Debug.Print "File = " & swModel.GetPathName
    Set swModelDocExtension = swModel.Extension
```

```
    'Create a selection set
    status = swModelDocExtension.SelectByID2("arm1-1@wrench", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    status = swModelDocExtension.SelectByID2("arm2-1@wrench", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExtension.SelectByID2("clamp2-1@wrench", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
    Set swSelectionSet1 = swModelDocExtension.SaveSelection(errors)
    Debug.Print "  First selection set created (1 = succeeded; 0 = failed)? " & errors
    swModel.ClearSelection2 True
```

```
    'Create another selection set
    status = swModelDocExtension.SelectByID2("centerlink-1@wrench", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    status = swModelDocExtension.SelectByID2("screw-1@wrench", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExtension.SelectByID2("screw-1@wrench", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionSet2 = swModelDocExtension.SaveSelection(errors)
    Debug.Print "  Second selection set created (1 = succeeded; 0 = failed)? " & errors
    swModel.ClearSelection2 True
```

```
    'Traverse the model to get Selection Sets folder
    TraverseModelFeatures swModel
```

```
End Sub
```
