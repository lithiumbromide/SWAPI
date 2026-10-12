---
title: "Get Type of Instant3D Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Type_of_Instant3D_Feature_Example_VB.htm"
---

# Get Type of Instant3D Feature Example (VBA)

This example shows how to get the types and persistent IDs of underlying features of Instant3D features.

```
'-----------------------------------------------------
' Preconditions:
' 1. Verify that the specified part exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part and traverses the FeatureManager
'    design tree.
' 2. Gets the types of features, including the types
'    of underlying features and persistent IDs
'    of Instant3D features.
' 3. Examine the Immediate window.
'-----------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swFeature As SldWorks.Feature
Dim fileName As String
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block.sldprt"
Set swModel = swApp.OpenDoc6(fileName, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
```

```
Set swFeature = swModel.FirstFeature
```

```
Call SelectFeat(swFeature)
```

```
End Sub
```

```
Public Function SelectFeat(featureTemp As SldWorks.Feature) As Boolean
```

```
While Not featureTemp Is Nothing
```

```
    Dim featureName As String
    featureName = featureTemp.GetTypeName2
```

```
    Debug.Print featureName
```

```
    ' Instant3D features are ICE features
    If featureName = "ICE" Then
        Debug.Print "   Type:     " & featureTemp.GetTypeName
        Debug.Print "   ID:       " & featureTemp.GetID
    End If
```

```
    Set featureTemp = featureTemp.GetNextFeature
```

```
Wend
```

```
End Function
```
