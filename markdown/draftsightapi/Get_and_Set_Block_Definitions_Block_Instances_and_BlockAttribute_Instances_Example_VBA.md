---
title: "Get and Set Block Definitions, Block Instances, and BlockAttribute Instances Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBA.htm"
---

# Get and Set Block Definitions, Block Instances, and BlockAttribute Instances Example (VBA)

This example shows how to get and set Block definitions, Block instances, and BlockAttribute instances.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a document.
' 5. Review the code to see how Block definitions,
'    Block instances, and BlockAttribute instances
'    are modified.
' 6. Run the macro.
'
' Postconditions: Block definitions, Block instances, and
' BlockAttribute instances are modified. Message
' boxes pop up when a Block-related entity does not exist.
' Read the text in each message box before clicking OK to close it.
'----------------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
```

```
    'Connect to DraftSight application
    Set dsApp = GetObject(, "DraftSight.Application")
    'Abort any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand

    'Get active document
    Set dsDoc = dsApp.GetActiveDocument()
    If Not dsDoc Is Nothing Then
```

```
        'Test Block definitions
        TestBlockDefinitions dsDoc
```

```
    Else
        MsgBox "There are no open documents in DraftSight."
    End If
End Sub
Sub TestBlockDefinitions(dsDoc As DraftSight.Document)
```

```
    Dim dsVarBlkDefinitions As Variant
    Dim dsBlkDefinition As DraftSight.BlockDefinition
    Dim dsExtRef As DraftSight.ExternalReference
    Dim index As Integer
```

```
    'Get all Block definitions in the drawing
    dsVarBlkDefinitions = dsDoc.GetBlockDefinitions
```

```
    'Check if there are any Block definitions
    If IsArray(dsVarBlkDefinitions) Then
```

```
        For index = LBound(dsVarBlkDefinitions) To UBound(dsVarBlkDefinitions)
```

```
            Set dsBlkDefinition = dsVarBlkDefinitions(index)
```

```
            'Check if Block definition is a reference
            Set dsExtRef = dsBlkDefinition.GetExternalReference
            If Not dsExtRef Is Nothing Then
                MsgBox dsBlkDefinition.GetName & " block definition is a reference."
            Else
                MsgBox dsBlkDefinition.GetName & " block definition isn't a reference."
            End If
```

```
            'Test BlockAttribute definitions
            TestAttributeDefinitions dsBlkDefinition
```

```
            'Test Block instances
            TestBlockInstances dsBlkDefinition
```

```
        Next
```

```
    Else
        MsgBox "There are no Block definitions in """ & dsDoc.GetPathName & """ document."
    End If
End Sub
Sub TestAttributeDefinitions(dsBlkDefinition As DraftSight.BlockDefinition)
    Dim dsVarAttrDefinitions As Variant
    Dim dsAttrDefinition As DraftSight.AttributeDefinition
    Dim index As Integer
    Dim attrDefCaption As String
    Dim attrDefValue As String
    Dim attrDefName As String
    Dim newAttrCaptionValue As String
    Dim newAttrDefValue As String
    Dim newAttrDefName As String
```

```
    'Get all BlockAttribute definitions in Block definition
    dsVarAttrDefinitions = dsBlkDefinition.GetAttributeDefinitions
```

```
    'Check if there are any BlockAttribute definition
    If IsArray(dsVarAttrDefinitions) Then
```

```
        For index = LBound(dsVarAttrDefinitions) To UBound(dsVarAttrDefinitions)
```

```
            Set dsAttrDefinition = dsVarAttrDefinitions(index)
```

```
            'Get BlockAttribute definition caption and change
            attrDefCaption = dsAttrDefinition.Caption
```

```
            'Change caption value
            newAttrCaptionValue = dsAttrDefinition.Caption & "_Changed"
            dsAttrDefinition.Caption = newAttrCaptionValue
```

```
            If newAttrCaptionValue <> dsAttrDefinition.Caption Then
                MsgBox "The caption of '" & dsAttrDefinition.Name + "' BlockAttribute definition wasn't changed from '" + attrDefCaption + "' to '" + newAttrCaptionValue + "'."
            End If
```

```
            'Get BlockAttribute definition value
            attrDefValue = dsAttrDefinition.Value
```

```
            'Change BlockAttribute definition value
            newAttrDefValue = dsAttrDefinition.Value & "_Changed"
            dsAttrDefinition.Value = newAttrDefValue
```

```
            If newAttrDefValue <> dsAttrDefinition.Value Then
                MsgBox "The value of '" & dsAttrDefinition.Name + "' BlockAttribute definition wasn't changed from '" + attrDefValue + "' to '" + newAttrDefValue + "'."
            End If
```

```
            'Get BlockAttribute definition name
            attrDefName = dsAttrDefinition.Name
```

```
            'Change BlockAttribute definition name
            newAttrDefName = dsAttrDefinition.Name & "_Changed"
            dsAttrDefinition.Name = newAttrDefName
```

```
            If newAttrDefName <> dsAttrDefinition.Name Then
                MsgBox "The name of '" & dsAttrDefinition.Name + "' BlockAttribute definition wasn't changed from '" + attrDefName + "' to '" + newAttrDefName + "'."
            End If
```

```
        Next
```

```
    Else
        MsgBox "There are no BlockAttribute definitions in """ & dsBlkDefinition.GetName & """ block definition."
    End If
End Sub
Sub TestBlockInstances(dsBlkDefinition As DraftSight.BlockDefinition)
    Dim dsVarBlockInstances As Variant
    Dim dsBlockInstance As DraftSight.BlockInstance
    Dim dsBlockDefinition As DraftSight.BlockDefinition
    Dim Workspace As Object
    Dim workSpaceType As DraftSight.dsObjectType_e
    Dim dsSheet As DraftSight.Sheet
    Dim dsModel As DraftSight.Model
    Dim index As Integer
```

```
    'Get Block instances of Block definition
    dsVarBlockInstances = dsBlkDefinition.GetBlockInstances
```

```
    'Check if there are any Block instances
    If IsArray(dsVarBlockInstances) Then
```

```
        For index = LBound(dsVarBlockInstances) To UBound(dsVarBlockInstances)
```

```
            Set dsBlockInstance = dsVarBlockInstances(index)
```

```
            'Test attribute instances
            TestAttributeInstances dsBlockInstance
```

```
            'Get Block definition from Block instance
            Set dsBlockDefinition = dsBlockInstance.GetBlockDefinition
            If dsBlockDefinition Is Nothing Then
                MsgBox "GetBlockDefinition method returns Nothing for Block instance with ID=""" & dsBlockInstance.GetID & "."
            End If
```

```
            'Get working space
            dsBlockInstance.GetWorkingSpace workSpaceType, Workspace
```

```
            If Not Workspace Is Nothing Then
```

```
                'If work space is sheet
                If workSpaceType = dsSheetType Then
                    Set dsSheet = Workspace
```

```
                    If dsSheet Is Nothing Then
                        MsgBox "GetWorkingSpace method returns dsSheetType type, but sheet object is Nothing."
                    End If
```

```
                ElseIf workSpaceType = dsModelType Then
                    Set dsModel = Workspace
```

```
                    If dsModel Is Nothing Then
                        MsgBox "GetWorkingSpace method returns dsModelType type, but model object is Nothing."
                    End If
```

```
                End If
```

```
            Else
                MsgBox "GetWorkingSpace method returns Nothing for Block instance."
            End If
```

```
        Next
```

```
    Else
        MsgBox "There are no Block instances of """ & dsBlkDefinition.GetName & """ Block definition."
    End If
End Sub
Sub TestAttributeInstances(dsBlockInstance As DraftSight.BlockInstance)
```

```
    Dim dsVarAttrInstances As Variant
    Dim dsAttrInstance As DraftSight.AttributeInstance
    Dim index As Integer
    Dim attrInstanceName As String
    Dim attrInstanceValue As String
    Dim newAttrInstanceValue As String
```

```
    'Get BlockAttribute instances
    dsVarAttrInstances = dsBlockInstance.GetAttributeInstances
```

```
    'Check if there are any BlockAttribute instances
    If IsArray(dsVarAttrInstances) Then
```

```
        For index = LBound(dsVarAttrInstances) To UBound(dsVarAttrInstances)
```

```
            Set dsAttrInstance = dsVarAttrInstances(index)
```

```
            'Get BlockAttribute instance name
            attrInstanceName = dsAttrInstance.GetName
```

```
            'Get BlockAttribute instance value
            attrInstanceValue = dsAttrInstance.Value
```

```
            'Change BlockAttribute instance value
            newAttrInstanceValue = dsAttrInstance.Value + "_Changed"
            dsAttrInstance.Value = newAttrInstanceValue
```

```
            If newAttrInstanceValue <> dsAttrInstance.Value Then
                MsgBox "The value of '" & dsAttrInstance.GetName + "' attribute instance wasn't changed from '" + attrInstanceValue + "' to '" + newAttrInstanceValue + "'."
            End If
```

```
            'Test general properties
            TestAttributeInstanceGeneralProperties dsAttrInstance
```

```
            'Select BlockAttribute instance
            dsAttrInstance.Select (True)
```

```
            'Deselect BlockAttribute instance
            dsAttrInstance.Select (False)
```

```
        Next
```

```
    Else
        MsgBox "There are no BlockAttribute instances in """ & dsBlockInstance.GetBlockDefinition.GetName & """ Block instance."
    End If
```

```
End Sub
Sub TestAttributeInstanceGeneralProperties(dsAttrInstance As DraftSight.AttributeInstance)
    Dim layer As String
    Dim lineStyle As String
    Dim lineScale As Double
    Dim newLineScale As Double
    Dim precision As Double
    Dim lineWeight As DraftSight.dsLineWeight_e
    Dim newLineWeight As DraftSight.dsLineWeight_e
    Dim visible As Boolean
    Dim newVisibleValue As Boolean
```

```
    'Get layer name
    layer = dsAttrInstance.layer
```

```
    'Set the same layer
    dsAttrInstance.layer = layer
```

```
    'Get line scale
    lineScale = dsAttrInstance.lineScale
```

```
    'Set line scale
    newLineScale = 8.6
    dsAttrInstance.lineScale = newLineScale
```

```
    precision = 0.000000001
    If Abs(newLineScale - dsAttrInstance.lineScale) > precision Then
        MsgBox "The line scale of '" & dsAttrInstance.GetName + "' attribute instance wasn't changed from '" + lineScale + "' to '" + newLineScale + "'."
    End If
```

```
    'Get line style
    lineStyle = dsAttrInstance.lineStyle
```

```
    'Set the same line style
    dsAttrInstance.lineStyle = lineStyle
```

```
    'Get line weight
    lineWeight = dsAttrInstance.lineWeight
```

```
    'Set new line weight
    newLineWeight = dsLnWt_015
    dsAttrInstance.lineWeight = newLineWeight
    If newLineWeight <> dsAttrInstance.lineWeight Then
        MsgBox "The line weight of '" & dsAttrInstance.GetName + "' attribute instance wasn't changed from '" + lineWeight + "' to '" + newLineWeight + "'."
    End If
```

```
    'Get visible property
    visible = dsAttrInstance.visible
```

```
    'Set visible property
    newVisibleValue = Not visible
    dsAttrInstance.visible = newVisibleValue
    If newVisibleValue <> dsAttrInstance.visible Then
        MsgBox "The visible property of '" & dsAttrInstance.GetName + "' attribute instance wasn't changed from '" + visible + "' to '" + newVisibleValue + "'."
    End If
```

```
End Sub
```
