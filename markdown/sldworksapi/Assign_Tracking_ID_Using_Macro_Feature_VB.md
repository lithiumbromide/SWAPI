---
title: "Assign Tracking ID Using Macro Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Assign_Tracking_ID_Using_Macro_Feature_VB.htm"
---

# Assign Tracking ID Using Macro Feature Example (VBA)

This example shows how to assign a tracking ID to a face using a macro feature, which then allows the tracking ID to be persistent across SOLIDWORKS Design sessions.

```vb
'----------------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Click Tools > References > SolidWorks version exposed type libraries for
 '    add-in use > OK.
 ' 2. Copy Macros to the main module and rename it  Macros. (To rename the module, click
 '    View > Properties Window and type Macros in  (Name).)
 ' 3. Click Insert > Module and copy PropMgrConst to that module and name it PropMgrConst.
 ' 4. Click Insert > Class module and copy PropMgr to that class module and name it PropMgr.
 ' 5. Click Insert > Class module and copy  PropMgrCmd to that class module and name it PropMgrCmd.
 ' 6. Click Insert > Class module and copy  PropMgrHdlr to that class module and name it PropMgrHdlr.
 ' 7. Open a part.
 '
 ' Postconditions:
 ' 1. Select a face.
 ' 2. Assigns a tracking ID of 2 to the selected face via a macro feature.
 ' 3. Creates the macro feature CustomTrackingID1.
 ' 4. Examine the FeatureManager design tree.
 '------------------------------------------------------------------------------------
'Macros
Option Explicit
```

```
' Handle to Macro feature regeneration
Function swmMain(swAppIn, partIn, featureIn)
    Dim featData As MacroFeatureData
    Set featData = featureIn.GetDefinition
```

```
    Dim sels, types, selmarks
    Dim faceSel As Object
    Call featData.GetSelections(sels, types, selmarks)
    If IsEmpty(sels) Then
        swmMain = "Face was not been selected."
        Exit Function
    End If
```

```
    Set faceSel = sels(0)
    Dim TrackingID As Long
    Call featData.GetIntegerByName("TrackingID", TrackingID)
```

```
    If Not faceSel Is Nothing Then
        Dim Cookies As Long
	Cookies = swAppIn.RegisterTrackingDefinition("API_TrackingIDUsingMacroFeature")
        faceSel.setTrackingID Cookies, TrackingID
    End If
End Function
```

```
' Handle to Macro feature edit definition
Sub swmPM(swAppIn, partIn, featureIn)
    Dim swPage As New PropMgr
    swPage.Init swAppIn, partIn, featureIn, swCmdEdit, swAppIn.GetCurrentMacroPathName
    swPage.Show
End Sub
```

```
'Run this procedure to insert macro feature with customized Property Manager Page
Public Sub swmInsertCustomizedMacroFeature()
    Dim swAppIn, partIn, featureIn
    Set swAppIn = Application.SldWorks
    Set partIn = swAppIn.ActiveDoc
```

```
    Dim swPage As New PropMgr
    swPage.Init swAppIn, partIn, featureIn, swCmdCreate, swAppIn.GetCurrentMacroPathName
    swPage.Show

End Sub
```

```vb
 Back to top
```

'PropMgrConst

```
Public Enum swPageCmdState
    swCmdCreate = 1
    swCmdEdit = 2
End Enum
```

```
Public Const ID_GROUP = 1
Public Const ID_SELECTION = 2
Public Const ID_NUMBER = 3
```

```vb
 Back to top
```

'PropMgr

```
Option Explicit

Private m_swApp As SldWorks.SldWorks
Private m_Part As SldWorks.ModelDoc2
Private m_feature As SldWorks.feature
Private m_Page As PropertyManagerPage2
Private m_Group As PropertyManagerPageGroup
Private m_Selection As PropertyManagerPageSelectionbox
Private m_Number As PropertyManagerPageNumberbox
Private m_swPageCmd As New PropMgrCmd
Private m_cmdState As swPageCmdState
Private m_pageHdlr As New PropMgrHdlr
```

```
Private Sub Layout()
    Dim swPage As PropertyManagerPage2
    Dim swControl As PropertyManagerPageControl
    Dim title As String
    Dim buttonTypes As Long
    Dim message As String
    Dim ID As Long
    Dim controlType As Integer
    Dim caption As String
    Dim alignment As Integer
    Dim options As Long
    Dim tip As String
    Dim filterArray(0 To 0) As Long
```

```
    m_pageHdlr.Init Me
```

```
    If m_cmdState = swCmdCreate Then
        title = "Cutomized Macro"
    Else
        title = m_feature.Name
    End If
    buttonTypes = swPropertyManagerOptions_OkayButton + swPropertyManagerOptions_CancelButton + swPropertyManagerOptions_LockedPage
    Dim errorh As Long
    Set m_Page = m_swApp.CreatePropertyManagerPage(title, buttonTypes, m_pageHdlr, errorh)
    If Not m_Page Is Nothing Then
```

```
        'Initial set up of the dialog.
        message = "Customized Macro Feature."
        m_Page.SetMessage message, swImportantMessageBox
```

```
        'Begin adding the required controls to the dialog.
```

```
        'GROUP BOX ------------------------------------------------------------------
        ID = ID_GROUP
        caption = "Face Tracking ID"
        options = swGroupBoxOptions_Visible + swGroupBoxOptions_Expanded '+ swGroupBoxOptions_Checked
        Set m_Group = m_Page.AddGroupBox(ID, caption, options)
        If Not m_Group Is Nothing Then
```

```
            'CONTROL Selection box  ------------------------------------------------------------------
            ID = ID_SELECTION
            controlType = swControlType_Selectionbox
            caption = "Sample selection box"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "Select face"
            Set swControl = m_Group.AddControl(ID, controlType, caption, alignment, options, tip)
            If Not swControl Is Nothing Then
                Set m_Selection = swControl
                filterArray(0) = swSelFACES
                m_Selection.SingleEntityOnly = True
                m_Selection.Height = 50
                m_Selection.SetSelectionFilters (filterArray)
                m_Selection.SetStandardPictureLabel swBitmapLabel_SelectFaceSurface
            End If
```

```
            'CONTROL Number box  ------------------------------------------------------------------
            ID = ID_NUMBER
            controlType = swControlType_Numberbox
            caption = "Sample number box"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "Face Tracking ID"
            Set swControl = m_Group.AddControl(ID, controlType, caption, alignment, options, tip)
            If Not swControl Is Nothing Then
                Set m_Number = swControl
                m_Number.SetRange swNumberBox_UnitlessInteger, 1#, 1000000#, 1, True
```

```
                m_Number.Value = m_swPageCmd.getUserTrackingID()
                'm_Number.SetStandardPictureLabel
            End If
        End If
    End If
End Sub
```

```
Public Sub Show()
    m_Page.Show
End Sub
```

```
Sub Init(swApp, part, feature, cmdState As swPageCmdState, macroPath As String)
    Set m_swApp = swApp
    Set m_Part = part
    If Not IsEmpty(feature) Then
        Set m_feature = feature
    End If
    m_cmdState = cmdState
    m_Part.ClearSelection
    m_swPageCmd.Init swApp, part, feature, cmdState, macroPath
    Layout
End Sub
```

```
Public Function GetCmd() As PropMgrCmd
    Set GetCmd = m_swPageCmd
End Function
```

[Back to top](#Top)

'PropMgrCmd

```
Option Explicit

Private m_swApp As SldWorks.SldWorks
Private m_Part As SldWorks.ModelDoc2
Private m_feature As SldWorks.feature
Private m_faceSel As Object
Private m_TrackingID As Long
Private m_featData As SldWorks.MacroFeatureData
Private m_modelComp As SldWorks.Component2
Private m_cmdState As swPageCmdState
Private m_macroPath As String
```

```
Public Sub Init(swApp, part, feature, cmdState As swPageCmdState, macroPath As String)
    Set m_swApp = swApp
    Set m_Part = part
    m_macroPath = macroPath
    If Not IsEmpty(feature) Then
        Set m_feature = feature
    End If
    If cmdState = swCmdEdit Then ' On Edit Definition
        Dim ret As Boolean
        Set m_featData = m_feature.GetDefinition
        Set m_modelComp = m_feature.GetComponent
        m_cmdState = cmdState
        ret = m_featData.AccessSelections(m_Part, m_modelComp)
        Dim sels, types, selmarks
        Call m_featData.GetSelections(sels, types, selmarks)
        If Not IsEmpty(sels) Then
            Set m_faceSel = sels(0)
            Call m_faceSel.Select2(True, selmarks(0))
        End If
        Call m_featData.GetIntegerByName("TrackingID", m_TrackingID)
    Else ' On Insert Feature
        m_TrackingID = 2
    End If
End Sub
```

```
Public Sub OnOk()
```

```
    If m_cmdState = swCmdEdit Then ' On Edit Definition
        Dim sels, types, selmarks
        Call m_featData.GetSelections(sels, types, selmarks)
        Dim newSels(0 To 0) As Object
        Dim newSelMarks(0 To 0) As Long
        Set newSels(0) = m_faceSel
        newSelMarks(0) = 0
        sels = newSels
        selmarks = newSelMarks
        Call m_featData.SetSelections(sels, selmarks)
        Call m_featData.SetIntegerByName("TrackingID", m_TrackingID)
        Call m_feature.ModifyDefinition(m_featData, m_Part, m_modelComp)
    Else ' On Insert feature
        Dim paramNames, paramTypes, paramValues
        Dim paramNameArray(0 To 0) As String
        Dim paramTypeArray(0 To 0) As Long
        Dim paramValueArray(0 To 0) As String
        paramNameArray(0) = "TrackingID"
        paramTypeArray(0) = swMacroFeatureParamTypeInteger
        paramValueArray(0) = Str(m_TrackingID)
        paramNames = paramNameArray
        paramTypes = paramTypeArray
        paramValues = paramValueArray
                Dim methods(0 To 8) As String
        methods(0) = m_macroPath
        methods(1) = "Macros"
        methods(2) = "swmMain"
        methods(3) = m_macroPath
        methods(4) = "Macros"
        methods(5) = "swmPM"
        methods(6) = ""
        methods(7) = ""
        methods(8) = ""
        Dim feat As Object
        Set feat = m_Part.FeatureManager.InsertMacroFeature("CustumTrackingID", "", methods, (paramNames), (paramTypes), (paramValues), Nothing, swMacroFeatureByDefault)
    End If
End Sub
```

```
Public Sub OnCancel()
    If m_cmdState = swCmdEdit Then
        m_featData.ReleaseSelectionAccess
    End If
End Sub
```

```
Public Sub OnFaceSelect()
    Dim selM
    Set selM = m_Part.SelectionManager
    Set m_faceSel = Nothing
    Set m_faceSel = selM.GetSelectedObject3(1)
End Sub
```

```
Public Function getUserTrackingID() As Integer
    getUserTrackingID = m_TrackingID
End Function
```

```
Public Sub setUserTrackingID(TrackingID As Integer)
    m_TrackingID = TrackingID
End Sub
```

[Back to top](#Top)

'PropMgrHdlr

```
Option Explicit
Implements PropertyManagerPage2Handler
```

```
Dim m_pageObj As PropMgr
```

```
Public Sub Init(pageObj As PropMgr)
    Set m_pageObj = pageObj
End Sub
```

```
Private Function PropertyManagerPage2Handler_ConnectToSW(ByVal ThisSW As Object, ByVal Cookie As Long) As Boolean
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler_OnButtonPress(ByVal ID As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler_OnClose(ByVal reason As Long)
    If reason = swPropertyManagerPageClose_Okay Then
        m_pageObj.GetCmd().OnOk
    ElseIf reason = swPropertyManagerPageClose_Cancel Then
        m_pageObj.GetCmd().OnCancel
    End If
End Sub
```

```
Private Sub PropertyManagerPage2Handler_OnCheckboxCheck(ByVal ID As Long, ByVal Checked As Boolean)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler_OnComboboxSelectionChanged(ByVal ID As Long, ByVal Item As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler_OnGroupCheck(ByVal ID As Long, ByVal Checked As Boolean)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler_OnGroupExpand(ByVal ID As Long, ByVal Expanded As Boolean)
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler_OnHelp() As Boolean
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler_OnListboxSelectionChanged(ByVal ID As Long, ByVal Item As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler_AfterClose()
    Set m_pageObj = Nothing
End Sub
```

```
Private Sub PropertyManagerPage2Handler_OnNumberboxChanged(ByVal ID As Long, ByVal Value As Double)
    m_pageObj.GetCmd().setUserTrackingID (Value)
End Sub
```

```
Private Sub PropertyManagerPage2Handler_OnOptionCheck(ByVal ID As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler_OnSelectionboxFocusChanged(ByVal ID As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler_OnTextboxChanged(ByVal ID As Long, ByVal Text As String)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler_OnSelectionBoxListChanged(ByVal ID As Long, ByVal Text As Long)
    m_pageObj.GetCmd().OnFaceSelect
End Sub
```

[Back to top](#Top)
