---
title: "Get Part's Feature Statistics Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Part's_Feature_Statistics_Example_VB.htm"
---

# Get Part's Feature Statistics Example (VBA)

This example shows how to get the statistics of all of the features in a part document.

```
'-------------------------------------------
' Preconditions:
' 1. Open a part that has multiple features.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the statistics for the features in
'    the part.
' 2. Examine the Immediate window.
'-------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swFeatStat As SldWorks.FeatureStatistics
Dim swFeatMgr  As SldWorks.FeatureManager
Dim swModel As SldWorks.ModelDoc2
Dim featnames As Variant
Dim feattypes As Variant
Dim features As Variant
Dim featureUpdateTimes As Variant
Dim featureUpdatePercentTimes As Variant
Dim iter As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swFeatMgr = swModel.FeatureManager
```

```
    Set swFeatStat = swFeatMgr.FeatureStatistics
```

```
    swFeatStat.Refresh
```

```
    Debug.Print "Model name:                 " & swFeatStat.PartName
    Debug.Print "  Number of features:       " & swFeatStat.FeatureCount
    Debug.Print "  Number of solid bodies:   " & swFeatStat.SolidBodiesCount
    Debug.Print "  Number of surface bodies: " & swFeatStat.SurfaceBodiesCount
    Debug.Print "  Total rebuild time:       " & swFeatStat.TotalRebuildTime
    featnames = swFeatStat.FeatureNames
    feattypes = swFeatStat.FeatureTypes
    features = swFeatStat.features
    featureUpdateTimes = swFeatStat.featureUpdateTimes
    featureUpdatePercentTimes = swFeatStat.FeatureUpdatePercentageTimes
```

```
    If Not (IsEmpty(featnames) Or IsNull(featnames)) Then
        For iter = 0 To UBound(featnames)
            Debug.Print "    Feature name:           " & featnames(iter)
            Debug.Print "    Feature type:           " & feattypes(iter)
            Debug.Print "      Update time:          " & featureUpdateTimes(iter)
            Debug.Print "      Update % time:        " & featureUpdatePercentTimes(iter)
        Next iter
    End If
```

```
End Sub
```
