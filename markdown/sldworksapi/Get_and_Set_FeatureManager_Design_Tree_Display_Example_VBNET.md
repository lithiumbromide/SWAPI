---
title: "Get and Set FeatureManager Design Tree Display (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_FeatureManager_Design_Tree_Display_Example_VBNET.htm"
---

# Get and Set FeatureManager Design Tree Display (VB.NET)

This example shows how to get and set properties related to displaying the FeatureManager design tree.

```vb
'----------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified document exists.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the assembly and gets the FeatureManager
 '    design tree's display-related property values.
 ' 2. Examine both the Immediate window and the FeatureManager
 '    design tree, then press F5.
 ' 3. Re-examine both the Immediate window the
 '    FeatureManager design tree to verify the changes.
 '
 ' NOTE: Because this assembly document is used
 ' elsewhere, do not save changes.
 '----------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public Sub Main()

         Dim swModelDoc As ModelDoc2
         Dim swFeatMgr As FeatureManager
         Dim document As String
         Dim errors As Integer
         Dim warnings As Integer

         document =  "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\bladed shaft.sldasm"

         swModelDoc = swApp.OpenDoc6(document, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
         swFeatMgr = swModelDoc.FeatureManager

         Debug.Print("----------------- Before changing FeatureManager design tree properties -----------------")
         Debug.Print("View dependencies     = " & swFeatMgr.ViewDependencies)
         Debug.Print("View features         = " & swFeatMgr.ViewFeatures)
         Debug.Print("Show feature details  = " & swFeatMgr.ShowFeatureDetails)
         Debug.Print("Show hierarchy only   = " & swFeatMgr.ShowHierarchyOnly)

         Stop
         ' Examine the Immediate window and
         ' FeatureManager design tree before
         ' resuming the macro

         ' Change details, dependencies, hierarchy, and
         ' features-related properties
         If (swFeatMgr.ViewDependencies) Then
             swFeatMgr.ViewFeatures = True
         Else
             swFeatMgr.ViewDependencies = True
         End If

         If (swFeatMgr.ShowFeatureDetails) Then
             swFeatMgr.ShowHierarchyOnly = True
         Else
             swFeatMgr.ShowFeatureDetails = True
         End If

         Debug.Print("----------------- After changing FeatureManager design tree properties -----------------")
         Debug.Print("View dependencies     = " & swFeatMgr.ViewDependencies)
         Debug.Print("View features         = " & swFeatMgr.ViewFeatures)
         Debug.Print("Show feature details  = " & swFeatMgr.ShowFeatureDetails)
         Debug.Print("Show hierarchy only   = " & swFeatMgr.ShowHierarchyOnly)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
