---
title: "Get Part's Feature Statistics Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Part's_Feature_Statistics_Example_VBNET.htm"
---

# Get Part's Feature Statistics Example (VB.NET)

This example shows how to get the statistics of all of the features in a part document.

```vb
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
Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public Sub main()

         Dim swFeatStat As FeatureStatistics
         Dim swFeatMgr As FeatureManager
         Dim swModel As ModelDoc2
         Dim featnames As Object
         Dim feattypes As Object
         Dim features As Object
         Dim featureUpdateTimes As Object
         Dim featureUpdatePercentTimes As Object
         Dim iter As Integer

         swModel = swApp.ActiveDoc
         swFeatMgr = swModel.FeatureManager

         swFeatStat = swFeatMgr.FeatureStatistics

         swFeatStat.Refresh()

         Debug.Print("Model name:                 " & swFeatStat.PartName)
         Debug.Print("  Number of features:       " & swFeatStat.FeatureCount)
         Debug.Print("  Number of solid bodies:   " & swFeatStat.SolidBodiesCount)
         Debug.Print("  Number of surface bodies: " & swFeatStat.SurfaceBodiesCount)
         Debug.Print("  Total rebuild time:       " & swFeatStat.TotalRebuildTime)
         featnames = swFeatStat.FeatureNames
         feattypes = swFeatStat.FeatureTypes
         features = swFeatStat.features
         featureUpdateTimes = swFeatStat.featureUpdateTimes
         featureUpdatePercentTimes = swFeatStat.FeatureUpdatePercentageTimes
         If Not featnames Is Nothing Then
             For iter = 0 To UBound(featnames)
                 Debug.Print("    Feature name:           " & featnames(iter))
                 Debug.Print("    Feature type:           " & feattypes(iter))
                 Debug.Print("      Update time:          " & featureUpdateTimes(iter))
                 Debug.Print("      Update % time:        " & featureUpdatePercentTimes(iter))
             Next iter
         End If

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
