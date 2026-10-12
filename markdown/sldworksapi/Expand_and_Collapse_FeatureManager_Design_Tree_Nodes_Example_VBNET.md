---
title: "Expand or Collapse FeatureManager Design Tree Nodes Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_VBNET.htm"
---

# Expand or Collapse FeatureManager Design Tree Nodes Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim traverseLevel As Integer
     Dim expandThis As Boolean

     Sub main()
         Dim i As  Integer

         Dim myModel As ModelDoc2
         Dim featureMgr As FeatureManager
         Dim rootNode As TreeControlItem

         myModel = swApp.ActiveDoc
         featureMgr = myModel.FeatureManager
         rootNode = featureMgr.GetFeatureTreeRootItem2(swFeatMgrPane_e.swFeatMgrPaneBottom)

         expandThis = True

         For i = 0 To 1
             If Not rootNode Is Nothing Then
                 Debug.Print("")
                 traverseLevel = 0
                 traverse_node(rootNode)
             End If

             expandThis =  False

             If i = 0 Then
                 MsgBox("OK to collapse all nodes?")
             End If
         Next
     End Sub

     Private Sub traverse_node(ByVal node As TreeControlItem)

         Dim childNode As TreeControlItem
         Dim featureNode As Feature
         Dim componentNode As Component2
         Dim nodeObjectType As Long
         Dim nodeObject As Object
         Dim restOfString As String = ""
         Dim indent As String = ""
         Dim i As  Integer
         Dim displayNodeInfo As Boolean
         Dim compName As String
         Dim suppr As Long, supprString As String = ""
         Dim vis As Long, visString As String = ""
         Dim fixed As Boolean, fixedString As String = ""
         Dim componentDoc As Object, docString As String = ""
         Dim refConfigName As String = ""

         displayNodeInfo =  False
         nodeObjectType = node.ObjectType
         nodeObject = node.Object

         Select Case nodeObjectType
             Case swTreeControlItemType_e.swFeatureManagerItem_Feature

                 displayNodeInfo = True
                 If Not nodeObject Is Nothing Then
                     featureNode = nodeObject
                     restOfString =  "[FEATURE: " & featureNode.Name & "]"
                 Else
                     restOfString =  "[FEATURE: object Null?!]"
                 End If

             Case swTreeControlItemType_e.swFeatureManagerItem_Component

                 displayNodeInfo = True

                 If Not nodeObject Is Nothing Then
                     componentNode = nodeObject
                     compName = componentNode.Name2

                     If (compName = "") Then
                         compName =  "???"
                     End If

                     suppr = componentNode.GetSuppression

                     Select Case (suppr)

                         Case swComponentSuppressionState_e.swComponentFullyResolved
                             supprString =  "Resolved"

                         Case swComponentSuppressionState_e.swComponentLightweight
                             supprString =  "Lightweight"

                         Case swComponentSuppressionState_e.swComponentSuppressed
                             supprString =  "Suppressed"

                     End Select

                     vis = componentNode.Visible

                     Select Case (vis)

                         Case swComponentVisibilityState_e.swComponentHidden
                             visString =  "Hidden"

                         Case swComponentVisibilityState_e.swComponentVisible
                             visString =  "Visible"

                     End Select

                     fixed = componentNode.IsFixed

                     If fixed = 0 Then
                         fixedString = "Floating"
                     Else
                         fixedString = "Fixed"
                     End If

                     componentDoc = componentNode.GetModelDoc2

                     If componentDoc Is Nothing Then
                         docString =  "NotLoaded"
                     Else
                         docString =  "Loaded"
                     End If

                     refConfigName = componentNode.ReferencedConfiguration

                     If (refConfigName = "") Then
                         refConfigName = "???"
                     End If

                     restOfString =  "[COMPONENT: " & compName & " " & docString & " " & supprString & " " & visString & " " & refConfigName & "]"
                 Else
                     restOfString =  "[COMPONENT: object Null?!]"
                 End If

             Case Else

                 displayNodeInfo =  True

                 If Not nodeObject Is Nothing Then
                     restOfString =  "[object type not handled]"
                 Else
                     restOfString =  "[object Null?!]"
                 End If

         End Select

         For i = 1 To traverseLevel
             indent = indent & "  "
         Next i

         If (displayNodeInfo) Then
             Debug.Print(indent & node.Text & " : " & restOfString)
         End If

         ' Expand the node
         node.Expanded = expandThis
         traverseLevel = traverseLevel + 1
         childNode = node.GetFirstChild

         While Not childNode Is Nothing
             Debug.Print(indent   "Node is expanded: " & childNode.Expanded)
             traverse_node(childNode)
             childNode = childNode.GetNext
         End While

         traverseLevel = traverseLevel - 1

     End Sub

     Public swApp As SldWorks

 End  Class
```
