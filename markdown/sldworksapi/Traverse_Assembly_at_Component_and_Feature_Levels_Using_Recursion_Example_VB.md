---
title: "Traverse Assembly at Component and Feature Levels Using Recursion Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VB.htm"
---

# Traverse Assembly at Component and Feature Levels Using Recursion Example (VBA)

This example shows how to traverse an assembly at the component and feature levels using recursion.

```vb
 '--------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open an assembly document containing nested subassemblies.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Traverses the assembly.
 ' 2. Examine the Immediate window.
 '---------------------------------------------------------------------------
```

```
Option Explicit
```

```
Sub TraverseFeatureFeatures(swFeat As SldWorks.Feature, nLevel As Long)
```

```
    Dim swSubFeat                   As SldWorks.Feature
    Dim swSubSubFeat                As SldWorks.Feature
    Dim swSubSubSubFeat             As SldWorks.Feature
    Dim sPadStr                     As String
    Dim i                           As Long
```

```
    For i = 0 To nLevel
        sPadStr = sPadStr + "  "
    Next i
```

```
    While Not swFeat Is Nothing
        Debug.Print sPadStr + swFeat.Name + " [" + swFeat.GetTypeName + "]"
```

```
        Set swSubFeat = swFeat.GetFirstSubFeature
        While Not swSubFeat Is Nothing
            Debug.Print sPadStr + "  " + swSubFeat.Name + " [" + swSubFeat.GetTypeName + "]"
```

```
            Set swSubSubFeat = swSubFeat.GetFirstSubFeature
            While Not swSubSubFeat Is Nothing
                Debug.Print sPadStr + "    " + swSubSubFeat.Name + " [" + swSubSubFeat.GetTypeName + "]"
```

```
                Set swSubSubSubFeat = swSubSubFeat.GetFirstSubFeature
                While Not swSubSubSubFeat Is Nothing
                    Debug.Print sPadStr + "      " + swSubSubSubFeat.Name + " [" + swSubSubSubFeat.GetTypeName + "]"
```

```
                    Set swSubSubSubFeat = swSubSubSubFeat.GetNextSubFeature()
```

```
                Wend
```

```
                Set swSubSubFeat = swSubSubFeat.GetNextSubFeature()
```

```
            Wend
```

```
            Set swSubFeat = swSubFeat.GetNextSubFeature()
```

```
        Wend
```

```
        Set swFeat = swFeat.GetNextFeature
```

```
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
```

```
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
    Dim vChildComp                  As Variant
    Dim swChildComp                 As SldWorks.Component2
    Dim sPadStr                     As String
    Dim i                           As Long
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
```

```
        Debug.Print sPadStr & "+" & swChildComp.Name2 & " <" & swChildComp.ReferencedConfiguration & ">"
```

```
        TraverseComponentFeatures swChildComp, nLevel
        TraverseComponent swChildComp, nLevel + 1

    Next i

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

End Sub
```

```
Sub main()
```

```
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swConfMgr                   As SldWorks.ConfigurationManager
    Dim swConf                      As SldWorks.Configuration
    Dim swRootComp                  As SldWorks.Component2
    Dim StartTime                   As Double
    Dim FinishTime                  As Double
    Dim TotalTime                   As Double
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swConfMgr = swModel.ConfigurationManager
    Set swConf = swConfMgr.ActiveConfiguration
    Set swRootComp = swConf.GetRootComponent3(True)
```

```
    StartTime = Timer ' Start time
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    TraverseModelFeatures swModel, 1
```

```
    If swModel.GetType = SwConst.swDocASSEMBLY Then
        TraverseComponent swRootComp, 1

    End If
```

```
    FinishTime = Timer ' End time
    TotalTime = FinishTime - StartTime ' Elapsed time
    Debug.Print ("Time = " & TotalTime & " sec")
```

```
End Sub
```
