---
title: "Traverse SubFeatures Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_SubFeatures_Example_VB.htm"
---

# Traverse SubFeatures Example (VBA)

## Traverse Subfeatures Example (VBA)

This example shows how to traverse the subfeatures of each feature in a part.

```
'---------------------------------------------
' Preconditions: Open a part that has at least one feature.
'
' Postconditions:
' 1. Gets all of the features and subfeatures.
' 2. Click OK to close each message box.
'---------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swPartDoc As SldWorks.ModelDoc2
Dim swFeature As SldWorks.feature
Dim swSubFeature As SldWorks.feature
Dim featureName As String
Dim subFeatureName As String
Dim message As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swPartDoc = swApp.ActiveDoc
```

```
    ' Get the first feature in part
    Set swFeature = swPartDoc.FirstFeature
```

```
    ' While we have a valid feature
    While Not swFeature Is Nothing
```

```
     ' Get the name of the feature
     featureName = swFeature.Name
     message = "Feature: " & featureName & Chr(10) & "  SubFeatures:"
     Set swSubFeature = swFeature.GetFirstSubFeature
```

```
     ' While we have a valid sub-feature
     While Not swSubFeature Is Nothing
```

```
      ' Get the name of the sub-feature
      subFeatureName = swSubFeature.Name
      message = message & Chr(10) & "    " & subFeatureName
```

```
      Set swSubFeature = swSubFeature.GetNextSubFeature
     ' Continue until the last sub-feature is found
     Wend
```

```
     ' Display the sub-features
     swApp.SendMsgToUser message
```

```
     ' Get the next feature
     Set swFeature = swFeature.GetNextFeature()
```

```
    ' Continue until the last feature is found
    Wend
```

```
End Sub
```
