---
title: "Show Bubble ToolTip for PropertyManager Page Control Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Show_Bubble_ToolTip_for_PropertyManager_Page_Control_Example_VB.htm"
---

# Show Bubble ToolTip for PropertyManager Page Control Example (VBA)

This example shows how to create a PropertyManager page. When the check box on the PropertyManager page is selected, a bubble ToolTip is displayed. This type of ToolTip is useful for validating data typed or selected by users in controls on a PropertyManager page.

```
'----------------------------------------
' Preconditions:
' 1. Copy Main into your project.
' 2. Insert a class module called PropMgrHdlr and
'    copy PropMgrHdlr to that module.
' 3. Click Tools > References > SOLIDWORKS <version> exposed
'    type libraries for add-in use).
' 4. Open a part document.
'
' Postconditions:
' 1. Creates and displays a PropertyManager page.
' 2. Select Sample check box to display a bubble ToolTip.
' 3. Click outside the bubble ToolTip to close it.
'    NOTE: Clearing Sample check box does not display
'    the bubble ToolTip.
'---------------------------------------
'Main
```

```
Option Explicit
```

```
Public swApp As SldWorks.SldWorks
Public swModel As SldWorks.ModelDoc2
Public swSelMgr As SldWorks.SelectionMgr
Public pm As PropMgrHdlr
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swSelMgr = swModel.SelectionManager
```

```
'Create a new instance of the PropertyManager class
'Calls the Class_Initialize procedure of the class
Set pm = New PropMgrHdlr
    pm.Show
```

```
End Sub
```

```
Back to top
```

```
'PropMgrHdlr
```

```
Option Explicit
```

```
'Required for PropertyManager page controls
Implements PropertyManagerPage2Handler6
```

```
'Objects for the PropertyManager page
Dim pm_Page As PropertyManagerPage2
Dim pm_Group As PropertyManagerPageGroup
Dim pm_Selection As PropertyManagerPageSelectionbox
Dim pm_Control As PropertyManagerPageControl
```

```
'Each object in the page needs a unique ID
Const GroupID As Integer = 1
Const SelectionID As Integer = 3
Const ControlID As Integer = 4
```

```
Dim ClickedCancel As Boolean
Dim bubbleToolTipTitle As String
Dim bubbleToolTipMessage As String
Dim bubbleToolTipBmpFile As String
Dim isChecked As Boolean
```

```
Sub Show()
    pm_Page.Show
End Sub
```

```
Private Sub Class_Initialize()
    Dim PageTitle As String
    Dim caption As String
    Dim tip As String
    Dim options As Long
    Dim longerrors As Long
    Dim controlType As Integer
    Dim alignment As Integer
```

```
    'Set the variables for the page
    PageTitle = "Sample PropertyManager page"
    options = swPropertyManager_OkayButton + swPropertyManager_CancelButton + swPropertyManagerOptions_LockedPage + swPropertyManagerOptions_PushpinButton
```

```
    'Create the PropertyManager page
    Set pm_Page = swApp.CreatePropertyManagerPage(PageTitle, options, Me, longerrors)
```

```
    'Make sure that the page was created properly
    If longerrors = swPropertyManagerPage_Okay Then
        'Begin adding the controls to the page
        'Create the group box
        caption = "Sample Group Box"
        options = swGroupBoxOptions_Visible + swGroupBoxOptions_Expanded
        Set pm_Group = pm_Page.AddGroupBox(GroupID, caption, options)
```

```
          'Create selection box
          controlType = swControlType_Selectionbox
```

```
          caption = ""  ' No captions for selection boxes
          alignment = swControlAlign_Indent
          options = swControlOptions_Visible + swControlOptions_Enabled
          tip = "Select an edge, face, vertex, solid body, or a component"
          Set pm_Selection = pm_Group.AddControl(SelectionID, controlType, caption, alignment, options, tip)
```

```
          Dim filters(6) As Long
          filters(0) = swSelEDGES
          filters(1) = swSelREFEDGES
          filters(2) = swSelFACES
          filters(3) = swSelVERTICES
          filters(4) = swSelSOLIDBODIES
          filters(5) = swSelCOMPONENTS
          filters(6) = swSelCOMPSDONTOVERRIDE
```

```
          pm_Selection.SingleEntityOnly = False
          pm_Selection.AllowMultipleSelectOfSameEntity = True
          pm_Selection.Height = 50
          pm_Selection.SetSelectionFilters filters
```

```
          ' Create check box
          controlType = swControlType_Checkbox
          caption = "Sample check box"
          alignment = swControlAlign_Indent
          options = swControlOptions_Visible + swControlOptions_Enabled
          tip = "Check box"
          Set pm_Control = pm_Group.AddControl(ControlID, controlType, caption, alignment, options, tip)
          isChecked = False
          pm_Control.Checked = isChecked
          bubbleToolTipTitle = "Sample bubble ToolTip Title"
          bubbleToolTipMessage = "Sample bubble ToolTip message"
          bubbleToolTipBmpFile = ""
    Else  'If the page is not created
        MsgBox "An error occurred while attempting to create the " & "PropertyManager Page", vbCritical
    End If
```

```
End Sub
Private Sub PropertyManagerPage2Handler6_AfterActivation()
End Sub
Private Sub PropertyManagerPage2Handler6_AfterClose()
    Set pm = Nothing
End Sub
Private Function PropertyManagerPage2Handler6_OnActiveXControlCreated(ByVal Id As Long, ByVal Status As Boolean) As Long
End Function
Private Sub PropertyManagerPage2Handler6_OnButtonPress(ByVal Id As Long)
End Sub
Private Sub PropertyManagerPage2Handler6_OnClose(ByVal Reason As Long)
    If Reason = swPropertyManagerPageClose_Cancel Then
        'Cancel button was clicked
        ClickedCancel = True
    ElseIf Reason = swPropertyManagerPageClose_Okay Then
        'OK button was clicked
        ClickedCancel = False
    End If
End Sub
Private Sub PropertyManagerPage2Handler6_OnCheckboxCheck(ByVal Id As Long, ByVal isChecked As Boolean)
    If isChecked Then
        pm_Control.ShowBubbleTooltip bubbleToolTipTitle, bubbleToolTipMessage, bubbleToolTipBmpFile
    Else
    End If
End Sub
Private Sub PropertyManagerPage2Handler6_OnComboboxEditChanged(ByVal Id As Long, ByVal Text As String)
End Sub
Private Sub PropertyManagerPage2Handler6_OnComboboxSelectionChanged(ByVal Id As Long, ByVal Item As Long)
End Sub
Private Sub PropertyManagerPage2Handler6_OnGroupCheck(ByVal Id As Long, ByVal Checked As Boolean)
End Sub
Private Sub PropertyManagerPage2Handler6_OnGroupExpand(ByVal Id As Long, ByVal Expanded As Boolean)
End Sub
Private Function PropertyManagerPage2Handler6_OnHelp() As Boolean
End Function
Private Function PropertyManagerPage2Handler6_OnKeystroke(ByVal Wparam As Long, ByVal Message As Long, ByVal Lparam As Long, ByVal Id As Long) As Boolean
End Function
Private Sub PropertyManagerPage2Handler6_OnListboxSelectionChanged(ByVal Id As Long, ByVal Item As Long)
End Sub
Private Function PropertyManagerPage2Handler6_OnNextPage() As Boolean
End Function
Private Sub PropertyManagerPage2Handler6_OnNumberboxChanged(ByVal Id As Long, ByVal Value As Double)
End Sub
Private Sub PropertyManagerPage2Handler6_OnOptionCheck(ByVal Id As Long)
End Sub
Private Sub PropertyManagerPage2Handler6_OnPopupMenuItem(ByVal Id As Long)
End Sub
Private Sub PropertyManagerPage2Handler6_OnPopupMenuItemUpdate(ByVal Id As Long, retval As Long)
End Sub
Private Function PropertyManagerPage2Handler6_OnPreview() As Boolean
End Function
Private Function PropertyManagerPage2Handler6_OnPreviousPage() As Boolean
End Function
Private Sub PropertyManagerPage2Handler6_OnRedo()
End Sub
Private Sub PropertyManagerPage2Handler6_OnSelectionboxCalloutCreated(ByVal Id As Long)
End Sub
Private Sub PropertyManagerPage2Handler6_OnSelectionboxCalloutDestroyed(ByVal Id As Long)
End Sub
Private Sub PropertyManagerPage2Handler6_OnSelectionboxFocusChanged(ByVal Id As Long)
End Sub
Private Sub PropertyManagerPage2Handler6_OnSelectionboxListChanged(ByVal Id As Long, ByVal Count As Long)
End Sub
Private Sub PropertyManagerPage2Handler6_OnSliderPositionChanged(ByVal Id As Long, ByVal Value As Double)
End Sub
Private Sub PropertyManagerPage2Handler6_OnSliderTrackingCompleted(ByVal Id As Long, ByVal Value As Double)
End Sub
Private Function PropertyManagerPage2Handler6_OnSubmitSelection(ByVal Id As Long, ByVal Selection As Object, ByVal SelType As Long, ItemText As String) As Boolean
     PropertyManagerPage2Handler6_OnSubmitSelection = True
End Function
Private Function PropertyManagerPage2Handler6_OnTabClicked(ByVal Id As Long) As Boolean
End Function
Private Sub PropertyManagerPage2Handler6_OnTextboxChanged(ByVal Id As Long, ByVal Text As String)
End Sub
Private Sub PropertyManagerPage2Handler6_OnUndo()
End Sub
Private Sub PropertyManagerPage2Handler6_OnWhatsNew()
End Sub
```
