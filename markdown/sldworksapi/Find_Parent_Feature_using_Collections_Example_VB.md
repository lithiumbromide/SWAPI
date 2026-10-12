---
title: "Find Parent Feature using Collections Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Find_Parent_Feature_using_Collections_Example_VB.htm"
---

# Find Parent Feature using Collections Example (VBA)

This example shows how to walk the FeatureManager design tree and touch all of the parent features of a selected feature. Using collections lets you visit all of the parent features without using a recursive operation.

```
'----------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
' 2. Expand the Cut list(31) folder and click Gusset4.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Finds the parent features of the selected feature
'    and selects that parent features in the graphics area.
' 2. Examine the Immediate window and graphics area.
'----------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModelDoc2 As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swBody2 As SldWorks.Body2
Dim swFace2 As SldWorks.Face2
Dim swFeature As SldWorks.Feature
Dim parents As Variant
Dim varobj As Variant
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModelDoc2 = swApp.ActiveDoc
    Set swSelMgr = swModelDoc2.SelectionManager
    Set swBody2 = swSelMgr.GetSelectedObject6(1, -1)
```

```
    Set swFace2 = swBody2.GetFirstFace
    Set swFeature = swFace2.GetFeature
    Debug.Print ("Selected feature name: " & swFeature.Name)
    Debug.Print ("Selected feature type: " & swFeature.GetTypeName)
    Debug.Print ("")
    If "WeldMemberFeat" <> swFeature.GetTypeName Then
        Dim parentcoll As New Collection
        Set varobj = swFeature
        parentcoll.Add swFeature
        Do While parentcoll.Count > 0
            Set swFeature = parentcoll(1)
            If "WeldMemberFeat" <> swFeature.GetTypeName Then
                parentcoll.Remove 1
                parents = swFeature.GetParents
                For Each varobj In parents
                   Set swFeature = varobj
                    Debug.Print ("  Parent feature name: " & swFeature.Name)
                    Debug.Print ("  Parent feature type: " & swFeature.GetTypeName)
                    Debug.Print ("")
                   parentcoll.Add varobj
                Next varobj
                Set swFeature = Nothing
            Else
                Exit Do
            End If
        Loop
    End If
    If Not swFeature Is Nothing Then
        swFeature.Select2 False, 0
    Else
        Stop
    End If
```

```
End Sub
```
