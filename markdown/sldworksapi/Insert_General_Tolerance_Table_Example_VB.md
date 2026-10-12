---
title: "Insert General Tolerance Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_General_Tolerance_Table_Example_VB.htm"
---

# Insert General Tolerance Table Example (VBA)

This example shows how to create a general tolerance table annotation.

'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Ensure that the specified table template exists.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Creates a general tolerance table annotation.
' 2. Inspect the Immediate window, the graphics area, and the Tables folder
' of the FeatureManager design tree.
'----------------------------------------------------------------------------

```vb
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim gttAnno As SldWorks.GeneralToleranceTableAnnotation
 Dim gttFeat As SldWorks.GeneralToleranceTableFeature
 Dim feat As SldWorks.Feature
 Dim mde As SldWorks.ModelDocExtension
 Dim boolstatus As Boolean
 Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc
     Set mde = Part.Extension
     Set gttAnno = mde.InsertGeneralToleranceTableAnnotation("c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\bom-standard.sldbomtbt", 481, 163)
     Set gttFeat = gttAnno.GeneralToleranceTableFeature
     Set feat = gttFeat.GetFeature
     Debug.Print "Created " & feat.Name
     boolstatus = Part.EditRebuild3()

End Sub
```
