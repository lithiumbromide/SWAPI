---
title: "Create PropertyManager Page Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swpublishedapi/Create_PropertyManager_Page_Example_VB.htm"
---

# Create PropertyManager Page Example (VBA)

This example shows how to create a PropertyManager page that contains the following controls:

- ActiveX
- Bitmap
- Bitmap button
- Button
- Combo box
- Group box
- Label
- List box
- Number box
- Radio button
- Selection box
- Slider
- Tab

This example also shows how to handle focus events for these controls.

NOTE: If the model is an assembly that contains multiple components, and you want to allow the user to select edges, faces, or vertices, then you must specify swSelCOMPSDONTOVERRIDE for parameter SelType of IPropertyManagerPageSelectionbox::SetSelectionFilters. Otherwise, if the user attempts to select an edge, face, or vertex, then the entire component might get selected and not the edge, face, or vertex. This example demonstrates how to specify SelType.

```vb
'--------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Copy Modules - main to your project.
 ' 2. Copy Class Modules - clsPropMgr to a class module in your project.
 ' 3. Click   Tools > References, select
 '    SOLIDWORKS version exposed type libraries for add-in use, and click OK.
 ' 4. Ensure that the specified assembly document exists.
 ' 5. Modify ClassID and LicenseKey parameters in
 '    IPropertyManagerPageActiveX::SetClass to add your ActiveX control
 '    to the PropertyManager page.
 ' 6. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a PropertyManager page called Comps.
 ' 2. Creates the specified controls.
 ' 3. Inspect the contents of Comps and the Immediate Window as
 '    you use the specified controls.
 ' 4. Click the green check mark to close the PropertyManager page.
 '
 ' NOTE: Because the assembly document is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
 'Modules - main
Option Explicit

Public swApp As SldWorks.SldWorks
Public Part As SldWorks.ModelDoc2
Public pm As clsPropMgr

Sub main()
```

```vb
Dim openDocErrors As Long
Dim OpenDocWarnings As Long

Set swApp = Application.SldWorks
Set Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\bladed shaft.sldasm", swDocASSEMBLY, swOpenDocOptions_Silent, "", openDocErrors, OpenDocWarnings)
```

```vb
'Create a new instance of the PropertyManager class
Set pm = New clsPropMgr
pm.Show
```

```vb
End Sub
```

[Back to top](#Top)

```vb
'Class Modules - clsPropMgr
Option Explicit
' Handler for PropertyManager page controls
 Implements PropertyManagerPage2Handler9

' Control objects required for the PropertyManager page
 Dim pm_Page As PropertyManagerPage2
 Dim pm_Group As PropertyManagerPageGroup
 Dim pm_Selection As PropertyManagerPageSelectionbox
 Dim pm_Selection2 As PropertyManagerPageSelectionbox
 Dim pm_Label As PropertyManagerPageLabel
 Dim pm_Combo As PropertyManagerPageCombobox
 Dim pm_List As PropertyManagerPageListbox
 Dim pm_Number As PropertyManagerPageNumberbox
 Dim pm_Radio As PropertyManagerPageOption
 Dim pm_Slider As PropertyManagerPageSlider
 Dim pm_Tab As PropertyManagerPageTab
 Dim pm_Button As PropertyManagerPageButton
 Dim pm_BMPButton As PropertyManagerPageBitmapButton
 Dim pm_Bitmap As PropertyManagerPageBitmap
 Dim pm_ActiveX As PropertyManagerPageActiveX
 Dim ClickedCancel As Boolean
 Dim retVal As Long

' Each control in the page needs a unique ID
 Const GroupID As Long = 1
 Const LabelID As Long = 2
 Const SelectionID As Long = 3
 Const ComboID As Long = 4
 Const ListID As Long = 5
 Const Selection2ID As Long = 6
 Const NumberID As Long = 7
 Const RadioID As Long = 8
 Const SliderID As Long = 9
 Const TabID As Long = 10
 Const ButtonID As Long = 11
 Const BMPButtonID As Long = 12
 Const BitmapID As Long = 13
 Const ActiveXID As Long = 14
Sub Show()
    pm_Page.Show2 0
End Sub

' The following runs when a new instance of the class is created
Private Sub Class_Initialize()

    Dim PageTitle As String
     Dim caption As String
     Dim tip As String
     Dim options As Long
     Dim longerrors As Long
     Dim controlType As Long
     Dim alignment As Long
     Dim listItems(3) As String

     ' Set the variables for the page
     PageTitle = "Comps"

    options = swPropertyManager_OkayButton _
         + swPropertyManager_CancelButton _
         + swPropertyManagerOptions_LockedPage _
         + swPropertyManagerOptions_PushpinButton

     ' Create the PropertyManager page
     Set pm_Page = swApp.CreatePropertyManagerPage(PageTitle, _
         options, Me, longerrors)

     ' Make sure that the page was created properly
     If longerrors = swPropertyManagerPage_Okay Then

        ' Add controls to the page

        ' Add a tab
        Set pm_Tab = pm_Page.AddTab(TabID, "Application", "", 0)

         ' Add a group box to the tab
        caption = "Controls"
        options = swGroupBoxOptions_Visible + _
             swGroupBoxOptions_Expanded
        Set pm_Group = pm_Tab.AddGroupBox(GroupID, caption, options)

         ' Add two selection boxes
        controlType = swControlType_Selectionbox
        caption = ""
        alignment = swControlAlign_Indent
        options = swControlOptions_Visible + _
               swControlOptions_Enabled
        tip = "Select an edge, face, vertex, solid body, or a component"
        Set pm_Selection = pm_Group.AddControl2(SelectionID, _
               controlType, caption, alignment, options, tip)

        Set pm_Selection2 = pm_Group.AddControl2(Selection2ID, _
               controlType, caption, alignment, options, tip)

        Dim filters(6) As Long
         filters(0) = swSelEDGES
         filters(1) = swSelREFEDGES
         filters(2) = swSelFACES
         filters(3) = swSelVERTICES
         filters(4) = swSelSOLIDBODIES
         filters(5) = swSelCOMPONENTS
         filters(6) = swSelCOMPSDONTOVERRIDE

        pm_Selection.SingleEntityOnly = False
         pm_Selection.AllowMultipleSelectOfSameEntity = True
         pm_Selection.Height = 50
         pm_Selection.SetSelectionFilters filters
         pm_Selection2.SingleEntityOnly = False
         pm_Selection2.AllowMultipleSelectOfSameEntity = True
         pm_Selection2.Height = 50
         pm_Selection2.SetSelectionFilters filters

         ' Add a combo box
        controlType = swControlType_Combobox
        caption = ""
        alignment = swControlAlign_Indent
        options = swControlOptions_Visible + _
               swControlOptions_Enabled
        tip = "Select a value"

        Set pm_Combo = pm_Group.AddControl2(ComboID, _
               controlType, caption, alignment, options, tip)

        If Not pm_Combo Is Nothing Then

            pm_Combo.Height = 50

            listItems(0) = "Value 1"
             listItems(1) = "Value 2"
             listItems(2) = "Value 3"
             listItems(3) = "Value 4"

            pm_Combo.AddItems (listItems)
             pm_Combo.CurrentSelection = 0

        End If

         ' Add a list box
        controlType = swControlType_Listbox
        caption = ""
        alignment = swControlAlign_Indent
        options = swControlOptions_Visible + _
               swControlOptions_Enabled
        tip = "Multi-select values in the list box"

        Set pm_List = pm_Group.AddControl2(ListID, _
               controlType, caption, alignment, options, tip)
         pm_List.Style = swPropMgrPageListBoxStyle_MultipleItemSelect
         pm_List.Height = 50

         If Not pm_List Is Nothing Then

            pm_List.Height = 50
             listItems(0) = "Value 1"
             listItems(1) = "Value 2"
             listItems(2) = "Value 3"
             listItems(3) = "Value 4"
             pm_List.AddItems (listItems)
             pm_List.SetSelectedItem 1, True

        End If

        ' Add a label
         Set pm_Label = pm_Group.AddControl2(LabelID, swControlType_Label, "Label", swControlAlign_LeftEdge, options, "")

        ' Add a slider
         Set pm_Slider = pm_Group.AddControl2(SliderID, swControlType_Slider, "Slider", swControlAlign_LeftEdge, options, "Slide")

        ' Add a radio button
         Set pm_Radio = pm_Group.AddControl2(RadioID, swControlType_Option, "Radio button", swControlAlign_LeftEdge, options, "Select")

        ' Add a number box
         Set pm_Number = pm_Group.AddControl2(NumberID, swControlType_Numberbox, "Number box", swControlAlign_LeftEdge, options, "Spin")

        ' Add a button
         Set pm_Button = pm_Group.AddControl2(ButtonID, swControlType_Button, "Button", swControlAlign_LeftEdge, options, "Click")

        ' Add a bitmap button
         Set pm_BMPButton = pm_Group.AddControl2(BMPButtonID, swControlType_BitmapButton, "Bitmap button", swControlAlign_LeftEdge, options, "Click")
         pm_BMPButton.SetStandardBitmaps (swPropertyManagerPageBitmapButtons_e.swBitmapButtonImage_parallel)

        ' Add a bitmap
         Set pm_Bitmap = pm_Group.AddControl2(BitmapID, swControlType_Bitmap, "Bitmap", swControlAlign_LeftEdge, options, "Bitmap")
         pm_Bitmap.SetStandardBitmap (swBitmapControlStandardTypes_e.swBitmapControl_Volume)

        ' Add an ActiveX control
         Set pm_ActiveX = pm_Group.AddControl2(ActiveXID, swControlType_ActiveX, "ActiveX", swControlAlign_LeftEdge, options, "ActiveX control tip")
         pm_ActiveX.SetClass "ClassID", "LicenseKey"

    Else

        MsgBox "An error occurred while attempting to create the PropertyManager Page", vbCritical

    End If

End Sub

Private Sub PropertyManagerPage2Handler9_AfterActivation()
End Sub

Private Sub PropertyManagerPage2Handler9_AfterClose()
    ' Destroy the class
     Set pm = Nothing
End Sub

Private Function PropertyManagerPage2Handler9_OnActiveXControlCreated(ByVal Id As Long, ByVal Status As Boolean) As Long
     Debug.Print "ActiveX control created"
 End Function

Private Sub PropertyManagerPage2Handler9_OnButtonPress(ByVal Id As Long)
     Debug.Print "Button clicked"
 End Sub

Private Sub PropertyManagerPage2Handler9_OnCheckboxCheck(ByVal Id As Long, ByVal Checked As Boolean)
End Sub

Private Sub PropertyManagerPage2Handler9_OnClose(ByVal Reason As Long)
    If Reason = swPropertyManagerPageClose_Cancel Then
        ' Cancel button clicked
         ClickedCancel = True
    ElseIf Reason = swPropertyManagerPageClose_Okay Then
        ' OK button clicked
         ClickedCancel = False
    End If
End Sub

Private Sub PropertyManagerPage2Handler9_OnComboboxEditChanged(ByVal Id As Long, ByVal Text As String)
End Sub

Private Sub PropertyManagerPage2Handler9_OnComboboxSelectionChanged(ByVal Id As Long, ByVal Item As Long)
End Sub

Private Sub PropertyManagerPage2Handler9_OnGroupCheck(ByVal Id As Long, ByVal Checked As Boolean)
End Sub

Private Sub PropertyManagerPage2Handler9_OnGroupExpand(ByVal Id As Long, ByVal Expanded As Boolean)
End Sub

 Private Function PropertyManagerPage2Handler9_OnHelp() As Boolean
End Function

Private Function PropertyManagerPage2Handler9_OnKeystroke(ByVal Wparam As Long, ByVal Message As Long, ByVal Lparam As Long, ByVal Id As Long) As Boolean
End Function

Private Sub PropertyManagerPage2Handler9_OnListboxSelectionChanged(ByVal Id As Long, ByVal Item As Long)

End Sub

Private Function PropertyManagerPage2Handler9_OnNextPage() As Boolean
End Function

Private Sub PropertyManagerPage2Handler9_OnNumberboxChanged(ByVal Id As Long, ByVal Value As Double)
     Debug.Print "Number box changed"
 End Sub

Private Sub PropertyManagerPage2Handler9_OnOptionCheck(ByVal Id As Long)
     Debug.Print "Option selected"
 End Sub

Private Sub PropertyManagerPage2Handler9_OnPopupMenuItem(ByVal Id As Long)
End Sub

Private Sub PropertyManagerPage2Handler9_OnPopupMenuItemUpdate(ByVal Id As Long, retVal As Long)
End Sub

Private Function PropertyManagerPage2Handler9_OnPreview() As Boolean
End Function

Private Function PropertyManagerPage2Handler9_OnPreviousPage() As Boolean
End Function

Private Sub PropertyManagerPage2Handler9_OnRedo()
End Sub

Private Sub PropertyManagerPage2Handler9_OnSelectionboxCalloutCreated(ByVal Id As Long)
End Sub

Private Sub PropertyManagerPage2Handler9_OnSelectionboxCalloutDestroyed(ByVal Id As Long)
End Sub

Private Sub PropertyManagerPage2Handler9_OnSelectionboxFocusChanged(ByVal Id As Long)
    Debug.Print "The focus moved to selection box " & Id
End Sub

Private Sub PropertyManagerPage2Handler9_OnSelectionboxListChanged(ByVal Id As Long, ByVal Count As Long)
     pm_Page.SetCursor (swPropertyManagerPageCursors_Advance)
    Debug.Print "The list in selection box " & Id & " changed"
End Sub

Private Sub PropertyManagerPage2Handler9_OnSliderPositionChanged(ByVal Id As Long, ByVal Value As Double)
     Debug.Print "Slider position changed"
 End Sub

Private Sub PropertyManagerPage2Handler9_OnSliderTrackingCompleted(ByVal Id As Long, ByVal Value As Double)
End Sub

Private Function PropertyManagerPage2Handler9_OnSubmitSelection(ByVal Id As Long, ByVal Selection As Object, ByVal SelType As Long, ItemText As String) As Boolean
    PropertyManagerPage2Handler9_OnSubmitSelection = True
End Function

Private Function PropertyManagerPage2Handler9_OnTabClicked(ByVal Id As Long) As Boolean
End Function

Private Sub PropertyManagerPage2Handler9_OnTextboxChanged(ByVal Id As Long, ByVal Text As String)
End Sub

Private Sub PropertyManagerPage2Handler9_OnUndo()
End Sub

Private Sub PropertyManagerPage2Handler9_OnWhatsNew()
End Sub

Private Sub PropertyManagerPage2Handler9_OnLostFocus(ByVal Id As Long)
    Debug.Print "Control box " & Id & " lost focus"
End Sub

Private Sub PropertyManagerPage2Handler9_OnGainedFocus(ByVal Id As Long)
   Dim varArray As Variant
   Debug.Print "Control box " & Id & " gained focus"
   varArray = pm_List.GetSelectedItems
   pm_Combo.CurrentSelection = varArray(0)
End Sub

Public Sub PropertyManagerPage2Handler9_OnListBoxRMBUp(ByVal Id As Long, ByVal posX As Long, ByVal posY As Long)
End Sub

Public Function PropertyManagerPage2Handler9_OnWindowFromHandleControlCreated(ByVal Id As Long, ByVal Status As Boolean) As Long
End Function

Public Sub PropertyManagerPage2Handler9_OnNumberboxTrackingCompleted(ByVal Id As Long, ByVal Value As Double)
End Sub
```

[Back to top](#Top)
