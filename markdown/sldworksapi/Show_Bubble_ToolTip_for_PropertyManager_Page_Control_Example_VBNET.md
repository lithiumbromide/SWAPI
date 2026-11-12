---
title: "Show Bubble ToolTip for PropertyManager Page Control Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Show_Bubble_ToolTip_for_PropertyManager_Page_Control_Example_VBNET.htm"
---

# Show Bubble ToolTip for PropertyManager Page Control Example (VB.NET)

This example shows how to create a PropertyManager page. When the check box on the PropertyManager page is selected, a bubble ToolTip is displayed. This type of ToolTip is useful for validating data typed or selected by users in controls on a PropertyManager page.

```
'--------------------------------------
' Preconditions:
' 1. Copy SolidWorksMacro.vb to your project.
' 2. Add a class module called PropMgrHdlr.vb and copy
'    PropMgrHdlr.vb to that module.
' 3. Click Project > Add Reference, browse to install_dir\api\redist,
'    select SolidWorks.Interop.swpublished.dll > OK.
' 4. Verify that the Tools > Options > System Options > Stop VSTA debugger
'    on macro exit checkbox is clear.
' 5. Open a part.
'
' Postconditions:
' 1. Creates and displays a PropertyManager page.
' 2. Select Sample check box to display a bubble ToolTip.
' 3. Click outside the bubble ToolTip to close it.
'    NOTE: Clearing Sample check box does not display
'    the bubble ToolTip.
'---------------------------------------
'SolidWorksMacro.vb
```

```
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
```

```
Partial Class SolidWorksMacro
```

```
    Public swModel As ModelDoc2
    Public swSelMgr As SelectionMgr
    Public pm As PropMgrHdlr
```

```
    Public Sub main()
```

```
        swModel = swApp.ActiveDoc
        swSelMgr = swModel.SelectionManager
```

```
        'Create a new instance of the PropertyManager class
        pm = New PropMgrHdlr(swApp)
        pm.Show()
    End Sub
```

```
    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks
End Class
```

```
Back to top
```

```
'PropMgrHdlr.vb
```

```
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.swpublished
Imports System
Imports System.Runtime.InteropServices
```

```
<ComVisibleAttribute(True)> Public Class PropMgrHdlr
```

```
    'Required for PropertyManager page controls
    Implements PropertyManagerPage2Handler6
```

```
    'Objects required for the PropertyManager page
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
    Dim ClickedCancel As Boolean
    Dim bubbleToolTipTitle As String
    Dim bubbleToolTipMessage As String
    Dim bubbleToolTipBmpFile As String
    Dim isChecked As Boolean
```

```
    Sub Show()
        pm_Page.Show()
    End Sub
```

```
    Sub New(ByVal swApp As SolidWorks.Interop.sldworks.SldWorks)
        Dim PageTitle As String
        Dim caption As String
        Dim tip As String
        Dim options As Integer
        Dim longerrors As Integer
        Dim controlType As Integer
        Dim alignment As Integer
```

```
        'Set the variables for the page
        PageTitle = "Sample PropertyManager page"
        options = swPropertyManagerButtonTypes_e.swPropertyManager_OkayButton + swPropertyManagerButtonTypes_e.swPropertyManager_CancelButton + swPropertyManagerPageOptions_e.swPropertyManagerOptions_LockedPage + swPropertyManagerPageOptions_e.swPropertyManagerOptions_PushpinButton
```

```
        'Create the PropertyManager page
        pm_Page = swApp.CreatePropertyManagerPage(PageTitle, options, Me, longerrors)
```

```
        'Make sure that the page was created properly
        If longerrors = swPropertyManagerPageStatus_e.swPropertyManagerPage_Okay Then
            'Begin adding the controls to the page
            'Create the group box
            caption = "Sample Group Box"
            options = swAddGroupBoxOptions_e.swGroupBoxOptions_Visible + swAddGroupBoxOptions_e.swGroupBoxOptions_Expanded
            pm_Group = pm_Page.AddGroupBox(GroupID, caption, options)
```

```
            'Create selection box
            controlType = swPropertyManagerPageControlType_e.swControlType_Selectionbox
```

```
            caption = ""  ' No caption for selection boxes
            alignment = swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent
            options = swAddControlOptions_e.swControlOptions_Visible + swAddControlOptions_e.swControlOptions_Enabled
            tip = "Select an edge, face, vertex, solid body, or a component"
            pm_Selection = pm_Group.AddControl(SelectionID, controlType, caption, alignment, options, tip)
            Dim filters(6) As Integer
            filters(0) = swSelectType_e.swSelEDGES
            filters(1) = swSelectType_e.swSelREFEDGES
            filters(2) = swSelectType_e.swSelFACES
            filters(3) = swSelectType_e.swSelVERTICES
            filters(4) = swSelectType_e.swSelSOLIDBODIES
            filters(5) = swSelectType_e.swSelCOMPONENTS
            filters(6) = swSelectType_e.swSelCOMPSDONTOVERRIDE
            pm_Selection.SingleEntityOnly = False
            pm_Selection.AllowMultipleSelectOfSameEntity = True
            pm_Selection.Height = 50
            pm_Selection.SetSelectionFilters(filters)
```

```
            ' Create check box
            controlType = swPropertyManagerPageControlType_e.swControlType_Checkbox
            caption = "Sample check box"
            alignment = swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent
            options = swAddControlOptions_e.swControlOptions_Visible + swAddControlOptions_e.swControlOptions_Enabled
            tip = "Check box"
            pm_Control = pm_Group.AddControl(ControlID, controlType, caption, alignment, options, tip)
            isChecked = False
            pm_Control.Checked = isChecked
            bubbleToolTipTitle = "Sample bubble ToolTip Title"
            bubbleToolTipMessage = "Sample bubble ToolTip message"
            bubbleToolTipBmpFile = ""
        Else  'If the page is not created
            MsgBox("An error occurred while attempting to create the " & "PropertyManager Page", vbCritical)
        End If
    End Sub
```

```
    Private Sub PropertyManagerPage2Handler6_OnCheckboxCheck(ByVal Id As Integer, ByVal isChecked As Boolean) Implements PropertyManagerPage2Handler6.OnCheckboxCheck
        If isChecked Then
            pm_Control.ShowBubbleTooltip(bubbleToolTipTitle, bubbleToolTipMessage, bubbleToolTipBmpFile)
        Else
        End If
    End Sub
    Private Sub PropertyManagerPage2Handler6_AfterClose() Implements PropertyManagerPage2Handler6.AfterClose
    End Sub
    Private Sub PropertyManagerPage2Handler6_OnButtonPress(ByVal Id As Integer) Implements PropertyManagerPage2Handler6.OnButtonPress
    End Sub
```

```
    Private Sub PropertyManagerPage2Handler6_OnClose(ByVal Reason As Integer) Implements PropertyManagerPage2Handler6.OnClose
        If Reason = swPropertyManagerPageCloseReasons_e.swPropertyManagerPageClose_Cancel Then
            'Cancel button was clicked
            ClickedCancel = True
        ElseIf Reason = swPropertyManagerPageCloseReasons_e.swPropertyManagerPageClose_Okay Then
            'OK button was clicked
            ClickedCancel = False
        End If
    End Sub
    Private Sub PropertyManagerPage2Handler6_OnSelectionboxCalloutCreated(ByVal Id As Integer) Implements PropertyManagerPage2Handler6.OnSelectionboxCalloutCreated
    End Sub
    Private Sub PropertyManagerPage2Handler6_OnComboboxEditChanged(ByVal Id As Integer, ByVal Text As String) Implements PropertyManagerPage2Handler6.OnComboboxEditChanged
    End Sub
    Private Sub PropertyManagerPage2Handler6_OnComboboxSelectionChanged(ByVal Id As Integer, ByVal Item As Integer) Implements PropertyManagerPage2Handler6.OnComboboxSelectionChanged
    End Sub
    Private Sub PropertyManagerPage2Handler6_OnGroupCheck(ByVal Id As Integer, ByVal Checked As Boolean) Implements PropertyManagerPage2Handler6.OnGroupCheck
    End Sub
    Private Sub PropertyManagerPage2Handler6_OnGroupExpand(ByVal Id As Integer, ByVal Expanded As Boolean) Implements PropertyManagerPage2Handler6.OnGroupExpand
    End Sub
    Private Function PropertyManagerPage2Handler6_OnHelp() As Boolean Implements PropertyManagerPage2Handler6.OnHelp
    End Function
    Private Function PropertyManagerPage2Handler6_OnKeystroke(ByVal Wparam As Integer, ByVal Message As Integer, ByVal Lparam As Integer, ByVal Id As Integer) As Boolean Implements PropertyManagerPage2Handler6.OnKeystroke
    End Function
    Private Sub PropertyManagerPage2Handler6_OnListboxSelectionChanged(ByVal Id As Integer, ByVal Item As Integer) Implements PropertyManagerPage2Handler6.OnListboxSelectionChanged
    End Sub
    Private Function PropertyManagerPage2Handler6_OnNextPage() As Boolean Implements PropertyManagerPage2Handler6.OnNextPage
    End Function
    Private Sub PropertyManagerPage2Handler6_OnNumberboxChanged(ByVal Id As Integer, ByVal Value As Double) Implements PropertyManagerPage2Handler6.OnNumberboxChanged
    End Sub
    Private Sub PropertyManagerPage2Handler6_OnOptionCheck(ByVal Id As Integer) Implements PropertyManagerPage2Handler6.OnOptionCheck
    End Sub
    Private Sub PropertyManagerPage2Handler6_OnPopupMenuItem(ByVal Id As Integer) Implements PropertyManagerPage2Handler6.OnPopupMenuItem
    End Sub
    Private Sub PropertyManagerPage2Handler6_OnPopupMenuItemUpdate(ByVal Id As Integer, ByRef retval As Integer) Implements PropertyManagerPage2Handler6.OnPopupMenuItemUpdate
    End Sub
    Private Function PropertyManagerPage2Handler6_OnPreview() As Boolean Implements PropertyManagerPage2Handler6.OnPreview
    End Function
    Private Function PropertyManagerPage2Handler6_OnPreviousPage() As Boolean Implements PropertyManagerPage2Handler6.OnPreviousPage
    End Function
    Private Sub PropertyManagerPage2Handler6_OnRedo() Implements PropertyManagerPage2Handler6.OnRedo
    End Sub
    Private Sub PropertyManagerPage2Handler6_OnSelectionboxCalloutDestroyed(ByVal Id As Integer) Implements PropertyManagerPage2Handler6.OnSelectionboxCalloutDestroyed
    End Sub
    Private Sub PropertyManagerPage2Handler6_OnSelectionboxFocusChanged(ByVal Id As Integer) Implements PropertyManagerPage2Handler6.OnSelectionboxFocusChanged
    End Sub
    Private Sub PropertyManagerPage2Handler6_OnSelectionboxListChanged(ByVal Id As Integer, ByVal Count As Integer) Implements PropertyManagerPage2Handler6.OnSelectionboxListChanged
    End Sub
    Private Sub PropertyManagerPage2Handler6_OnSliderPositionChanged(ByVal Id As Integer, ByVal Value As Double) Implements PropertyManagerPage2Handler6.OnSliderPositionChanged
    End Sub
    Private Sub PropertyManagerPage2Handler6_OnSliderTrackingCompleted(ByVal Id As Integer, ByVal Value As Double) Implements PropertyManagerPage2Handler6.OnSliderTrackingCompleted
    End Sub
    Private Function PropertyManagerPage2Handler6_OnSubmitSelection(ByVal Id As Integer, ByVal Selection As Object, ByVal SelType As Integer, ByRef ItemText As String) As Boolean Implements PropertyManagerPage2Handler6.OnSubmitSelection
        PropertyManagerPage2Handler6_OnSubmitSelection = True
    End Function
    Private Function PropertyManagerPage2Handler6_OnTabClicked(ByVal Id As Integer) As Boolean Implements PropertyManagerPage2Handler6.OnTabClicked
    End Function
    Private Sub PropertyManagerPage2Handler6_OnTextboxChanged(ByVal Id As Integer, ByVal Text As String) Implements PropertyManagerPage2Handler6.OnTextboxChanged
    End Sub
    Private Sub PropertyManagerPage2Handler6_OnUndo() Implements PropertyManagerPage2Handler6.OnUndo
    End Sub
    Private Sub PropertyManagerPage2Handler6_OnWhatsNew() Implements PropertyManagerPage2Handler6.OnWhatsNew
    End Sub
    Private Function PropertyManagerPage2Handler6_OnActiveXControlCreated(ByVal Id As Integer, ByVal Status As Boolean) As Integer Implements PropertyManagerPage2Handler6.OnActiveXControlCreated
    End Function
    Private Sub PropertyManagerPage2Handler6_AfterActivation() Implements PropertyManagerPage2Handler6.AfterActivation
    End Sub
```

```
End Class
```
