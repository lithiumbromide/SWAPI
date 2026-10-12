---
title: "Get and Set FeatureManager Design Tree Display (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_FeatureManager_Design_Tree_Display_Example_VB.htm"
---

# Get and Set FeatureManager Design Tree Display (VBA)

This example shows how to get and set properties related to displaying the FeatureManager design tree.

```
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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModelDoc As SldWorks.ModelDoc2
Dim swFeatMgr As SldWorks.FeatureManager
Dim document As String
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
document = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\bladed shaft.sldasm"
```

```
Set swApp = Application.SldWorks
Set swModelDoc = swApp.OpenDoc6(document, swDocASSEMBLY, swOpenDocOptions_Silent, "", errors, warnings)
Set swFeatMgr = swModelDoc.FeatureManager
```

```
Debug.Print "----------------- Before changing FeatureManager design tree properties -----------------"
Debug.Print "View dependencies     = " & swFeatMgr.ViewDependencies
Debug.Print "View features         = " & swFeatMgr.ViewFeatures
Debug.Print "Show feature details  = " & swFeatMgr.ShowFeatureDetails
Debug.Print "Show hierarchy only   = " & swFeatMgr.ShowHierarchyOnly
```

```
Stop
' Examine the Immediate window and
' FeatureManager design tree before
' resuming the macro
```

```
' Change details, dependencies, hierarchy, and
' features-related properties
    If (swFeatMgr.ViewDependencies) Then
        swFeatMgr.ViewFeatures = True
    Else
        swFeatMgr.ViewDependencies = True
    End If
```

```
    If (swFeatMgr.ShowFeatureDetails) Then
        swFeatMgr.ShowHierarchyOnly = True
    Else
        swFeatMgr.ShowFeatureDetails = True
    End If
```

```
Debug.Print "----------------- After changing FeatureManager design tree properties -----------------"
Debug.Print "View dependencies     = " & swFeatMgr.ViewDependencies
Debug.Print "View features         = " & swFeatMgr.ViewFeatures
Debug.Print "Show feature details  = " & swFeatMgr.ShowFeatureDetails
Debug.Print "Show hierarchy only   = " & swFeatMgr.ShowHierarchyOnly
```

```
End Sub
```
