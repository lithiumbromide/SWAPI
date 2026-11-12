---
title: "Create Intersect Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Intersect_Feature_Example_VB.htm"
---

# Create Intersect Feature Example (VBA)

This example shows how to create an intersect feature that includes only the internal (hollow) regions between the intersecting regions.

```
'----------------------------------------------------
' Preconditions: Verify that the specified part exists.
'
' Postconditions:
' 1. Opens the specified part.
' 2. Selects Shell1 and Plane6.
' 3. Creates Intersect1 feature.
' 4. Examine the FeatureManager design tree.
'
' NOTE: Because the part is used elsewhere, do not save
' changes.
'----------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureMgr As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim bodyArray As Variant
Dim bodyExcludeArray() As Boolean
Dim excludeArray As Variant
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
Dim nbrBodies As Long
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2017\whatsnew\parts\pot.SLDPRT"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    Set swFeatureMgr = swModel.FeatureManager
```

```
    'Select features for intersect feature
    status = swModelDocExt.SelectByID2("Shell1", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Plane6", "PLANE", 0, 0, 0, True, 0, Nothing, 0)

    ' Create intersect feature
    ' * Do not cap planar surface openings of intersect feature
    ' * Create internal regions
    bodyArray = swFeatureMgr.PreIntersect2(False, 1)
    swModel.ClearSelection2 True
```

```
    nbrBodies = UBound(bodyArray)
    ReDim bodyExcludeArray(nbrBodies)
    For i = 0 To nbrBodies
        bodyExcludeArray(i) = False
    Next
    excludeArray = bodyExcludeArray
    Set swFeature = swFeatureMgr.PostIntersect(excludeArray, True, False)
```

```
End Sub
```
