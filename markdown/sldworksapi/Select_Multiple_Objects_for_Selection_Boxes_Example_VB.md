---
title: "Select Multiple Objects for Selection Boxes Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Multiple_Objects_for_Selection_Boxes_Example_VB.htm"
---

# Select Multiple Objects for Selection Boxes Example (VBA)

This example shows how to select multiple objects and add the selected objects to different selection boxes on a PropertyManager page.

```vb
'--------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Copy Modules - main to your project.
 ' 2. Insert a class module and copy Class Modules - clsPropMgr to that module.
 ' 3. Rename the class module to clsPropMgr.
 ' 3. Add swpublished.tlb to your project (click   Tools > References >
 '    SOLIDWORKS version exposed type libraries for add-in use).
 ' 4. Verify that the specified assembly exists.
 '
 ' Postconditions:
 ' 1. Opens the assembly.
 ' 2. Creates a PropertyManager page.
 ' 3. Examine the PropertyManager page and verify that three selected faces
 '    appear in the top selection box and two selected faces appear in the
 '    bottom selection box.
 ' 4. Close the PropertyManager page.
 '
 ' NOTE: Because the assembly document is used elsewhere,
 ' do not save changes.
 '----------------------------------------------------------------------------
 'Modules - main
```

```
Option Explicit
```

```
Public swApp As SldWorks.SldWorks
Public swModel As SldWorks.ModelDoc2
Public swModelDocExt As SldWorks.ModelDocExtension
Public swSelectionMgr As SldWorks.SelectionMgr
Public pm As clsPropMgr
Public mark As Long
Public mark2 As Long
```

```
Sub main()
```

```
    Dim openDocErrors As Long
    Dim OpenDocWarnings As Long
    Dim nbrSelections As Long
    Dim selections1(2) As SldWorks.Face2
    Dim selections2(1) As SldWorks.Face2
    Dim i As Long
    Dim j As Long
    Dim status As Boolean
    Dim fileName As String
```

```
    'Set the marks for the selections and selection boxes
    mark = 1
    mark2 = 2
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\bladed shaft.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocASSEMBLY, swOpenDocOptions_Silent, "", openDocErrors, OpenDocWarnings)
    Set swModelDocExt = swModel.Extension
    Set swSelectionMgr = swModel.SelectionManager
```

```
    'Create a new instance of the PropertyManager class
    Set pm = New clsPropMgr
    pm.Show
```

```
    'Selections for top selection box
    status = swModelDocExt.SelectByID2("", "FACE", 3.69805475952489E-03, 9.01975482463513E-02, 3.15907187808762E-03, True, mark, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", 8.60570843923369E-03, 7.37431971170679E-02, 3.9892160950501E-03, True, mark, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", 1.00013029872912E-02, 4.46884591512742E-02, 9.96173127262523E-03, True, mark, Nothing, 0)
    nbrSelections = swSelectionMgr.GetSelectedObjectCount2(-1)
    nbrSelections = nbrSelections - 1
    For i = 0 To nbrSelections
      Set selections1(i) = swSelectionMgr.GetSelectedObject6(i + 1, -1)
    Next
```

```
    swModel.ClearSelection2 True

    'Selections for bottom selection box
    status = swModelDocExt.SelectByID2("", "FACE", -2.64206017159268E-02, -3.42602957275062E-03, 9.87615560137556E-03, True, mark2, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", -1.28130257782288E-03, -3.54158999988385E-03, 1.77003152412567E-02, True, mark2, Nothing, 0)
    nbrSelections = swSelectionMgr.GetSelectedObjectCount2(-1)
    nbrSelections = nbrSelections - 1
    For j = 0 To nbrSelections
      Set selections2(j) = swSelectionMgr.GetSelectedObject6(j + 1, -1)
    Next
```

```
    swModel.ClearSelection2 True
```

```
    'Populate selection boxes
    SelectBoxFaces1 selections1, mark
```

```
    SelectBoxFaces2 selections2, mark2
```

```
End Sub
```

```
Private Sub SelectBoxFaces1(selections() As SldWorks.Face2, selectionBoxMark)
```

```
    Dim swSelectData As SldWorks.SelectData
    Set swSelectData = swSelectionMgr.CreateSelectData
    swSelectData.mark = selectionBoxMark
    swModelDocExt.MultiSelect2 selections, True, swSelectData
```

```
End Sub
```

```
Private Sub SelectBoxFaces2(selections() As SldWorks.Face2, selectionBoxMark)
```

```
    Dim swSelectData As SldWorks.SelectData
    Set swSelectData = swSelectionMgr.CreateSelectData
    swSelectData.mark = selectionBoxMark
    swModelDocExt.MultiSelect2 selections, True, swSelectData
```

```
End Sub
```

[Back to top](#Top)

```vb
 'Class Modules - clsPropMgr
```

```
Option Explicit
```

```
'Required for PropertyManager page controls
Implements PropertyManagerPage2Handler9
```

```
'General objects required for the PropertyManager page
Dim pm_Page As PropertyManagerPage2
Dim pm_Group As PropertyManagerPageGroup
Dim pm_Selection As PropertyManagerPageSelectionbox
Dim pm_Selection2 As PropertyManagerPageSelectionbox
```

```
'Each object in the PropertyManager page needs a unique ID
Const GroupID As Long = 1
Const LabelID As Long = 2
Const SelectionID As Long = 3
Const ComboID As Long = 4
Const ListID As Long = 5
Const Selection2ID As Long = 6
```

```
Dim ClickedCancel As Boolean
Dim retVal As Long
```

```
Sub Show()
  pm_Page.Show2 0
End Sub
```

```
'The following runs when a new instance
'of the class is created
Private Sub Class_Initialize()
```

```
Dim PageTitle As String
Dim caption As String
Dim tip As String
Dim options As Long
Dim longerrors As Long
Dim controlType As Long
Dim alignment As Long
```

```
'Set the variables for the PropertyManager page
PageTitle = "MultiSelect2 Test"
options = swPropertyManager_OkayButton + swPropertyManager_CancelButton + swPropertyManagerOptions_PushpinButton
```

```
'Create the PropertyManager page
Set pm_Page = swApp.CreatePropertyManagerPage(PageTitle, options, Me, longerrors)
```

```
'Make sure that the PropertyManager page was created properly
If longerrors = swPropertyManagerPage_Okay Then
```

```
    'Begin adding the controls to the PropertyManager page
```

```
    'Create the group box
     caption = ""
     options = swGroupBoxOptions_Visible + swGroupBoxOptions_Expanded
```

```
     Set pm_Group = pm_Page.AddGroupBox(GroupID, caption, options)
```

```
    'Create selection boxes
     controlType = swControlType_Selectionbox
     caption = ""  ' No caption for selection box
     alignment = swControlAlign_Indent
     options = swControlOptions_Visible + swControlOptions_Enabled
     tip = "Select multiple faces."
```

```
     Set pm_Selection = pm_Group.AddControl(SelectionID, controlType, caption, alignment, options, tip)
     Set pm_Selection2 = pm_Group.AddControl(Selection2ID, controlType, caption, alignment, options, tip)
```

```
     'Only faces can populate the selection boxes
     Dim filters(0) As Long
     filters(0) = swSelFACES
```

```
     pm_Selection.SingleEntityOnly = False
     pm_Selection.AllowMultipleSelectOfSameEntity = True
     pm_Selection.Height = 50
     pm_Selection.SetSelectionFilters filters
     pm_Selection.mark = mark
```

```
     pm_Selection2.SingleEntityOnly = False
     pm_Selection2.AllowMultipleSelectOfSameEntity = True
     pm_Selection2.Height = 50
     pm_Selection2.SetSelectionFilters filters
     pm_Selection2.mark = mark2
```

```
Else  'If the page is not created
    MsgBox "An error occurred while attempting to create the " & "PropertyManager Page", vbCritical
```

```
End If
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_AfterActivation()
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_AfterClose()
    'Destroy the class
    Set pm = Nothing
End Sub
```

```
Private Function PropertyManagerPage2Handler9_OnActiveXControlCreated(ByVal Id As Long, ByVal status As Boolean) As Long
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler9_OnButtonPress(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnCheckboxCheck(ByVal Id As Long, ByVal Checked As Boolean)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnClose(ByVal Reason As Long)
```

```
If Reason = swPropertyManagerPageClose_Cancel Then
    'Cancel button was clicked
    ClickedCancel = True
ElseIf Reason = swPropertyManagerPageClose_Okay Then
    'OK button was clicked
    ClickedCancel = False
End If
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnComboboxEditChanged(ByVal Id As Long, ByVal Text As String)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnComboboxSelectionChanged(ByVal Id As Long, ByVal Item As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnGroupCheck(ByVal Id As Long, ByVal Checked As Boolean)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnGroupExpand(ByVal Id As Long, ByVal Expanded As Boolean)
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler9_OnHelp() As Boolean
```

```
End Function
```

```
Private Function PropertyManagerPage2Handler9_OnKeystroke(ByVal Wparam As Long, ByVal Message As Long, ByVal Lparam As Long, ByVal Id As Long) As Boolean
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler9_OnListboxSelectionChanged(ByVal Id As Long, ByVal Item As Long)
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler9_OnNextPage() As Boolean
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler9_OnNumberboxChanged(ByVal Id As Long, ByVal Value As Double)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnOptionCheck(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnPopupMenuItem(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnPopupMenuItemUpdate(ByVal Id As Long, retVal As Long)
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler9_OnPreview() As Boolean
```

```
End Function
```

```
Private Function PropertyManagerPage2Handler9_OnPreviousPage() As Boolean
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler9_OnRedo()
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnSelectionboxCalloutCreated(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnSelectionboxCalloutDestroyed(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnSelectionboxFocusChanged(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnSelectionboxListChanged(ByVal Id As Long, ByVal Count As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnSliderPositionChanged(ByVal Id As Long, ByVal Value As Double)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnSliderTrackingCompleted(ByVal Id As Long, ByVal Value As Double)
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler9_OnSubmitSelection(ByVal Id As Long, ByVal Selection As Object, ByVal SelType As Long, ItemText As String) As Boolean
```

```
    PropertyManagerPage2Handler9_OnSubmitSelection = True
    Debug.Print ("OnSubmitSelection event fired.")
```

```
End Function
```

```
Private Function PropertyManagerPage2Handler9_OnTabClicked(ByVal Id As Long) As Boolean
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler9_OnTextboxChanged(ByVal Id As Long, ByVal Text As String)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnUndo()
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnWhatsNew()
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnLostFocus(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler9_OnGainedFocus(ByVal Id As Long)
```

```
End Sub
```

```
Public Sub PropertyManagerPage2Handler9_OnListBoxRMBUp(ByVal Id As Long, ByVal posX As Long, ByVal posY As Long)
```

```
End Sub
```

```
Public Function PropertyManagerPage2Handler9_OnWindowFromHandleControlCreated(ByVal Id As Long, ByVal status As Boolean) As Long
```

```
End Function
```

```
Public Sub PropertyManagerPage2Handler9_OnNumberboxTrackingCompleted(ByVal Id As Long, ByVal Value As Double)
```

```
End Sub
```

[Back to top](#Top)
