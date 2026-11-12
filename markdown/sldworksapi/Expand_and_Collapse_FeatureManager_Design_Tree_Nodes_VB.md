---
title: "Expand or Collapse FeatureManager Design Tree Nodes Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_VB.htm"
---

# Expand or Collapse FeatureManager Design Tree Nodes Example (VBA)

This example shows how to traverse, expand, and collapse the nodes of a FeatureManager design tree.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part or assembly document.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Expands all of the FeatureManager design tree nodes.
 ' 2. Click OK to collapse all nodes.
 ' 3. Inspect the Immediate window.
 '--------------------------------------------------------------------------
Option Explicit
Dim traverseLevel As Integer
 Dim expandThis As Boolean
Sub main()
     Dim i As Integer
     Dim swApp As SldWorks.SldWorks
     Dim myModel As SldWorks.ModelDoc2
     Dim featureMgr As SldWorks.FeatureManager
     Dim rootNode As SldWorks.TreeControlItem

    Set swApp = Application.SldWorks
     Set myModel = swApp.ActiveDoc
     Set featureMgr = myModel.FeatureManager
     Set rootNode = featureMgr.GetFeatureTreeRootItem2(swFeatMgrPaneBottom)

    expandThis = True

    For i = 0 To 1
         If Not rootNode Is Nothing Then
             Debug.Print
             traverseLevel = 0
             traverse_node rootNode
         End If

        expandThis = False

        If i = 0 Then
             MsgBox "OK to collapse all nodes?"
         End If
     Next
 End Sub
Private Sub traverse_node(node As SldWorks.TreeControlItem)
    Dim childNode As SldWorks.TreeControlItem
     Dim featureNode As SldWorks.Feature
     Dim componentNode As SldWorks.Component2
     Dim nodeObjectType As Long
     Dim nodeObject As Object
     Dim restOfString As String
     Dim indent As String
     Dim i As Integer
     Dim displayNodeInfo As Boolean
     Dim compName As String
     Dim suppr As Long, supprString As String
     Dim vis As Long, visString As String
     Dim fixed As Boolean, fixedString As String
     Dim componentDoc As Object, docString As String
     Dim refConfigName As String
    displayNodeInfo = False
     nodeObjectType = node.ObjectType
     Set nodeObject = node.Object
    Select Case nodeObjectType

        Case SwConst.swTreeControlItemType_e.swFeatureManagerItem_Feature:

            displayNodeInfo = True
             If Not nodeObject Is Nothing Then
                 Set featureNode = nodeObject
                 restOfString = "[FEATURE: " & featureNode.Name & "]"
             Else
                 restOfString = "[FEATURE: object Null?!]"
             End If

        Case SwConst.swTreeControlItemType_e.swFeatureManagerItem_Component:

            displayNodeInfo = True

            If Not nodeObject Is Nothing Then
                 Set componentNode = nodeObject
                 compName = componentNode.Name2

                If (compName = "") Then
                     compName = "???"
                 End If

                suppr = componentNode.GetSuppression

                Select Case (suppr)

                    Case SwConst.swComponentSuppressionState_e.swComponentFullyResolved
                         supprString = "Resolved"

                    Case SwConst.swComponentSuppressionState_e.swComponentLightweight
                         supprString = "Lightweight"

                    Case SwConst.swComponentSuppressionState_e.swComponentSuppressed
                         supprString = "Suppressed"

                End Select

                vis = componentNode.Visible

                Select Case (vis)

                    Case SwConst.swComponentVisibilityState_e.swComponentHidden
                         visString = "Hidden"

                    Case SwConst.swComponentVisibilityState_e.swComponentVisible
                         visString = "Visible"

                End Select

                fixed = componentNode.IsFixed

                If fixed = 0 Then
                     fixedString = "Floating"
                 Else
                     fixedString = "Fixed"
                 End If

                Set componentDoc = componentNode.GetModelDoc2

                If componentDoc Is Nothing Then
                     docString = "NotLoaded"
                 Else
                     docString = "Loaded"
                 End If

                refConfigName = componentNode.ReferencedConfiguration

                If (refConfigName = "") Then
                     refConfigName = "???"
                 End If

                restOfString = "[COMPONENT: " & compName & " " & docString & " " & supprString & " " & visString & " " & refConfigName & "]"
             Else
                 restOfString = "[COMPONENT: object Null?!]"
             End If

        Case Else:
            displayNodeInfo = True
            If Not nodeObject Is Nothing Then
                 restOfString = "[object type not handled]"
             Else
                 restOfString = "[object Null?!]"
             End If
    End Select
    For i = 1 To traverseLevel
         indent = indent & "  "
     Next i
    If (displayNodeInfo) Then
         Debug.Print indent & node.Text & " : " & restOfString
     End If
    ' Expand the node
     node.Expanded = expandThis
     traverseLevel = traverseLevel + 1
     Set childNode = node.GetFirstChild

    While Not childNode Is Nothing
         Debug.Print indent & "Node is expanded: " & childNode.Expanded
         traverse_node childNode
         Set childNode = childNode.GetNext
     Wend
    traverseLevel = traverseLevel - 1
End Sub
```
