---
title: "Traverse All Cosmetic Threads Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_All_Cosmetic_Threads_Example_VBNET.htm"
---

# Traverse All Cosmetic Threads Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swFeat As Feature
         Dim swSubFeat As Feature
         Dim sFeatType As String
         Dim swCosThread As CosmeticThreadFeatureData
         Dim bRet As Boolean

         swModel = swApp.ActiveDoc

         bRet = swModel.Extension.SelectByID2("", "EDGE", -0.000802489357837999, -0.0246888176810671, 0.0000600726028778809,  True, 0,  Nothing, 0)
         swFeat = swModel.FeatureManager.InsertCosmeticThread3(swCosmeticStandardType_e.swStandardType_StandardHelicoilMetric, "Helicoil threads", "M33x2.0", 0.033, swCosmeticEndConditions_e.swEndConditionBlind2Dia, 0.025,  "M33x2.0 Helicoil Threads")

         Debug.Print("File = " & swModel.GetPathName)

         swFeat = swModel.FirstFeature

         Do While Not swFeat Is  Nothing
             swSubFeat = swFeat.GetFirstSubFeature
             Do While Not swSubFeat Is Nothing
                 sFeatType = swSubFeat.GetTypeName

                 Select Case sFeatType

                     Case "CosmeticThread"
                         Debug.Print("    " & swSubFeat.Name & " [" & sFeatType & "]")

                         swCosThread = swSubFeat.GetDefinition

                         Debug.Print("      ApplyThread      = " & swCosThread.ApplyThread)
                         Debug.Print("      BlindDepth       = " & swCosThread.BlindDepth * 1000.0# & " mm")
                         Debug.Print("      Diameter         = " & swCosThread.Diameter * 1000.0# & " mm")
                         Debug.Print("      DiameterType     = " & swCosThread.DiameterType)
                         Debug.Print("      ThreadCallout    = " & swCosThread.ThreadCallout)
                         Debug.Print("      ConfigurationOption as defined in swCosmeticConfigOptions_e = " & swCosThread.ConfigurationOption)
                         Debug.Print("      EndCondition as defined in swCosmeticEndConditions_e = " & swCosThread.EndCondition)
                         Debug.Print("      Size = " & swCosThread.Size)
                         Debug.Print("      Standard as defined in swCosmeticStandardType_e = " & swCosThread.Standard)
                         Debug.Print("      StandardType = " & swCosThread.StandardType)

                         Debug.Print("")

                 End Select

                 swSubFeat = swSubFeat.GetNextSubFeature

             Loop

             swFeat = swFeat.GetNextFeature

         Loop

     End Sub

     Public swApp As SldWorks

 End  Class
```
