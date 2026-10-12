---
title: "Create PropertyManager Page With Many Controls Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_PropertyManager_Page_With_Many_Controls_Example_VB.htm"
---

# Create PropertyManager Page With Many Controls Example (VBA)

This example shows how to create a PropertyManager page with many controls.

```
'-----------------------------------------
' Preconditions:
' 1. Copy Main into your macro.
' 2. Click Insert > Class Module, name if PropMgr, and copy PropMgr
'    into the module. (To rename the module, click View >
'    Properties Window and type PropMgr in (Name).
' 3. Click Insert > Class Module, name it PropMgrHdlr, and copy
'    PropMgrHdlr in the module.
' 4. Add a reference to SolidWorks <version> exposed
'    type libraries for add-in use.
' 5. Open a part or assembly.
' 6. Open the Immediate window.
'
' Postconditions:
' 1. Creates a PropertyManager page.
' 2. Click or type text in the different controls and
'    examine the Immediate window after action.
' 3. Click OK to close the PropertyManager
'    page and examine the Immediate window.
'----------------------------------------
'Main
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swPart As SldWorks.PartDoc
```

```
'The application's PropertyManager page
Dim swPage As PropMgr
```

```
Sub main()
```

```
    Dim nRetVal As Long
    Set swApp = CreateObject("SldWorks.Application")
    'Make sure that there is a model to which to
    'the page; if there is no model, then get rid
    'of references to any previous pages
    If swApp.ActiveDoc Is Nothing Then
        Set swPart = swApp.NewPart
        Set swPage = Nothing
    End If
```

```
    'If there is no page, create a new one and show it
    'If there is a page, then show it
    If swPage Is Nothing Then
        Set swPage = New PropMgr
        swPage.Show
    Else
        swPage.Show
    End If
End Sub
```

```
Back to top
```

```
'PropMgr
'This class defines the PropertyManager page and its controls
```

```
Option Explicit
```

```
'The PropertyManager page
Private m_Page As SldWorks.PropertyManagerPage2
```

```
'The two groups that will contain the controls
Private m_Group1 As SldWorks.PropertyManagerPageGroup
Private m_Group2 As SldWorks.PropertyManagerPageGroup
```

```
'The controls on the page
Private m_Text As SldWorks.PropertyManagerPageTextbox
Private m_Check As SldWorks.PropertyManagerPageCheckbox
Private m_Option1 As SldWorks.PropertyManagerPageOption
Private m_Option2 As SldWorks.PropertyManagerPageOption
Private m_Option3 As SldWorks.PropertyManagerPageOption
Private m_List As SldWorks.PropertyManagerPageListbox
Private m_Selection1 As SldWorks.PropertyManagerPageSelectionbox
Private m_Selection2 As SldWorks.PropertyManagerPageSelectionbox
Private m_Number As SldWorks.PropertyManagerPageNumberbox
Private m_Combo As SldWorks.PropertyManagerPageCombobox
Private m_ClearSelection As SldWorks.PropertyManagerPageCheckbox
Private m_Button As SldWorks.PropertyManagerPageButton
Private m_Label As SldWorks.PropertyManagerPageLabel
Private m_pActiveXControl As SldWorks.PropertyManagerPageActiveX
```

```
'Whether the second group is active
Private m_bGroup2 As Boolean
```

```
'The IDs for all of the controls
Const ID_GROUP1 As Long = 1
Const ID_TEXT As Long = 2
Const ID_CHECK As Long = 3
Const ID_OPTION1 As Long = 4
Const ID_OPTION2 As Long = 5
Const ID_OPTION3 As Long = 6
Const ID_LIST As Long = 7
Const ID_GROUP2 As Long = 8
Const ID_SELECTION1 As Long = 9
Const ID_SELECTION2 As Long = 10
Const ID_NUMBER As Long = 11
Const ID_COMBO As Long = 12
Const ID_BUTTON As Long = 13
Const ID_LABEL As Long = 14
Const ID_ACTIVEX As Long = 15
```

```
'Create the page and place all of the controls on it
Private Sub Layout()
    Dim swApp As SldWorks.SldWorks
```

```
    'Objects needed to create the PropertyManager page
    Dim pageHdlr As New PropMgrHdlr
    Dim swPage As SldWorks.PropertyManagerPage2
    Dim swControl As SldWorks.PropertyManagerPageControl
    Dim title As String
    Dim Message As String
    Dim caption As String
    Dim tip As String
    Dim listItems(3) As String
    Dim buttonTypes As Long
    Dim Id As Long
    Dim options As Long
    Dim filterArray(1) As Long
    Dim errors As Long
    Dim controlType As Integer
    Dim alignment As Integer
    Dim bRet As Boolean
```

```
    'Access SOLIDWORKS Design
    Set swApp = GetObject(, "SldWorks.Application")
```

```
    'Initialize the page handler
    'Pass a reference to this PropertyManager page
    pageHdlr.Init Me
```

```
    'Set some variables for the page
    title = "Sample PropertyManager"
    buttonTypes = swPropertyManager_OkayButton + swPropertyManager_CancelButton
```

```
   'Create the PropertyManager page
    Set m_Page = swApp.CreatePropertyManagerPage(title, buttonTypes, pageHdlr, errors)
```

```
    'Make sure that it was created properly
    If errors = swPropertyManagerPage_Okay Then
```

```
        'Initial set up of the dialog
        Message = "Information message that can be displayed as necessary."
        m_Page.SetMessage Message, swImportantMessageBox
```

```
        'Begin adding the controls to the PropertyManager page
        'GROUP BOX ------------------------------------------------------------------
        Id = ID_GROUP1
        caption = "Group &1"
        options = swGroupBoxOptions_Visible + swGroupBoxOptions_Expanded
        Set m_Group1 = m_Page.AddGroupBox(Id, caption, options)
        If Not m_Group1 Is Nothing Then
            'Place these controls in the first group
            'CONTROL Textbox  --------------------------------------------------------------------
            Id = ID_TEXT
            controlType = swControlType_Textbox
            caption = "Sample text box"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "Text box"
            Set swControl = Nothing
            Set swControl = m_Group1.AddControl(Id, controlType, caption, alignment, options, tip)
            If Not swControl Is Nothing Then
                Set m_Text = swControl
               'm_Text.Style = swconst.swPropMgrPageTextBoxStyle_e.
            End If
            'CONTROL Checkbox  --------------------------------------------------------------------
            Id = ID_CHECK
            controlType = swControlType_Checkbox
            caption = "Sample check box"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "Check box"
            Set swControl = m_Group1.AddControl(Id, controlType, caption, alignment, options, tip)
            If Not swControl Is Nothing Then
                Set m_Check = swControl
                m_Check.Checked = False
                End If
            'CONTROL Option  --------------------------------------------------------------------
            Id = ID_OPTION1
            controlType = swControlType_Option
            caption = "Radio button 1"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "Option 1"
            Set swControl = m_Group1.AddControl(Id, controlType, caption, alignment, options, tip)
            If Not swControl Is Nothing Then
                Set m_Option1 = swControl
                m_Option1.Checked = True
            End If
            'CONTROL Option  --------------------------------------------------------------------
            Id = ID_OPTION2
            controlType = swControlType_Option
            caption = "Radio button 2"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "Option 2"
            Set swControl = m_Group1.AddControl(Id, controlType, caption, alignment, options, tip)
            If Not swControl Is Nothing Then
                Set m_Option2 = swControl
                m_Option2.Checked = False
            End If
            'CONTROL Option  --------------------------------------------------------------------
            Id = ID_OPTION3
            controlType = swControlType_Option
            caption = "Radio button 3"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "Option 3"
            Set swControl = m_Group1.AddControl(Id, controlType, caption, alignment, options, tip)
            If Not swControl Is Nothing Then
                Set m_Option3 = swControl
                m_Option3.Checked = False
            End If
            'CONTROL List box  -------------------------------------------------------------------
            Id = ID_LIST
            controlType = swControlType_Listbox
            caption = "Sample list box"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "List box"
            Set swControl = m_Group1.AddControl(Id, controlType, caption, alignment, options, tip)
            If Not swControl Is Nothing Then
                Set m_List = swControl
                m_List.Height = 50
                listItems(0) = "One Fish"
                listItems(1) = "Two Fish"
                listItems(2) = "Red Fish"
                listItems(3) = "Blue Fish"
                m_List.AddItems (listItems)
                m_List.CurrentSelection = 2
            End If
            'CONTROL Button --------------------------------------------------------------------
            Id = ID_BUTTON
            controlType = swControlType_Button
            caption = "Sample button"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "Button"
            Set swControl = m_Group1.AddControl(Id, controlType, caption, alignment, options, tip)
            If Not swControl Is Nothing Then
                Set m_Button = swControl
            End If
        End If
        'GROUP BOX ------------------------------------------------------------------
        Id = ID_GROUP2
        caption = "Group &2"
        options = swGroupBoxOptions_Visible + swGroupBoxOptions_Checkbox '+ swGroupBoxOptions_Expanded + swGroupBoxOptions_Checked
        m_bGroup2 = False  'Mark that the second group is disabled
        Set m_Group2 = m_Page.AddGroupBox(Id, caption, options)
        If Not m_Group2 Is Nothing Then
            'Place these controls in the second group
            'CONTROL Label --------------------------------------------------------------------
            Id = ID_LABEL
            controlType = swControlType_Label
            caption = "Sample label"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "Label"
            Set swControl = m_Group2.AddControl(Id, controlType, caption, alignment, options, tip)
            If Not swControl Is Nothing Then
                Set m_Label = swControl
            End If
            'CONTROL Selection box  --------------------------------------------------------------
            Id = ID_SELECTION1
            controlType = swControlType_Selectionbox
            caption = "Sample selection box"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "Select faces and vertices"
            Set swControl = m_Group2.AddControl(Id, controlType, caption, alignment, options, tip)
            If Not swControl Is Nothing Then
                Set m_Selection1 = swControl
                filterArray(0) = swSelFACES
                filterArray(1) = swSelVERTICES
                m_Selection1.SetSelectionFilters (filterArray)
                m_Selection1.SingleEntityOnly = True
                m_Selection1.Height = 50
                m_Selection1.Mark = 1
            End If
            'CONTROL Selection box  --------------------------------------------------------------
            Id = ID_SELECTION2
            controlType = swControlType_Selectionbox
            caption = "Sample selection box"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "Select faces and vertices"
            Set swControl = m_Group2.AddControl(Id, controlType, caption, alignment, options, tip)
            If Not swControl Is Nothing Then
                Set m_Selection2 = swControl
                filterArray(0) = swSelFACES
                filterArray(1) = swSelVERTICES
                m_Selection2.SetSelectionFilters (filterArray)
                m_Selection2.SingleEntityOnly = True
                m_Selection2.Height = 50
                m_Selection2.Mark = 2
            End If
            'CONTROL Number box  -----------------------------------------------------------------
            Id = ID_NUMBER
            controlType = swControlType_Numberbox
            caption = "Sample number box"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "Number box"
            Set swControl = m_Group2.AddControl(Id, controlType, caption, alignment, options, tip)
            If Not swControl Is Nothing Then
                Set m_Number = swControl
                m_Number.SetRange2 swNumberBox_Length, -0.01, 0.01, True, 0.00001, 0.0001, 0.00005
                m_Number.Value = 0.01
                m_Number.Style = swPropMgrPageNumberBoxStyle_e.swPropMgrPageNumberBoxStyle_Thumbwheel
                Debug.Print m_Number.Style
            End If
            'CONTROL Combo box  ------------------------------------------------------------------
            Id = ID_COMBO
            controlType = swControlType_Combobox
            caption = "Sample combo list box"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "Combo box"
            Set swControl = m_Group2.AddControl(Id, controlType, caption, alignment, options, tip)
            If Not swControl Is Nothing Then
            Set m_Combo = swControl
            m_Combo.Height = 50
                listItems(0) = "One Fish"
                listItems(1) = "Two Fish"
                listItems(2) = "Red Fish"
                listItems(3) = "Blue Fish"
                m_Combo.AddItems (listItems)
                m_Combo.CurrentSelection = 1
            End If
        End If
    Else
        swApp.SendMsgToUser2 "There was an error creating the Property Manager page.", swMbInformation, swMbOk
    End If
End Sub
'Display the PropertyManager page
Public Sub Show()
    Dim nRetVal As Long
```

```
    nRetVal = m_Page.Show
```

```
End Sub
'Generate the PropertyManagre page and its controls
Private Sub Class_Initialize()
    Layout
End Sub
```

```
'Callback called by PropertyManagerPage2Handler5_OnButtonPress
'in the PropertyManagerPage2Handler5 class
'This implementation just clears the selections
Public Sub OnButtonPressed(ByVal Id As Long)
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim nSelCount As Long
    Dim i As Long
```

```
    If Id = ID_BUTTON Then
        Set swApp = GetObject(, "SldWorks.Application")
        Set swModel = swApp.ActiveDoc
        Set swSelMgr = swModel.SelectionManager
        nSelCount = swSelMgr.GetSelectedObjectCount
        For i = 1 To nSelCount
            Debug.Print "SelMark(" + Str(i) + ") =" + Str(swSelMgr.GetSelectedObjectMark(i))
        Next i
        swModel.ClearSelection2 True
    End If
End Sub
```

```
Back to top
```

```
'PropMgrHdlr
' This file is the implementation of the PropertyManagerPage2Handler5
' interface
' Each of these methods is called when its corresponding
' notification is fired from within SOLIDWORKS Design
' It is customary to have notifications use callback
' functions defined within the main application to perform
' any desired actions
Option Explicit
Implements PropertyManagerPage2Handler5
' Variable that provides access to the PropertyManager page
Dim m_PageObj As PropMgr
' This method is called to initialize the handler
Public Sub Init(pageObj As PropMgr)
    Set m_PageObj = pageObj
End Sub
Private Sub Class_Initialize()
    Debug.Print "Class_Initialize"
End Sub
Private Sub Class_Terminate()
    Debug.Print "Class_Terminate"
End Sub
'These methods are the implementations of the SOLIDWORKS Design notifications
Private Sub PropertyManagerPage2Handler5_AfterClose()
    Debug.Print "PropertyManagerPage2Handler5_AfterClose"
End Sub
Private Function PropertyManagerPage2Handler5_OnActiveXControlCreated(ByVal Id As Long, ByVal Status As Boolean) As Long
    Debug.Print "PropertyManagerPage2Handler5_OnActiveXControlCreated"
End Function
Private Sub PropertyManagerPage2Handler5_OnButtonPress(ByVal Id As Long)
    m_PageObj.OnButtonPressed (Id)
End Sub
Private Sub PropertyManagerPage2Handler5_OnCancel()
    Debug.Print "PropertyManagerPage2Handler5_OnCancel"
End Sub
Private Sub PropertyManagerPage2Handler5_OnCheckboxCheck(ByVal Id As Long, ByVal Checked As Boolean)
    Debug.Print "PropertyManagerPage2Handler5_OnCheckboxCheck"
End Sub
Private Sub PropertyManagerPage2Handler5_OnClose(ByVal Reason As Long)
    Debug.Print "PropertyManagerPage2Handler5_OnClose"
End Sub
Private Sub PropertyManagerPage2Handler5_OnComboboxEditChanged(ByVal Id As Long, ByVal Text As String)
    Debug.Print "PropertyManagerPage2Handler5_OnComboboxEditChanged"
End Sub
Private Sub PropertyManagerPage2Handler5_OnComboboxSelectionChanged(ByVal Id As Long, ByVal Item As Long)
    Debug.Print "PropertyManagerPage2Handler5_OnComboboxSelectionChanged"
End Sub
Private Sub PropertyManagerPage2Handler5_OnGroupCheck(ByVal Id As Long, ByVal Checked As Boolean)
    Debug.Print "PropertyManagerPage2Handler5_OnGroupCheck"
End Sub
Private Sub PropertyManagerPage2Handler5_OnGroupExpand(ByVal Id As Long, ByVal Expanded As Boolean)
    Debug.Print "PropertyManagerPage2Handler5_OnGroupExpand"
End Sub
Private Function PropertyManagerPage2Handler5_OnHelp() As Boolean
    Debug.Print "PropertyManagerPage2Handler5_OnHelp"
End Function
Private Sub PropertyManagerPage2Handler5_OnListboxSelectionChanged(ByVal Id As Long, ByVal Item As Long)
    Debug.Print "PropertyManagerPage2Handler5_OnListboxSelectionChanged"
End Sub
Private Function PropertyManagerPage2Handler5_OnNextPage() As Boolean
    Debug.Print "PropertyManagerPage2Handler5_OnNextPage"
End Function
 Private Sub PropertyManagerPage2Handler5_OnNumberboxChanged(ByVal Id As Long, ByVal Value As Double)
    Debug.Print "PropertyManagerPage2Handler5_OnNumberboxChanged"
End Sub
Private Sub PropertyManagerPage2Handler5_OnOK()
    Debug.Print "PropertyManagerPage2Handler5_OnOK"
End Sub
Private Sub PropertyManagerPage2Handler5_OnOptionCheck(ByVal Id As Long)
    Debug.Print "PropertyManagerPage2Handler5_OnOptionCheck"
End Sub
Private Function PropertyManagerPage2Handler5_OnPreviousPage() As Boolean
    Debug.Print "PropertyManagerPage2Handler5_OnPreviousPage"
End Function
Private Sub PropertyManagerPage2Handler5_OnSelectionboxCalloutCreated(ByVal Id As Long)
    Debug.Print "PropertyManagerPage2Handler5_OnSelectionboxCalloutCreated"
End Sub
Private Sub PropertyManagerPage2Handler5_OnSelectionboxCalloutDestroyed(ByVal Id As Long)
    Debug.Print "PropertyManagerPage2Handler5_OnSelectionboxCalloutDestroyed"
End Sub
Private Sub PropertyManagerPage2Handler5_OnSelectionboxFocusChanged(ByVal Id As Long)
    Debug.Print "PropertyManagerPage2Handler5_OnSelectionboxFocusChanged"
End Sub
Private Sub PropertyManagerPage2Handler5_OnSelectionboxListChanged(ByVal Id As Long, ByVal Count As Long)
    Debug.Print "PropertyManagerPage2Handler5_OnSelectionboxListChanged"
End Sub
Private Sub PropertyManagerPage2Handler5_OnTextboxChanged(ByVal Id As Long, ByVal Text As String)
    Debug.Print "PropertyManagerPage2Handler5_OnTextboxChanged"
End Sub
Private Function PropertyManagerPage2Handler5_OnPreview() As Boolean
    Debug.Print "PropertyManagerPage2Handler5_OnPreview"
End Function
Private Function PropertyManagerPage2Handler5_OnSubmitSelection(ByVal Id As Long, ByVal Selection As Object, ByVal SelType As Long, ItemText As String) As Boolean
    Debug.Print "PropertyManagerPage2Handler5_OnSubmitSelection"
End Function
Private Function PropertyManagerPage2Handler5_OnTabClicked(ByVal Id As Long) As Boolean
    Debug.Print "PropertyManagerPage2Handler5_OnTabClicked"
End Function
Private Sub PropertyManagerPage2Handler5_OnSliderPositionChanged(ByVal Id As Long, ByVal Value As Double)
    Debug.Print "PropertyManagerPage2Handler5_OnSliderPositionChanged"
End Sub
Private Sub PropertyManagerPage2Handler5_OnWhatsNew()
    Debug.Print "PropertyManagerPage2Handler5_OnWhatsNew"
End Sub
Private Sub PropertyManagerPage2Handler5_OnUndo()
    Debug.Print "PropertyManagerPage2Handler5_OnUndo"
End Sub
Private Sub PropertyManagerPage2Handler5_OnSliderTrackingCompleted(ByVal Id As Long, ByVal Value As Double)
    Debug.Print "PropertyManagerPage2Handler5_OnSliderTrackingCompleted"
End Sub
Private Function PropertyManagerPage2Handler5_OnKeystroke(ByVal Wparam As Long, ByVal Message As Long, ByVal Lparam As Long, ByVal Id As Long) As Boolean
    Debug.Print "PropertyManagerPage2Handler5_OnKeystroke"
End Function
Private Sub PropertyManagerPage2Handler5_OnPopupMenuItemUpdate(ByVal Id As Long, retVal As Long)
    Debug.Print "PropertyManagerPage2Handler5_OnPopupMenuItemUpdate"
End Sub
Private Sub PropertyManagerPage2Handler5_OnPopupMenuItem(ByVal Id As Long)
    Debug.Print "PropertyManagerPage2Handler5_OnPopupMenuItem"
End Sub
Private Sub PropertyManagerPage2Handler5_AfterActivation()
    Debug.Print "PropertyManagerPage2Handler5_AfterActivation"
End Sub
```

```
Back to top
```
