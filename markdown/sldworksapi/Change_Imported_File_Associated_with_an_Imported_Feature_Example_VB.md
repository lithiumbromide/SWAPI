---
title: "Change Imported File Associated with an Imported Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Imported_File_Associated_with_an_Imported_Feature_Example_VB.htm"
---

# Change Imported File Associated with an Imported Feature Example (VBA)

This example shows how to change the imported file associated with an imported feature.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Verify that c:\temp exists.
' 2. Open public_documents\samples\tutorial\api\cylinder20.sldprt.
' 3. Click File > Save As > Parasolid (*.x_t) in Save as type.
' 4. Type c:\temp before cylinder20.X_T in File name and click Save.
' 5. Open public_documents\samples\tutorial\api\cam roller.sldprt.
' 6. Select 91212_182-P9_SWP_001-1-solid1 in the FeatureManager
'    design tree.
' 7. Open the Immediate window.
'
' Postconditions:
' 1. Replaces the selected imported feature with the specified
'    imported file, c:\temp\cylinder20.x_t.
' 2. Examine the Immediate window and click each imported feature
'    in the FeatureManager design tree.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'-----------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Const sImportFileName As String = "C:\temp\cylinder20.x_t"
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
    Dim swNewModel As SldWorks.ModelDoc2
    Dim swNewPart As SldWorks.PartDoc
    Dim vBodyArr As Variant
    Dim swBody As SldWorks.Body2
    Dim swTempBody As SldWorks.Body2
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Feat = " & swFeat.Name
    Debug.Print "    FeatTypeName = " & swFeat.GetTypeName
```

```
    ' Open import file into a new part file
    bRet = swApp.LoadFile2(sImportFileName, "")
    Set swNewModel = swApp.ActiveDoc
    Set swNewPart = swNewModel
```

```
    ' Only consider solid bodies
    vBodyArr = swNewPart.GetBodies2(swSolidBody, True)
```

```
    ' Only consider first solid body
    Set swBody = vBodyArr(0)
    Set swTempBody = swBody.Copy
    bRet = swFeat.SetBody2(swTempBody, False)
    Debug.Print "       Body replaced? " & bRet
```

```
    ' Close SOLIDWORKS Design file associated with opening the import file
    swApp.QuitDoc swNewModel.GetTitle
```

```
    bRet = swModel.ForceRebuild3(False)
    swModel.ViewZoomtofit2
```

```
End Sub
```
