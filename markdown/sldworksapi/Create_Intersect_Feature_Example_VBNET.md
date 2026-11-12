---
title: "Create Intersect Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Intersect_Feature_Example_VBNET.htm"
---

# Create Intersect Feature Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeatureMgr As FeatureManager
        Dim swFeature As Feature
        Dim bodyArray As Object
        Dim bodyExcludeArray() As Boolean
        Dim excludeArray As Object
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String
        Dim nbrBodies As Integer
        Dim i As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2017\whatsnew\parts\pot.SLDPRT"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        swFeatureMgr = swModel.FeatureManager

        'Select features for intersect feature
        status = swModelDocExt.SelectByID2("Shell1", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Plane6", "PLANE", 0, 0, 0, True, 0, Nothing, 0)

        ' Create intersect feature
        ' * Do not cap planar surface openings of intersect feature
        ' * Create internal regions
        bodyArray = swFeatureMgr.PreIntersect2(False, 1)
        swModel.ClearSelection2(True)

        nbrBodies = UBound(bodyArray)
        ReDim bodyExcludeArray(nbrBodies)
        For i = 0 To nbrBodies
            bodyExcludeArray(i) = False
        Next
        excludeArray = bodyExcludeArray
        swFeature = swFeatureMgr.PostIntersect(excludeArray, True, False)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
