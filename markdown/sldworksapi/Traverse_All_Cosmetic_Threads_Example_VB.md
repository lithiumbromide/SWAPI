---
title: "Traverse All Cosmetic Threads Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_All_Cosmetic_Threads_Example_VB.htm"
---

# Traverse All Cosmetic Threads Example (VBA)

This example shows how to traverse all cosmetic threads in a part and extract their data.

**NOTE**: In a part or assembly, a cosmetic thread is a subfeature of a hole or cut extrusion. Thus, you can traverse all of the cosmetic threads in a model using the IFeature traversal methods.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\holecube.sldprt.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a Helicoil Metric standard cosmetic thread.
 ' 2. Examine the Immediate window.
 '
 ' NOTE: Because the part is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                                   As SldWorks.SldWorks
     Dim swModel                                 As SldWorks.ModelDoc2
     Dim swFeat                                  As SldWorks.Feature
     Dim swSubFeat                               As SldWorks.Feature
     Dim sFeatType                               As String
     Dim swCosThread                             As SldWorks.CosmeticThreadFeatureData
     Dim bRet                                    As Boolean
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc

    bRet = swModel.Extension.SelectByID2("", "EDGE", -8.02489357837999E-04, -2.46888176810671E-02, 6.00726028778809E-05, True, 0, Nothing, 0)
     Set swFeat = swModel.FeatureManager.InsertCosmeticThread3(swStandardType_StandardHelicoilMetric, "Helicoil threads", "M33x2.0", 0.033, swEndConditionBlind2Dia, 0.025, "M33x2.0 Helicoil Threads")
    Debug.Print "File = " & swModel.GetPathName
    Set swFeat = swModel.FirstFeature
    Do While Not swFeat Is Nothing
         Set swSubFeat = swFeat.GetFirstSubFeature
         Do While Not swSubFeat Is Nothing
             sFeatType = swSubFeat.GetTypeName
            Select Case sFeatType
                Case "CosmeticThread"
                     Debug.Print "    " & swSubFeat.Name & " [" & sFeatType & "]"
                    Set swCosThread = swSubFeat.GetDefinition
                    Debug.Print "      ApplyThread      = " & swCosThread.ApplyThread
                     Debug.Print "      BlindDepth       = " & swCosThread.BlindDepth * 1000# & " mm"
                     Debug.Print "      Diameter         = " & swCosThread.Diameter * 1000# & " mm"
                     Debug.Print "      DiameterType     = " & swCosThread.DiameterType
                     Debug.Print "      ThreadCallout    = " & swCosThread.ThreadCallout
                     Debug.Print "      ConfigurationOption as defined in swCosmeticConfigOptions_e = " & swCosThread.ConfigurationOption
                     Debug.Print "      EndCondition as defined in swCosmeticEndConditions_e = " & swCosThread.EndCondition
                     Debug.Print "      Size = " & swCosThread.Size
                     Debug.Print "      Standard as defined in swCosmeticStandardType_e = " & swCosThread.Standard
                     Debug.Print "      StandardType = " & swCosThread.StandardType

                    Debug.Print ""
            End Select
            Set swSubFeat = swSubFeat.GetNextSubFeature
        Loop
        Set swFeat = swFeat.GetNextFeature
    Loop
End Sub
```
