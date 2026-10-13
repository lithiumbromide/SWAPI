---
title: "Create PropertyManager Page and Selectable Triad Manipulator Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_PropertyManager_Page_and_Selectable_Triad_Manipulator_Example_VB.htm"
---

# Create PropertyManager Page and Selectable Triad Manipulator Example (VBA)

This example shows how to create a PropertyManager page and a triad manipulator you can select.

```
'---------------------------------------------------------------------------------
' Preconditions:
' 1. Click Tools > References > SolidWorks <version> exposed type libraries for
'    add-in use > OK.
' 2. Copy Macros to the main module and rename it Macros. (To rename the module,
'    click View > Properties Window and type Macros in (Name).)
' 3. Click Insert > Class Module and copy PropMgr to that class module and
'    name it PropMgr.
' 4. Click Insert > Class Module and copy PropMgrHdlr to that class module
'    and name it PropMgrHdlr.
' 5. Click Insert > Class Module and copy swDragManipHdlr to that class module
'    and name it swDragManipHdlr.
' 6. Open public_documents\samples\tutorial\api\assem20.sldasm.
' 7. Select the top face of the left-side component.
'
' Postconditions:
' 1. Displays the Sample PropertyManager page.
' 2. Click Select Entity to show the ID of the face
'    selected in Preconditions step 7.
'    a. Click OK to close the message box.
'    b. Examine the Immediate window.
' 3. Selects the top face of the right-side component.
' 4. Click Create triad manipulator to create a triad
'    manipulator at the pick point on the top face
'    of the right-side component.
'    a. Right-click the triad manipulator.
'    b. Examine the Immediate window.
' 5. Click OK one or two times to close the
'    PropertyManager page.
' 6. Click any handle on the triad manipulator.
' 7. Examine the Immediate window.
' 8. Press F5 to finish executing the macro and
'    remove the triad manipulator.
'--------------------------------------------------------------------------------
'Macros
Option Explicit
Dim swApp As SldWorks.SldWorks
Dim swPart As SldWorks.PartDoc
```

```
' Application's PropertyManager page
Dim swPage As PropMgr
```

```
Sub main()
```

```
    Dim nRetVal As Long
    Set swApp = CreateObject("SldWorks.Application")
```

```
    ' Make sure that there is a model open to which to add the
    ' PropertyManager page; if there is no model, then get rid
    ' of references to any previous pages
    If swApp.ActiveDoc Is Nothing Then
        Set swPart = swApp.NewPart
        Set swPage = Nothing
    End If
```

```
    ' If there is no PropertyManager page, then create a new one and show it,
    ' or if there is a PropertyManager page, then show it
    If swPage Is Nothing Then
        Set swPage = New PropMgr
        swPage.Show 'Display it
    Else
        swPage.Show
    End If
End Sub
```

[Back to top](#Top)

```
'PropMgr
' This class defines the PropertyManager page and its controls
Option Explicit
```

```
' PropertyManager page
Private m_Page  As SldWorks.PropertyManagerPage2
```

```
' Two groups contains the controls
Private m_Group As SldWorks.PropertyManagerPageGroup
```

```
' Controls on the page
Private m_Text As SldWorks.PropertyManagerPageTextbox
Private m_Check As SldWorks.PropertyManagerPageCheckbox
Private m_Selection As SldWorks.PropertyManagerPageSelectionbox
Private m_ClearSelection As SldWorks.PropertyManagerPageCheckbox
Private m_Button As SldWorks.PropertyManagerPageButton
Private m_Button1  As SldWorks.PropertyManagerPageButton
Private m_Label As SldWorks.PropertyManagerPageLabel
```

```
' To determine whether the second group is active
Private m_bGroup As Boolean
```

```
' IDs for all of the controls
Const ID_GROUP As Long = 1
Const ID_SELECTION As Long = 2
Const ID_BUTTON As Long = 3
Const ID_BUTTON1 As Long = 4
Const ID_LABEL As Long = 5
```

```
' Generate the PropertyManager page and its controls
Dim swManip As SldWorks.Manipulator
Dim swDrag As SldWorks.DragArrowManipulator
Dim swTriad As SldWorks.TriadManipulator
Dim swDragHdlr As swDragManipHdlr
Public swFace As SldWorks.Face2
```

```
' Create the page and place all of the controls on it
Private Sub Layout()
    Dim swApp As SldWorks.SldWorks
```

```
    ' Objects needed to create the PropertyManager page
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
    Dim filterArray(2) As Long
    Dim errors As Long
    Dim controlType As Integer
    Dim alignment As Integer
    Dim bRet As Boolean
```

```
    ' Access SOLIDWORKS Design
    Set swApp = GetObject(, "SldWorks.Application")
```

```
    ' Initialize the Property page handler
    ' Pass a reference to this PropertyManager page
    pageHdlr.Init Me
```

```
    ' Set some variables for the PropertyManager page
    title = "Sample PropertyManager"
    buttonTypes = swPropertyManager_OkayButton + swPropertyManager_CancelButton
```

```
   ' Create the PropertyManager page
    Set m_Page = swApp.CreatePropertyManagerPage(title, buttonTypes, pageHdlr, errors)
```

```
    ' Make sure that the PropertyManger page was correctly created
    If errors = swPropertyManagerPage_Okay Then
        ' Initial setup of the dialog
        Message = "Information message that can be displayed as necessary."
        m_Page.SetMessage Message, swImportantMessageBox
        ' Begin adding the required controls to the dialog
        'GROUP Box ------------------------------------------------------------------
        Id = ID_GROUP
        caption = "Group &1"
        options = swGroupBoxOptions_Visible + swGroupBoxOptions_Checkbox + swGroupBoxOptions_Expanded + swGroupBoxOptions_Checked
        m_bGroup = False  ' Mark that the second group is disabled
        Set m_Group = m_Page.AddGroupBox(Id, caption, options)
        If Not m_Group Is Nothing Then
            ' Place these controls in the second group
            'CONTROL Label --------------------------------------------------------------------
            Id = ID_LABEL
            controlType = swControlType_Label
            caption = "Selection box"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "Label"
            Set swControl = m_Group.AddControl(Id, controlType, caption, alignment, options, tip)
            If Not swControl Is Nothing Then
                Set m_Label = swControl
            End If

            'CONTROL Selection box  ------------------------------------------------------------------
            Id = ID_SELECTION
            controlType = swControlType_Selectionbox
            caption = "Sample selection box"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "Select faces and vertices"
            Set swControl = m_Group.AddControl(Id, controlType, caption, alignment, options, tip)
            If Not swControl Is Nothing Then
                Set m_Selection = swControl
                filterArray(0) = swSelFACES
                filterArray(1) = swSelVERTICES
                filterArray(2) = swSelMANIPULATORS
                m_Selection.SetSelectionFilters (filterArray)
                m_Selection.AllowMultipleSelectOfSameEntity = True
                m_Selection.Height = 50
                m_Selection.Mark = 1
            End If

            'CONTROL Button --------------------------------------------------------------------
            Id = ID_BUTTON
            controlType = swControlType_Button
            caption = "Create triad manipulator"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "Button"
            Set swControl = m_Group.AddControl(Id, controlType, caption, alignment, options, tip)
            If Not swControl Is Nothing Then
                Set m_Button = swControl
            End If
```

```
            'CONTROL Button --------------------------------------------------------------------
            Id = ID_BUTTON1
            controlType = swControlType_Button
            caption = "Select Entity"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "Button"
            Set swControl = m_Group.AddControl(Id, controlType, caption, alignment, options, tip)
            If Not swControl Is Nothing Then
                Set m_Button1 = swControl
            End If
        End If
    Else
        swApp.SendMsgToUser2 "There was an error creating the PropertyManager page.", swMbInformation, swMbOk
    End If
End Sub
```

```
' Display the Property Manager page
Public Sub Show()
    Dim nRetVal As Long
    Dim bRet As Boolean
```

```
    nRetVal = m_Page.Show
    bRet = m_Page.SetMessage("Some message string.", swAnnotationVisible)
    Debug.Assert bRet
End Sub
```

```
Private Sub Class_Initialize()
    Layout
End Sub
```

```
Private Sub Class_Terminate()
```

```
End Sub
```

```
' Callback called by PropertyManagerPage2Handler_OnButtonPress
' in the PropertyManager page handler class
' This implementation just clears the selections
Public Sub OnButtonPressed(ByVal Id As Long)
    Dim swApp As SldWorks.SldWorks
    Dim swMathUtil As SldWorks.MathUtility
    Dim swModel As SldWorks.ModelDoc2
    Dim swModViewMgr As SldWorks.ModelViewManager
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim vPickPt As Variant
    Dim swPickPt As SldWorks.MathPoint
    Dim origin As SldWorks.MathPoint
    Dim pt As Variant
    Dim obj As Object
    Dim boolstatus As Boolean
    Dim nVector(2) As Double
    Dim vVector As Variant
    Dim swN As SldWorks.MathVector
```

```
    Set swDragHdlr = New swDragManipHdlr
    Set swApp = Application.SldWorks
    Set swMathUtil = swApp.GetMathUtility
    Set swModel = swApp.ActiveDoc
```

```
    If Id = ID_BUTTON1 Then
         Set swSelMgr = swModel.SelectionManager
         Id = swSelMgr.GetSelectedObjectCount2(-1)
         Set obj = swSelMgr.GetSelectedObject6(1, -1)
         If obj Is Nothing Then
            swApp.SendMsgToUser2 "Not selected.", swMbWarning, swMbOk
         Else
            swApp.SendMsgToUser2 "Selected, ID = " & swSelMgr.GetSelectedObjectType2(1), swMbWarning, swMbOk
            Debug.Print "SelType      = " & swSelMgr.GetSelectedObjectType2(1)
         End If
         Exit Sub
    End If
```

```
    swModel.ClearSelection2 True
```

```
    boolstatus = swModel.Extension.SelectByRay(0.112447854353888, 0.084630970938349, -7.93916624701296E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 3.53102873173539E-03, 2, False, 0, 0)
    Set swSelMgr = swModel.SelectionManager
    Set swFace = swSelMgr.GetSelectedObject6(1, -1)
    nVector(0) = 0:     nVector(1) = 1:     nVector(2) = 0
    vVector = nVector
    Set swN = swMathUtil.CreateVector((vVector))
    vPickPt = swSelMgr.GetSelectionPoint(1)
    Set swPickPt = swMathUtil.CreatePoint((vPickPt))
    Set swModViewMgr = swModel.ModelViewManager
    If Id = ID_BUTTON Then
        Set swManip = swModViewMgr.CreateManipulator(swManipulatorType_e.swTriadManipulator, swDragHdlr)
        Set swTriad = swManip.GetSpecificManipulator
        swTriad.origin = swPickPt
        swManip.Show swModel
        swManip.Selectable = True
        Set origin = swTriad.origin
        pt = origin.ArrayData
        Stop
        swManip.Remove
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
```

```
Implements PropertyManagerPage2Handler5
' Variable that provides access to the PropertyManager page
Dim m_PageObj As PropMgr
```

```
' This method is called to initialize the handler
Public Sub Init(pageObj As PropMgr)
    Set m_PageObj = pageObj
End Sub
```

```
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
```

```
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

```
'swDragManipHdlr
Option Explicit
Implements SwManipulatorHandler2
```

```
Private Sub Class_Initialize()
End Sub
Private Function SwManipulatorHandler2_OnDelete(ByVal pManipulator As Object) As Boolean
    Debug.Print "SwManipulatorHandler2_OnDelete"
End Function
Private Sub SwManipulatorHandler2_OnDirectionFlipped(ByVal pManipulator As Object)
    Debug.Assert False
    Debug.Print "SwManipulatorHandler2_OnDirectionFlipped"
End Sub
Private Function SwManipulatorHandler2_OnDoubleValueChanged(ByVal pManipulator As Object, ByVal Id As Long, Value As Double) As Boolean
    'Debug.Assert False
    Debug.Print "SwManipulatorHandler2_OnDoubleValueChanged"
    Debug.Print "  ID               = " & Id
    Debug.Print "  Value            = " & Value
End Function
Private Sub SwManipulatorHandler2_OnEndDrag(ByVal pManipulator As Object, ByVal handleIndex As Long)
    Debug.Print "SwManipulatorHandler2_OnEndDrag"
    Debug.Print "  HandleIndex      = " & handleIndex
    If (handleIndex = swDragArrowManipulatorOptions_e.swDragArrowManipulatorDirection1) Then
        Debug.Print " Forward"
    Else
        Debug.Print " Backward"
    End If
End Sub
Private Sub SwManipulatorHandler2_OnEndNoDrag(ByVal pManipulator As Object, ByVal handleIndex As Long)
    Debug.Print "SwManipulatorHandler2_OnEndNoDrag"
    Debug.Print "  HandleIndex      = " & handleIndex
End Sub
Private Function SwManipulatorHandler2_OnHandleLmbSelected(ByVal pManipulator As Object) As Boolean
End Function
Private Sub SwManipulatorHandler2_OnHandleRmbSelected(ByVal pManipulator As Object, ByVal handleIndex As Long)
    Debug.Print "SwManipulatorHandler2_OnHandleRmbSelected"
    Debug.Print "  handleIndex      = " & handleIndex
End Sub
Private Sub SwManipulatorHandler2_OnHandleSelected(ByVal pManipulator As Object, ByVal handleIndex As Long)
    Debug.Print "SwManipulatorHandler2_OnHandleSelected"
    Debug.Print "  HandleIndex      = " & handleIndex
End Sub
Private Sub SwManipulatorHandler2_OnItemSetFocus(ByVal pManipulator As Object, ByVal Id As Long)
    Debug.Assert False
    Debug.Print "SwManipulatorHandler2_OnItemSetFocus"
    Debug.Print "  ID               = " & Id
End Sub
Private Function SwManipulatorHandler2_OnStringValueChanged(ByVal pManipulator As Object, ByVal Id As Long, Value As String) As Boolean
    Debug.Assert False
    Debug.Print "SwManipulatorHandler2_OnStringValueChanged"
    Debug.Print "  ID               = " & Id
    Debug.Print "  Value            = " & Value
End Function
Private Sub SwManipulatorHandler2_OnUpdateDrag(ByVal pManipulator As Object, ByVal handleIndex As Long, ByVal newPosMathPt As Object)
    Debug.Print "SwManipulatorHandler2_OnUpdateDrag"
    Debug.Print "  HandleIndex      = " & handleIndex
End Sub
```

```
Back to top
```
