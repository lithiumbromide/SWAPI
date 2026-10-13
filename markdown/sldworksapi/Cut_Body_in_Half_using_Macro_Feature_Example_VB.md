---
title: "Cut Body in Half using Macro Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm"
---

# Cut Body in Half using Macro Feature Example (VBA)

This example shows how to cut a body in a part document in half using a macro feature.

```
'-----------------------------------------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro.
' 2. Click Tools > References > SolidWorks version exposed type libraries for
'    add-in use > OK.
' 3. Copy Macros to the main module and rename it Macros. (To rename the module, click
'    View > Properties Window and type Macros in (Name).)
' 4. Click Insert > Module and copy PropMgrConst to that module and name it PropMgrConst.
' 5. Click Insert > Class module and copy PropMgr to that class module and name it PropMgr.
' 6. Click Insert > Class module and copy PropMgrCmd to that class module and name it PropMgrCmd.
' 7. Click Insert > Class module and copy PropMgrHdlr to that class module and name it PropMgrHdlr.
' 8. Open public_documents\samples\tutorial\api\plate.sldprt.
```

```
' Postconditions:
' 1. Click the part in the graphics area, which is then displayed in Surface on Mass Center in the
'    PropertyManager page.
' 2. Click the green check mark in the PropertyManager page to insert the macro feature.
' 3. Cuts the body in half and adds the AngleSurf1 macro feature to the FeatureManager design tree.
' 4. Right-click AngleSurf1 and select Edit Feature on the context-sensitive menu.
' 5. Change 1 to 2 in Select the body to keep in the AngleSurf1 PropertyManager page.
' 6. Click the green check mark in the PropertyManager page.
' 7. Displays the opposite side of the body in the graphics area.
' 8. Examine the graphics area and FeatureManager design tree.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'------------------------------------------------------------------------------------------------
'Macros
```

```
Option Explicit
```

```
' Macro feature rebuild function
Function swmMain(swAppIn, partIn, featureIn)
    Dim featData As SldWorks.MacroFeatureData
    Dim Config As SldWorks.Configuration
    Dim ConfigName As String
```

```
    Set featData = featureIn.GetDefinition
```

```
    ' Get name of configuration being rebuilt
    Set Config = featData.CurrentConfiguration
    ConfigName = Config.Name
```

```
    Dim sels, types, selmarks
    Dim body1 As SldWorks.Body2
    Call featData.GetSelections3(sels, types, selmarks, Nothing, Nothing)
    If IsEmpty(sels) Then
       swmMain = "Body has not been selected!"
       Exit Function
    End If
```

```
    If sels(0) Is Nothing Then
       swmMain = "Body has not been selected!"
       Exit Function
    End If
```

```
    Set body1 = sels(0)
```

```
    Dim modeler As SldWorks.modeler
    Set modeler = swAppIn.GetModeler
    Dim props As Variant
    props = body1.GetMassProperties(1)
    Dim p1(0 To 2) As Double
    Dim v1(0 To 2) As Double
    Dim v2(0 To 2) As Double
    p1(0) = props(0)
    p1(1) = props(1)
    p1(2) = props(2)
    v1(0) = 0
    v1(1) = 0
    v1(2) = 1
    v2(0) = 1
    v2(1) = 0
    v2(1) = 0
```

```
    Dim surf As SldWorks.Surface
    Set surf = modeler.CreatePlanarSurface2(p1, v1, v2)
    Dim box As Variant
    box = body1.GetBodyBox
```

```
    Dim uvLow, uvHigh As Variant
    uvLow = surf.GetClosestPointOn(box(0), box(1), box(2))
    uvHigh = surf.GetClosestPointOn(box(3), box(4), box(5))
```

```
    Dim midPt(0 To 2) As Double
    Dim i As Integer
    For i = 0 To 2
        midPt(i) = (uvLow(i) + uvHigh(i)) / 2
    Next i
```

```
    For i = 0 To 2
        uvLow(i) = (uvLow(i) - midPt(i)) * 1.1 + midPt(i)
        uvHigh(i) = (uvHigh(i) - midPt(i)) * 1.1 + midPt(i)
    Next i
```

```
    uvLow = surf.GetClosestPointOn(uvLow(0), uvLow(1), uvLow(2))
    uvHigh = surf.GetClosestPointOn(uvHigh(0), uvHigh(1), uvHigh(2))
```

```
    Dim sheet As SldWorks.Body2
    Dim uv(0 To 3) As Double
    uv(0) = uvLow(3)
    uv(1) = uvHigh(3)
    uv(2) = uvLow(4)
    uv(3) = uvHigh(4)
    Set sheet = modeler.CreateSheetFromSurface(surf, uv)
```

```
    ' Transform with angle
    Dim mathUtil As SldWorks.MathUtility
    Set mathUtil = swAppIn.GetMathUtility
    Dim aXform As SldWorks.MathTransform
    Dim basePt As SldWorks.MathPoint
    Dim RetVal As Boolean
    Set basePt = mathUtil.CreatePoint(midPt)
    Dim xAxis As MathVector
    Set xAxis = mathUtil.CreateVector(v2)
    Set aXform = mathUtil.CreateTransformRotateAxis(basePt, xAxis, 3.1416159 / 2)
    RetVal = sheet.ApplyTransform(aXform)
```

```
    ' Assign edge ID
    Dim edges As Variant
    Dim faces As Variant
    featData.GetEntitiesNeedUserId sheet, faces, edges
    edges = sheet.GetEdges
    For i = 0 To UBound(edges)
        featData.SetEdgeUserId edges(i), i, 0
        Dim id1 As Long
        Dim id2 As Long
        featData.GetEdgeUserId edges(i), id1, id2
    Next i
```

```
    Dim editBodies As Variant
    Dim editBdy As Body2
    Dim resBody As Body2
    editBodies = featData.editBodies
    Set editBdy = editBodies(0)
```

```
    Dim result As Variant
    Dim err As Long
    result = editBdy.Operations2(SWBODYCUT, sheet, err)
    Dim wb As Long
    featData.GetIntegerByName "WhichBody", wb
    Set resBody = result(wb - 1)
```

```
    Set swmMain = resBody
    resBody.Hide partIn
```

```
End Function
```

```
' Macro feature edit definition function
Sub swmPM(swAppIn, partIn, featureIn)
    Dim swPage As New PropMgr
    swPage.Init swAppIn, partIn, featureIn, swCmdEdit, swAppIn.GetCurrentMacroPathName
    swPage.Show
End Sub
```

```
'Inserts macro feature with customized PropertyManager page
Public Sub swmInsertCustomizedMacroFeature()
    Dim swAppIn, partIn, featureIn
    Set swAppIn = Application.SldWorks
    Set partIn = swAppIn.ActiveDoc
```

```
    If partIn.GetType() <> swDocPART Then
        MsgBox ("Available only from part document!")
        Exit Sub
    End If
```

```
    Dim swPage As New PropMgr
    swPage.Init swAppIn, partIn, featureIn, swCmdCreate, swAppIn.GetCurrentMacroPathName
    swPage.Show
```

```
End Sub
```

[Back to top](#Top)

#### 'PropMgrConst

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

[Back to top](#Top)

#### 'PropMgr

```
Option Explicit
```

```
Private m_swApp As SldWorks.SldWorks
Private m_Part As SldWorks.ModelDoc2
Private m_feature As SldWorks.feature
Private m_Page As PropertyManagerPage2
Private m_Group As PropertyManagerPageGroup
Private m_Selection As PropertyManagerPageSelectionbox
Private m_NumberBox As PropertyManagerPageNumberbox
Private m_Text As PropertyManagerPageTextbox
Private m_swPageCmd As New PropMgrCmd
Private m_cmdState As swPageCmdState
Private m_pageHdlr As New PropMgrHdlr
```

```
Private Sub Layout()
```

```
    Dim swControl As PropertyManagerPageControl
    Dim title As String
    Dim buttonTypes As Long
    Dim Message As String
    Dim Id As Long
    Dim controlType As Integer
    Dim caption As String
    Dim alignment As Integer
    Dim options As Long
    Dim tip As String
    Dim filterArray(0 To 1) As Long
```

```
    m_pageHdlr.Init Me
```

```
    If m_cmdState = swCmdCreate Then
        title = "Cut body macro feature"
    Else
        title = m_feature.Name
    End If
```

```
    buttonTypes = swPropertyManagerOptions_OkayButton + swPropertyManagerOptions_CancelButton + swPropertyManagerOptions_LockedPage
    Dim errorh As Long
    Set m_Page = m_swApp.CreatePropertyManagerPage(title, buttonTypes, m_pageHdlr, errorh)
    If Not m_Page Is Nothing Then
```

```
        'Initial set up of the message in the PropertyManager page
        Message = "Select body to cut, then select the side of the body to keep."
        m_Page.SetMessage Message, swImportantMessageBox
```

```
        'Begin adding the required controls to the PropertyManager
```

```
        'Group box
        Id = ID_GROUP
        caption = "Surface on Mass Center"
        options = swGroupBoxOptions_Visible + swGroupBoxOptions_Expanded '+ swGroupBoxOptions_Checked
        Set m_Group = m_Page.AddGroupBox(Id, caption, options)
        If Not m_Group Is Nothing Then
            'Selection box
            Id = ID_SELECTION
            controlType = swControlType_Selectionbox
            caption = "Selection box"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "Select body"
            Set swControl = m_Group.AddControl2(Id, controlType, caption, alignment, options, tip)
            If Not swControl Is Nothing Then
                Set m_Selection = swControl
                filterArray(0) = swSelSOLIDBODIES
                filterArray(1) = swSelSURFACEBODIES
                m_Selection.SingleEntityOnly = True
                m_Selection.Height = 50
                m_Selection.SingleEntityOnly = True
                m_Selection.SetSelectionFilters (filterArray)
                m_Selection.SetStandardPictureLabel swBitmapLabel_SelectFaceSurface
            End If
```

```
            'Selection box
            Id = ID_SELECTION
            controlType = swControlType_Numberbox
            caption = "Number box"
            alignment = swControlAlign_Indent
            options = swControlOptions_Visible + swControlOptions_Enabled
            tip = "Select the body to keep"
            Set swControl = m_Group.AddControl2(Id, controlType, caption, alignment, options, tip)
```

```
            If Not swControl Is Nothing Then
                Set m_NumberBox = swControl
                m_NumberBox.SetRange swNumberBox_UnitlessInteger, 1, 2, 1, True
                m_NumberBox.Value = GetCmd().GetNumberValue()
            End If
```

```
        End If
```

```
    End If
```

```
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
```

```
    If Not IsEmpty(feature) Then
        Set m_feature = feature
    End If
```

```
    m_cmdState = cmdState
    m_Part.ClearSelection2 True
    m_swPageCmd.Init swApp, part, feature, cmdState, macroPath
    Layout
```

```
End Sub
```

```
Public Function GetCmd() As PropMgrCmd
    Set GetCmd = m_swPageCmd
End Function
```

[Back to top](#Top)

#### 'PropMgrCmd

```
Option Explicit
```

```
Private m_swApp As SldWorks.SldWorks
Private m_Part As SldWorks.ModelDoc2
Private m_feature As SldWorks.feature
Private m_bodySel As Object
Private m_whichBody As Long
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
    m_whichBody = 1
```

```
    If Not IsEmpty(feature) Then
        Set m_feature = feature
    End If
```

```
    If cmdState = swCmdEdit Then ' On Edit Definition
```

```
        Dim ret As Boolean
        Set m_featData = m_feature.GetDefinition
        Set m_modelComp = m_feature.GetComponent
        m_cmdState = cmdState
        ret = m_featData.AccessSelections(m_Part, m_modelComp)
        Dim sels, types, selmarks
```

```
        Call m_featData.GetSelections3(sels, types, selmarks, Nothing, Nothing)
```

```
        If Not IsEmpty(sels) And Not sels(0) Is Nothing Then
            Set m_bodySel = sels(0)
            Call m_bodySel.Select(True, selmarks(0))
        End If
```

```
        m_featData.GetIntegerByName "WhichBody", m_whichBody
```

```
    End If
```

```
End Sub
```

```
Public Sub OnOk()
```

```
    If m_cmdState = swCmdEdit Then ' On Edit Definition
```

```
        Dim sels, types, selmarks
```

```
        Call m_featData.GetSelections3(sels, types, selmarks, Nothing, Nothing)
```

```
        Dim newSels(0 To 0) As Body2
        Dim newSelMarks(0 To 0) As Long
```

```
        Set newSels(0) = m_bodySel
        newSelMarks(0) = 0
        sels = newSels
        selmarks = newSelMarks
```

```
        Dim DrViews(0 To 0) As View
        Set DrViews(0) = Nothing
```

```
        Call m_featData.SetSelections2(sels, selmarks, DrViews)
```

```
        m_featData.SetIntegerByName "WhichBody", m_whichBody
```

```
        Call m_feature.ModifyDefinition(m_featData, m_Part, m_modelComp)
```

```
    Else ' On Insert feature
```

```
        Dim paramNames, paramTypes, paramValues
        Dim pNames(0 To 0) As String
        Dim pTypes(0 To 0) As Long
        Dim pValues(0 To 0) As String
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
        pNames(0) = "WhichBody"
        pTypes(0) = swMacroFeatureParamTypeInteger
        pValues(0) = m_whichBody
        paramNames = pNames
        paramTypes = pTypes
        paramValues = pValues
        Dim selBodies(0 To 0) As Body2
        Set selBodies(0) = m_bodySel
        Set feat = m_Part.FeatureManager.InsertMacroFeature3("AngleSurf", "", methods, (paramNames), (paramTypes), (paramValues), Nothing, Nothing, selBodies, Nothing, swMacroFeatureByDefault)
```

```
    End If
```

```
End Sub
```

```
Public Sub OnCancel()
```

```
    If m_cmdState = swCmdEdit Then
```

```
        m_featData.ReleaseSelectionAccess
```

```
    End If
```

```
End Sub
```

```
Public Sub OnBodySelect()
```

```
    Dim selM
```

```
    Set selM = m_Part.SelectionManager
```

```
    Set m_bodySel = Nothing
```

```
    Set m_bodySel = selM.GetSelectedObject6(1, -1)
```

```
End Sub
```

```
Public Sub OnNumberChanged(Value As Long)
```

```
    m_whichBody = Value
```

```
End Sub
```

```
Public Function GetNumberValue()
```

```
    GetNumberValue = m_whichBody
```

```
End Function
```

[Back to top](#Top)

#### 'PropMgrHdlr

```
Option Explicit
```

```
Implements PropertyManagerPage2Handler8
```

```
Dim m_pageObj As PropMgr
```

```
Public Sub Init(pageObj As PropMgr)
```

```
    Set m_pageObj = pageObj
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_OnListboxRMBUp(ByVal Id As Long, ByVal PosX As Long, ByVal PosY As Long)
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler8_OnWindowFromHandleControlCreated(ByVal Id As Long, ByVal Status As Boolean) As Long
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler8_OnLostFocus(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_OnGainedFocus(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_OnPopupMenuItemUpdate(ByVal Id As Long, ByRef RetVal As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_OnPopupMenuItem(ByVal Id As Long)
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler8_OnKeystroke(ByVal Wparam As Long, ByVal Message As Long, ByVal Lparam As Long, ByVal Id As Long) As Boolean
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler8_OnSliderTrackingCompleted(ByVal Id As Long, ByVal Value As Double)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_OnSliderPositionChanged(ByVal Id As Long, ByVal Value As Double)
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler8_OnActiveXControlCreated(ByVal Id As Long, ByVal Status As Boolean) As Long
```

```
End Function
```

```
Private Function PropertyManagerPage2Handler8_OnSubmitSelection(ByVal Id As Long, ByVal Selection As Object, ByVal SelType As Long, ByRef ItemText As String) As Boolean
    PropertyManagerPage2Handler8_OnSubmitSelection = True
End Function
```

```
Private Sub PropertyManagerPage2Handler8_OnSelectionboxCalloutDestroyed(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_OnSelectionboxCalloutCreated(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_OnComboboxEditChanged(ByVal Id As Long, ByVal Text As String)
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler8_OnTabClicked(ByVal Id As Long) As Boolean
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler8_OnRedo()
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_OnUndo()
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_OnWhatsNew()
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler8_OnPreview() As Boolean
```

```
End Function
```

```
Private Function PropertyManagerPage2Handler8_OnNextPage() As Boolean
```

```
End Function
```

```
Private Function PropertyManagerPage2Handler8_OnPreviousPage() As Boolean
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler8_AfterActivation()
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler8_ConnectToSW(ByVal ThisSW As Object, ByVal Cookie As Long) As Boolean
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler8_OnButtonPress(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_OnClose(ByVal reason As Long)
```

```
    If reason = swPropertyManagerPageClose_Okay Then
```

```
        m_pageObj.GetCmd().OnOk
```

```
    ElseIf reason = swPropertyManagerPageClose_Cancel Then
```

```
        m_pageObj.GetCmd().OnCancel
```

```
    End If
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_OnCheckboxCheck(ByVal Id As Long, ByVal Checked As Boolean)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_OnComboboxSelectionChanged(ByVal Id As Long, ByVal Item As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_OnGroupCheck(ByVal Id As Long, ByVal Checked As Boolean)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_OnGroupExpand(ByVal Id As Long, ByVal Expanded As Boolean)
```

```
End Sub
```

```
Private Function PropertyManagerPage2Handler8_OnHelp() As Boolean
```

```
End Function
```

```
Private Sub PropertyManagerPage2Handler8_OnListboxSelectionChanged(ByVal Id As Long, ByVal Item As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_OnNumberboxChanged(ByVal Id As Long, ByVal Value As Double)
```

```
    m_pageObj.GetCmd().OnNumberChanged Int(Value)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_AfterClose()
```

```
    Set m_pageObj = Nothing
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_OnOptionCheck(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_OnSelectionboxFocusChanged(ByVal Id As Long)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_OnTextboxChanged(ByVal Id As Long, ByVal Text As String)
```

```
End Sub
```

```
Private Sub PropertyManagerPage2Handler8_OnSelectionBoxListChanged(ByVal Id As Long, ByVal Text As Long)
```

```
    m_pageObj.GetCmd().OnBodySelect
```

```
End Sub
```

[Back to top](#Top)
