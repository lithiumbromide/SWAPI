---
title: "Create and Delete Selection Sets Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Delete_Selection_Sets_Example_VBNET.htm"
---

# Create and Delete Selection Sets Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExtension As ModelDocExtension
        Dim swSelectionSet1 As SelectionSet
        Dim swSelectionSet2 As SelectionSet
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\wrench.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        Debug.Print("File = " & swModel.GetPathName)
        swModelDocExtension = swModel.Extension

        'Create a selection set
        status = swModelDocExtension.SelectByID2("arm1-1@wrench", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        status = swModelDocExtension.SelectByID2("arm2-1@wrench", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExtension.SelectByID2("clamp2-1@wrench", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
        swSelectionSet1 = swModelDocExtension.SaveSelection(errors)
        Debug.Print("  First selection set created (1 = succeeded; 0 = failed)? " & errors)
        swModel.ClearSelection2(True)

        'Create another selection set
        status = swModelDocExtension.SelectByID2("centerlink-1@wrench", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        status = swModelDocExtension.SelectByID2("screw-1@wrench", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExtension.SelectByID2("screw-1@wrench", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionSet2 = swModelDocExtension.SaveSelection(errors)
        Debug.Print("  Second selection set created (1 = succeeded; 0 = failed)? " & errors)
        swModel.ClearSelection2(True)

        'Traverse the model to get Selection Sets folder
        TraverseModelFeatures(swModel)

    End Sub

    Sub TraverseFeatureFeatures(ByVal swFeat As Feature)

        Dim swSelectionSetFolder As SelectionSetFolder
        Dim selectionSetArray As Object
        Dim selectionSetItemArray As Object
        Dim selectionSetItemArrayTypes As Object
        Dim swSelectionSet As SelectionSet
        Dim swSelectionSetItem As SelectionSetItem
        Dim i As Integer
        Dim j As Integer

        While Not swFeat Is Nothing
            If swFeat.Name = "Selection Sets" Then
                Debug.Print("    " & swFeat.Name & " [" & swFeat.GetTypeName & "]")
                'Get Selection Sets folder
                swSelectionSetFolder = swFeat.GetSpecificFeature2
                'Get selection sets in Selection Sets folder
                selectionSetArray = swSelectionSetFolder.GetSelectionSets
                For i = 0 To UBound(selectionSetArray)
                    swSelectionSet = selectionSetArray(i)
                    Debug.Print("      Selection set[" & i & "] name: " & swSelectionSet.GetName)
                    'Get the items in this selection set
                    selectionSetItemArray = swSelectionSet.GetSelectionSetItems
                    selectionSetItemArrayTypes = swSelectionSet.GetSelectionSetItemTypes
                    For j = 0 To UBound(selectionSetItemArray)
                        swSelectionSetItem = selectionSetItemArray(j)
                        Debug.Print("        Item[" & j & "] in this selection set is this entity type as defined in swSelectType_e: " & selectionSetItemArrayTypes(j))
                        'Delete each item in this selection set
                        swSelectionSetItem.RemoveFromSelectionSet()
                        Debug.Print("          Selection set item[" & j & "] deleted")
                    Next
                Next
            End If
            swFeat = swFeat.GetNextFeature
        End While

    End Sub

    Sub TraverseModelFeatures(ByVal swModel As ModelDoc2)

        Dim swFeat As Feature

        swFeat = swModel.FirstFeature
        TraverseFeatureFeatures(swFeat)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
