---
title: "Get All Sheet Metal Feature Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_All_Sheet_Metal_Feature_Data_Example_VBNET.htm"
---

# Get All Sheet Metal Feature Data Example (VB.NET)

This example shows how to get all of the sheet metal part's feature data.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a sheet metal part.
 ' 2. Open the Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
 '---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swSelMgr As SelectionMgr
     Dim swFeat As Feature
     Dim swSubFeat As Feature
     Dim bRet As Boolean
     Dim lRet As Integer
     Dim gaugeTableFile As String

     Sub Process_CustomBendAllowance _
     ( _
     ByVal swApp As SldWorks, _
     ByVal swModel As ModelDoc2, _
     ByVal swCustBend As CustomBendAllowance _
     )

         Debug.Print("      BendAllowance    = " & swCustBend.BendAllowance * 1000.0# & " mm")
         Debug.Print("      BendDeduction    = " & swCustBend.BendDeduction * 1000.0# & " mm")
         Debug.Print("      BendTableFile    = " & swCustBend.BendTableFile)
         Debug.Print("      KFactor          = " & swCustBend.KFactor)
         Debug.Print("      Type             = " & swCustBend.Type)

     End Sub

     Sub Process_SMBaseFlange _
     ( _
     ByVal swApp As SldWorks, _
     ByVal swModel As ModelDoc2, _
     ByVal swFeat As Feature _
     )

         Debug.Print("  +" & swFeat.Name & " [" & swFeat.GetTypeName & "]")

         Dim swBaseFlange As BaseFlangeFeatureData
         swBaseFlange = swFeat.GetDefinition

         Debug.Print("    BendRadius = " & swBaseFlange.BendRadius * 1000.0#   " mm")

     End Sub

     Sub Process_SheetMetal _
     ( _
     ByVal swApp As SldWorks, _
     ByVal swModel As ModelDoc2, _
     ByVal swFeat As Feature _
     )

         Debug.Print("  +" & swFeat.Name & " [" & swFeat.GetTypeName & "]")

         Dim swSheetMetal As SheetMetalFeatureData
         swSheetMetal = swFeat.GetDefinition

         Dim swCustBend As CustomBendAllowance
         swCustBend = swSheetMetal.GetCustomBendAllowance
         Debug.Print("    BendRadius = " & swSheetMetal.BendRadius * 1000.0#   " mm")

         Process_CustomBendAllowance(swApp, swModel, swCustBend)

         lRet = swSheetMetal.GetUseGaugeTable(bRet, gaugeTableFile)
         Debug.Print("    Use gauge table? " & bRet)
         Debug.Print("      Error code as defined in swSheetMetalModifierError_e: " & lRet)

     End Sub

     Sub Process_SM3dBend _
     ( _
     ByVal swApp As SldWorks, _
     ByVal swModel As ModelDoc2, _
     ByVal swFeat As Feature _
     )

         Debug.Print("  +" & swFeat.Name & " [" & swFeat.GetTypeName & "]")

         Dim swSketchBend As SketchedBendFeatureData
         Dim swCustBend As CustomBendAllowance

         swSketchBend = swFeat.GetDefinition
         swCustBend = swSketchBend.GetCustomBendAllowance

         Debug.Print("    UseDefaultBendAllowance = " & swSketchBend.UseDefaultBendAllowance)
         Debug.Print("    UseDefaultBendRadius = " & swSketchBend.UseDefaultBendRadius)
         Debug.Print("    BendRadius = " & swSketchBend.BendRadius * 1000.0#   " mm")

         Process_CustomBendAllowance(swApp, swModel, swCustBend)

     End Sub

     Sub Process_SMMiteredFlange _
     ( _
     ByVal swApp As SldWorks, _
     ByVal swModel As ModelDoc2, _
     ByVal swFeat As Feature _
     )

         Debug.Print("  +" & swFeat.Name & " [" & swFeat.GetTypeName & "]")

         Dim swMiterFlange As MiterFlangeFeatureData
         swMiterFlange = swFeat.GetDefinition

         Debug.Print("    UseDefaultBendAllowance = " & swMiterFlange.UseDefaultBendAllowance)
         Debug.Print("    UseDefaultBendRadius = " & swMiterFlange.UseDefaultBendRadius)
         Debug.Print("    BendRadius = " & swMiterFlange.BendRadius * 1000.0#   " mm")

     End Sub

     Sub Process_Bends _
     ( _
     ByVal swApp As SldWorks, _
     ByVal swModel As ModelDoc2, _
     ByVal swBends As BendsFeatureData _
     )

         Dim swCustBend As CustomBendAllowance
         swCustBend = swBends.GetCustomBendAllowance

         Debug.Print("    BendRadius                 = " & swBends.BendRadius * 1000.0# & " mm")
         Debug.Print("    UseDefaultBendAllowance    = " & swBends.UseDefaultBendAllowance)
         Debug.Print("    UseDefaultBendRadius       = " & swBends.UseDefaultBendRadius)

         Process_CustomBendAllowance(swApp, swModel, swCustBend)

     End Sub

     Sub Process_ProcessBends _
     ( _
     ByVal swApp As SldWorks, _
     ByVal swModel As ModelDoc2, _
     ByVal swFeat As Feature _
     )

         Debug.Print("  +" & swFeat.Name & " [" & swFeat.GetTypeName & "]")

         Dim swBends As BendsFeatureData
         swBends = swFeat.GetDefinition

         Process_Bends(swApp, swModel, swBends)

     End Sub

     Sub Process_FlattenBends _
     ( _
     ByVal swApp As SldWorks, _
     ByVal swModel As ModelDoc2, _
     ByVal swFeat As Feature _
     )

         Debug.Print("  +" & swFeat.Name & " [" & swFeat.GetTypeName & "]")

         Dim swBends As BendsFeatureData
         swBends = swFeat.GetDefinition

         Process_Bends(swApp, swModel, swBends)

     End Sub

     Sub Process_EdgeFlange _
     ( _
     ByVal swApp As SldWorks, _
     ByVal swModel As ModelDoc2, _
     ByVal swFeat As Feature _
     )

         Debug.Print("  +" & swFeat.Name & " [" & swFeat.GetTypeName & "]")

         Dim swEdgeFlange As EdgeFlangeFeatureData
         swEdgeFlange = swFeat.GetDefinition

         Debug.Print("    UseDefaultBendRadius = " & swEdgeFlange.UseDefaultBendRadius)
         Debug.Print("    BendRadius = " & swEdgeFlange.BendRadius * 1000.0#   " mm")

     End Sub

     Sub Process_FlatPattern _
     ( _
     ByVal swApp As SldWorks, _
     ByVal swModel As ModelDoc2, _
     ByVal swFeat As Feature _
     )

         Debug.Print("  +" & swFeat.Name & " [" & swFeat.GetTypeName & "]")

         Dim swFlatPatt As FlatPatternFeatureData
         swFlatPatt = swFeat.GetDefinition

         Debug.Print("      Simplify bends? " & swFlatPatt.SimplifyBends)

     End Sub

     Sub Process_Hem _
     ( _
     ByVal swApp As SldWorks, _
     ByVal swModel As ModelDoc2, _
     ByVal swFeat As Feature _
     )

         Debug.Print("  +" & swFeat.Name & " [" & swFeat.GetTypeName & "]")

         Dim swHem As HemFeatureData
         Dim swCustBend As CustomBendAllowance

         swHem = swFeat.GetDefinition
         swCustBend = swHem.GetCustomBendAllowance

         Debug.Print("    UseDefaultBendAllowance = " & swHem.UseDefaultBendAllowance)
         Debug.Print("    Radius = " & swHem.Radius * 1000.0# & " mm")

         Process_CustomBendAllowance(swApp, swModel, swCustBend)

     End Sub

     Sub Process_Jog _
     ( _
     ByVal swApp As SldWorks, _
     ByVal swModel As ModelDoc2, _
     ByVal swFeat As Feature _
     )

         Debug.Print("  +" & swFeat.Name & " [" & swFeat.GetTypeName & "]")

         Dim swJog As JogFeatureData
         Dim swCustBend As CustomBendAllowance

         swJog = swFeat.GetDefinition
         swCustBend = swJog.GetCustomBendAllowance

         Debug.Print("    UseDefaultBendAllowance = " & swJog.UseDefaultBendAllowance)
         Debug.Print("    UseDefaultBendRadius = " & swJog.UseDefaultBendRadius)
         Debug.Print("    BendRadius = " & swJog.BendRadius * 1000.0# & " mm")

         Process_CustomBendAllowance(swApp, swModel, swCustBend)

     End Sub

     Sub Process_LoftedBend _
     ( _
     ByVal swApp As SldWorks, _
     ByVal swModel As ModelDoc2, _
     ByVal swFeat As Feature _
     )

         Debug.Print("  +" & swFeat.Name & " [" & swFeat.GetTypeName & "]")

         Dim swLoftBend As LoftedBendsFeatureData
         swLoftBend = swFeat.GetDefinition

     End Sub

     Sub Process_Rip _
     ( _
     ByVal swApp As SldWorks, _
     ByVal swModel As ModelDoc2, _
     ByVal swFeat As Feature _
     )

         Debug.Print("  +" & swFeat.Name & " [" & swFeat.GetTypeName & "]")

         Dim swRip As RipFeatureData
         swRip = swFeat.GetDefinition

     End Sub

     Sub Process_CornerFeat _
     ( _
     ByVal swApp As SldWorks, _
     ByVal swModel As ModelDoc2, _
     ByVal swFeat As Feature _
     )

         Debug.Print("  +" & swFeat.Name & " [" & swFeat.GetTypeName & "]")

         Dim swCloseCorner As ClosedCornerFeatureData
         swCloseCorner = swFeat.GetDefinition

     End Sub

     Sub Process_OneBend _
     ( _
     ByVal swApp As SldWorks, _
     ByVal swModel As ModelDoc2, _
     ByVal swFeat As Feature _
     )

         Debug.Print("    +" & swFeat.Name & " [" & swFeat.GetTypeName & "]")

         Dim swOneBend As OneBendFeatureData
         Dim swCustBend As CustomBendAllowance

         swOneBend = swFeat.GetDefinition
         swCustBend = swOneBend.GetCustomBendAllowance

         Debug.Print("      UseDefaultBendAllowance = " & swOneBend.UseDefaultBendAllowance)
         Debug.Print("      UseDefaultBendRadius = " & swOneBend.UseDefaultBendRadius)

         Process_CustomBendAllowance(swApp, swModel, swCustBend)

     End Sub

     Sub main()

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swFeat = swModel.FirstFeature

         Debug.Print("File = " & swModel.GetPathName)

         Do While Not swFeat Is  Nothing
             ' Process top-level sheet metal features
             Select Case swFeat.GetTypeName
                 Case "SMBaseFlange"
                     Process_SMBaseFlange(swApp, swModel, swFeat)

                 Case "SheetMetal"
                     Process_SheetMetal(swApp, swModel, swFeat)

                 Case "SM3dBend"
                     Process_SM3dBend(swApp, swModel, swFeat)

                 Case "SMMiteredFlange"
                     Process_SMMiteredFlange(swApp, swModel, swFeat)

                 Case "ProcessBends"
                     Process_ProcessBends(swApp, swModel, swFeat)

                 Case "FlattenBends"
                     Process_FlattenBends(swApp, swModel, swFeat)

                 Case "EdgeFlange"
                     Process_EdgeFlange(swApp, swModel, swFeat)

                 Case "FlatPattern"
                     Process_FlatPattern(swApp, swModel, swFeat)

                 Case "Hem"
                     Process_Hem(swApp, swModel, swFeat)

                 Case "Jog"
                     Process_Jog(swApp, swModel, swFeat)

                 Case "LoftedBend"
                     Process_LoftedBend(swApp, swModel, swFeat)

                 Case "Rip"
                     Process_Rip(swApp, swModel, swFeat)

                 Case "CornerFeat"
                     Process_CornerFeat(swApp, swModel, swFeat)

                 Case Else
                     ' Probably not a sheet metal feature

             End Select

             ' process sheet metal sub-features
             swSubFeat = swFeat.GetFirstSubFeature

             Do While Not swSubFeat Is Nothing
                 Select Case swSubFeat.GetTypeName
                     Case "OneBend"
                         Process_OneBend(swApp, swModel, swSubFeat)

                     Case Else
                         ' Probably not a sheet metal feature
                 End Select

                 swSubFeat = swSubFeat.GetNextSubFeature()
             Loop

             swFeat = swFeat.GetNextFeature

         Loop

     End Sub

     Public swApp As SldWorks

 End  Class
```
