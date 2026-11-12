---
title: "Traverse Assembly at Component and Feature Level Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_Assembly_at_Component_and_Feature_Level_Example_VB.htm"
---

# Traverse Assembly at Component and Feature Level Example (VBA)

## Traversing Assembly at Component and Feature Levels Example (VBA)

This example shows how to traverse an assembly at the component and feature levels.

```
'------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document to open
'    exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Specified assembly document opens.
' 2. Traverses the components and features in the assembly.
' 3. Examine the Immediate window.
'-------------------------------------------------------
```

```
Option Explicit
```

```
Sub TraverseFeatureFeatures(swFeat As SldWorks.Feature, nLevel As Long)
```

```
    Dim swSubFeat As SldWorks.Feature
    Dim swSubSubFeat As SldWorks.Feature
    Dim swSubSubSubFeat As SldWorks.Feature
    Dim sPadStr As String
    Dim i As Long
```

```
    For i = 0 To nLevel
        sPadStr = sPadStr + "  "
    Next i
```

```
    While Not swFeat Is Nothing
        Debug.Print sPadStr + swFeat.Name + " [" + swFeat.GetTypeName + "]"
        Set swSubFeat = swFeat.GetFirstSubFeature
        While Not swSubFeat Is Nothing
            Debug.Print sPadStr + "  " + swSubFeat.Name + " [" + swSubFeat.GetTypeName + "]"
            Set swSubSubFeat = swSubFeat.GetFirstSubFeature
            While Not swSubSubFeat Is Nothing
                Debug.Print sPadStr + "    " + swSubSubFeat.Name + " [" + swSubSubFeat.GetTypeName + "]"
                Set swSubSubSubFeat = swSubFeat.GetFirstSubFeature
                While Not swSubSubSubFeat Is Nothing
                    Debug.Print sPadStr + "      " + swSubSubSubFeat.Name + " [" + swSubSubSubFeat.GetTypeName + "]"
                    Set swSubSubSubFeat = swSubSubSubFeat.GetNextSubFeature()
                Wend
                Set swSubSubFeat = swSubSubFeat.GetNextSubFeature()
            Wend
            Set swSubFeat = swSubFeat.GetNextSubFeature()
        Wend
        Set swFeat = swFeat.GetNextFeature
    Wend
```

```
End Sub
```

```
Sub TraverseComponentFeatures(swComp As SldWorks.Component2, nLevel As Long)
```

```
    Dim swFeat As SldWorks.Feature

    Set swFeat = swComp.FirstFeature
    TraverseFeatureFeatures swFeat, nLevel
```

```
End Sub
```

```
Sub TraverseComponent(swComp As SldWorks.Component2, nLevel As Long)
```

```
    Dim vChildComp As Variant
    Dim swChildComp As SldWorks.Component2
    Dim swCompConfig As SldWorks.Configuration
    Dim sPadStr As String
    Dim i As Long
```

```
    For i = 0 To nLevel - 1
        sPadStr = sPadStr + "  "
    Next i
```

```
    vChildComp = swComp.GetChildren
    For i = 0 To UBound(vChildComp)
        Set swChildComp = vChildComp(i)
        Debug.Print sPadStr & "+" & swChildComp.Name2 & " <" & swChildComp.ReferencedConfiguration & ">"
        TraverseComponentFeatures swChildComp, nLevel
        TraverseComponent swChildComp, nLevel + 1
    Next i
```

```
End Sub
```

```
Sub TraverseModelFeatures(swModel As SldWorks.ModelDoc2, nLevel As Long)
```

```
    Dim swFeat As SldWorks.Feature
```

```
    Set swFeat = swModel.FirstFeature
    TraverseFeatureFeatures swFeat, nLevel
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swConf As SldWorks.Configuration
    Dim swRootComp As SldWorks.Component2
    Dim nStart As Long
    Dim bRet As Boolean
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
```

```
    ' Open assembly
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\smartcomponents\stepped_shaft.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    Set swConf = swModel.GetActiveConfiguration
    Set swRootComp = swConf.GetRootComponent3(True)
```

```
    nStart = Timer
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    ' Traverse components and features
    TraverseModelFeatures swModel, 1
    TraverseComponent swRootComp, 1
```

```
    Debug.Print ""
    Debug.Print "Time = " & Timer - nStart & " seconds"
```

```
End Sub
```
