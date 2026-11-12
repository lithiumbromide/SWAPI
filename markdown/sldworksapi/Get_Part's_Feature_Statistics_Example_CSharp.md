---
title: "Get Part's Feature Statistics Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Part's_Feature_Statistics_Example_CSharp.htm"
---

# Get Part's Feature Statistics Example (C#)

This example shows how to get the statistics of all of the features in a part document.

```
//-------------------------------------------
// Preconditions:
// 1. Open a part that has multiple features.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Gets the statistics for the features in
//    the part.
// 2. Examine the Immediate window.
//-------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace GetFeatureStatisticsForPart_CSharp.csproj
{
    partial
 class SolidWorksMacro
    {
        public
 void Main()
        {
            FeatureStatistics swFeatStat = default(FeatureStatistics);
            FeatureManager swFeatMgr = default(FeatureManager);
            ModelDoc2 swModel = default(ModelDoc2);
            String[] featnames = null;
            Int32[] feattypes = null;
            Object[]
 features = null;
            Double[] featureUpdateTimes = null;
            Double[] featureUpdatePercentTimes = null;
            int iter = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swFeatMgr = swModel.FeatureManager;
            swFeatStat = swFeatMgr.FeatureStatistics;

            swFeatStat.Refresh();

            Debug.Print("Model name: " + swFeatStat.PartName);
            Debug.Print("
 Number of features: " + swFeatStat.FeatureCount);
            Debug.Print("
 Number of solid bodies: " + swFeatStat.SolidBodiesCount);
            Debug.Print("
 Number of surface bodies: " + swFeatStat.SurfaceBodiesCount);
            Debug.Print("
 Total rebuild time: " + swFeatStat.TotalRebuildTime);
            Debug.Print("");
            features
 = (Object[])swFeatStat.Features;
            featnames = (String[])swFeatStat.FeatureNames;
            feattypes = (Int32[])swFeatStat.FeatureTypes;
            featureUpdateTimes = (Double[])swFeatStat.FeatureUpdateTimes;
            featureUpdatePercentTimes = (Double[])swFeatStat.FeatureUpdatePercentageTimes;
            if
 ((featnames != null))
            {
                for
 (iter = 0; iter <= featnames.GetUpperBound(0); iter++)
                {
                    Debug.Print("
 Feature name: " + featnames[iter]);
                    Debug.Print("
 Feature created: " + ((Feature)features[iter]).DateCreated);
                    Debug.Print("
 Feature type as defined in sw_SelectType_e: " + feattypes[iter]);
                    Debug.Print("
 Update time: " + featureUpdateTimes[iter]);
                    Debug.Print("
 Update % time: " + featureUpdatePercentTimes[iter]);
                    Debug.Print("");
                }
            }
        }
        public SldWorks swApp;
    }
}
```
