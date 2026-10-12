---
title: "Get All Sheet Metal Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_All_Sheet_Metal_Feature_Data_Example_CSharp.htm"
---

# Get All Sheet Metal Feature Data Example (C#)

This example shows how to get all of the sheet metal part's feature data.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a sheet metal part.
 // 2. Open the Immediate window.
 //
 // Postconditions: Inspect the Immediate window.
 //---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;
 namespace GetAllSheetMetalFeatureData_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         SelectionMgr swSelMgr;
         Feature swFeat;
         Feature swSubFeat;
         bool bRet;
         int lRet;

         string gaugeTableFile;

         public void Process_CustomBendAllowance(SldWorks swApp, ModelDoc2 swModel, CustomBendAllowance swCustBend)
         {
             Debug.Print("      BendAllowance    = " + swCustBend.BendAllowance * 1000.0 + " mm");
             Debug.Print("      BendDeduction    = " + swCustBend.BendDeduction * 1000.0 + " mm");
             Debug.Print("      BendTableFile    = " + swCustBend.BendTableFile);
             Debug.Print("      KFactor          = " + swCustBend.KFactor);
             Debug.Print("      Type             = " + swCustBend.Type);

         }

         public void Process_SMBaseFlange(SldWorks swApp, ModelDoc2 swModel, Feature swFeat)
         {
             Debug.Print("  +" + swFeat.Name + " [" + swFeat.GetTypeName() + "]");

             BaseFlangeFeatureData swBaseFlange = default(BaseFlangeFeatureData);
             swBaseFlange = (BaseFlangeFeatureData)swFeat.GetDefinition();

             Debug.Print("    BendRadius = " + swBaseFlange.BendRadius * 1000.0 + " mm");

         }

         public void Process_SheetMetal(SldWorks swApp, ModelDoc2 swModel, Feature swFeat)
         {
             Debug.Print("  +" + swFeat.Name + " [" + swFeat.GetTypeName() + "]");

             SheetMetalFeatureData swSheetMetal = default(SheetMetalFeatureData);
             swSheetMetal = (SheetMetalFeatureData)swFeat.GetDefinition();

             CustomBendAllowance swCustBend = default(CustomBendAllowance);
             swCustBend = swSheetMetal.GetCustomBendAllowance();
             Debug.Print("    BendRadius = " + swSheetMetal.BendRadius * 1000.0 + " mm");

             Process_CustomBendAllowance(swApp, swModel, swCustBend);

             lRet = swSheetMetal.GetUseGaugeTable(out bRet, out gaugeTableFile);
             Debug.Print("    Use gauge table? " + bRet);
             Debug.Print("      Error code as defined in swSheetMetalModifierError_e: " + lRet);

         }

         public void Process_SM3dBend(SldWorks swApp, ModelDoc2 swModel, Feature swFeat)
         {
             Debug.Print("  +" + swFeat.Name + " [" + swFeat.GetTypeName() + "]");

             SketchedBendFeatureData swSketchBend = default(SketchedBendFeatureData);
             CustomBendAllowance swCustBend = default(CustomBendAllowance);

             swSketchBend = (SketchedBendFeatureData)swFeat.GetDefinition();
             swCustBend = swSketchBend.GetCustomBendAllowance();

             Debug.Print("    UseDefaultBendAllowance = " + swSketchBend.UseDefaultBendAllowance);
             Debug.Print("    UseDefaultBendRadius = " + swSketchBend.UseDefaultBendRadius);
             Debug.Print("    BendRadius = " + swSketchBend.BendRadius * 1000.0 + " mm");

             Process_CustomBendAllowance(swApp, swModel, swCustBend);

         }

         public void Process_SMMiteredFlange(SldWorks swApp, ModelDoc2 swModel, Feature swFeat)
         {
             Debug.Print("  +" + swFeat.Name + " [" + swFeat.GetTypeName() + "]");

             MiterFlangeFeatureData swMiterFlange = default(MiterFlangeFeatureData);
             swMiterFlange = (MiterFlangeFeatureData)swFeat.GetDefinition();

             Debug.Print("    UseDefaultBendAllowance = " + swMiterFlange.UseDefaultBendAllowance);
             Debug.Print("    UseDefaultBendRadius = " + swMiterFlange.UseDefaultBendRadius);
             Debug.Print("    BendRadius = " + swMiterFlange.BendRadius * 1000.0 + " mm");

         }

         public void Process_Bends(SldWorks swApp, ModelDoc2 swModel, BendsFeatureData swBends)
         {
             CustomBendAllowance swCustBend = default(CustomBendAllowance);
             swCustBend = swBends.GetCustomBendAllowance();

             Debug.Print("    BendRadius                 = " + swBends.BendRadius * 1000.0 + " mm");
             Debug.Print("    UseDefaultBendAllowance    = " + swBends.UseDefaultBendAllowance);
             Debug.Print("    UseDefaultBendRadius       = " + swBends.UseDefaultBendRadius);

             Process_CustomBendAllowance(swApp, swModel, swCustBend);

         }

         public void Process_ProcessBends(SldWorks swApp, ModelDoc2 swModel, Feature swFeat)
         {
             Debug.Print("  +" + swFeat.Name + " [" + swFeat.GetTypeName() + "]");

             BendsFeatureData swBends = default(BendsFeatureData);
             swBends = (BendsFeatureData)swFeat.GetDefinition();

             Process_Bends(swApp, swModel, swBends);

         }

         public void Process_FlattenBends(SldWorks swApp, ModelDoc2 swModel, Feature swFeat)
         {
             Debug.Print("  +" + swFeat.Name + " [" + swFeat.GetTypeName() + "]");

             BendsFeatureData swBends = default(BendsFeatureData);
             swBends = (BendsFeatureData)swFeat.GetDefinition();

             Process_Bends(swApp, swModel, swBends);

         }

         public void Process_EdgeFlange(SldWorks swApp, ModelDoc2 swModel, Feature swFeat)
         {
             Debug.Print("  +" + swFeat.Name + " [" + swFeat.GetTypeName() + "]");

             EdgeFlangeFeatureData swEdgeFlange = default(EdgeFlangeFeatureData);
             swEdgeFlange = (EdgeFlangeFeatureData)swFeat.GetDefinition();

             Debug.Print("    UseDefaultBendRadius = " + swEdgeFlange.UseDefaultBendRadius);
             Debug.Print("    BendRadius = " + swEdgeFlange.BendRadius * 1000.0 + " mm");

         }

         public void Process_FlatPattern(SldWorks swApp, ModelDoc2 swModel, Feature swFeat)
         {
             Debug.Print("  +" + swFeat.Name + " [" + swFeat.GetTypeName() + "]");

             FlatPatternFeatureData swFlatPatt = default(FlatPatternFeatureData);
             swFlatPatt = (FlatPatternFeatureData)swFeat.GetDefinition();

             Debug.Print("      Simplify bends? " + swFlatPatt.SimplifyBends);

         }

         public void Process_Hem(SldWorks swApp, ModelDoc2 swModel, Feature swFeat)
         {
             Debug.Print("  +" + swFeat.Name + " [" + swFeat.GetTypeName() + "]");

             HemFeatureData swHem = default(HemFeatureData);
             CustomBendAllowance swCustBend = default(CustomBendAllowance);

             swHem = (HemFeatureData)swFeat.GetDefinition();
             swCustBend = swHem.GetCustomBendAllowance();

             Debug.Print("    UseDefaultBendAllowance = " + swHem.UseDefaultBendAllowance);
             Debug.Print("    Radius = " + swHem.Radius * 1000.0 +  " mm");

             Process_CustomBendAllowance(swApp, swModel, swCustBend);

         }

         public void Process_Jog(SldWorks swApp, ModelDoc2 swModel, Feature swFeat)
         {
             Debug.Print("  +" + swFeat.Name + " [" + swFeat.GetTypeName() + "]");

             JogFeatureData swJog = default(JogFeatureData);
             CustomBendAllowance swCustBend = default(CustomBendAllowance);

             swJog = (JogFeatureData)swFeat.GetDefinition();
             swCustBend = swJog.GetCustomBendAllowance();

             Debug.Print("    UseDefaultBendAllowance = " + swJog.UseDefaultBendAllowance);
             Debug.Print("    UseDefaultBendRadius = " + swJog.UseDefaultBendRadius);
             Debug.Print("    BendRadius = " + swJog.BendRadius * 1000.0 + " mm");

             Process_CustomBendAllowance(swApp, swModel, swCustBend);

         }

         public void Process_LoftedBend(SldWorks swApp, ModelDoc2 swModel, Feature swFeat)
         {
             Debug.Print("  +" + swFeat.Name + " [" + swFeat.GetTypeName() + "]");

             LoftedBendsFeatureData swLoftBend = default(LoftedBendsFeatureData);
             swLoftBend = (LoftedBendsFeatureData)swFeat.GetDefinition();

         }

         public void Process_Rip(SldWorks swApp, ModelDoc2 swModel, Feature swFeat)
         {
             Debug.Print("  +" + swFeat.Name + " [" + swFeat.GetTypeName() + "]");

             RipFeatureData swRip = default(RipFeatureData);
             swRip = (RipFeatureData)swFeat.GetDefinition();

         }

         public void Process_CornerFeat(SldWorks swApp, ModelDoc2 swModel, Feature swFeat)
         {
             Debug.Print("  +" + swFeat.Name + " [" + swFeat.GetTypeName() + "]");

             ClosedCornerFeatureData swCloseCorner = default(ClosedCornerFeatureData);
             swCloseCorner = (ClosedCornerFeatureData)swFeat.GetDefinition();

         }

         public void Process_OneBend(SldWorks swApp, ModelDoc2 swModel, Feature swFeat)
         {
             Debug.Print("    +" + swFeat.Name + " [" + swFeat.GetTypeName() + "]");

             OneBendFeatureData swOneBend = default(OneBendFeatureData);
             CustomBendAllowance swCustBend = default(CustomBendAllowance);

             swOneBend = (OneBendFeatureData)swFeat.GetDefinition();
             swCustBend = swOneBend.GetCustomBendAllowance();

             Debug.Print("      UseDefaultBendAllowance = " + swOneBend.UseDefaultBendAllowance);
             Debug.Print("      UseDefaultBendRadius = " + swOneBend.UseDefaultBendRadius);

             Process_CustomBendAllowance(swApp, swModel, swCustBend);

         }

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFeat = (Feature)swModel.FirstFeature();

             Debug.Print("File = " + swModel.GetPathName());

             while ((swFeat != null))
             {
                 // Process top-level sheet metal features
                 switch (swFeat.GetTypeName())
                 {
                     case "SMBaseFlange":
                         Process_SMBaseFlange(swApp, swModel, swFeat);

                         break;
                     case "SheetMetal":
                         Process_SheetMetal(swApp, swModel, swFeat);

                         break;
                     case "SM3dBend":
                         Process_SM3dBend(swApp, swModel, swFeat);

                         break;
                     case "SMMiteredFlange":
                         Process_SMMiteredFlange(swApp, swModel, swFeat);

                         break;
                     case "ProcessBends":
                         Process_ProcessBends(swApp, swModel, swFeat);

                         break;
                     case "FlattenBends":
                         Process_FlattenBends(swApp, swModel, swFeat);

                         break;
                     case "EdgeFlange":
                         Process_EdgeFlange(swApp, swModel, swFeat);

                         break;
                     case "FlatPattern":
                         Process_FlatPattern(swApp, swModel, swFeat);

                         break;
                     case "Hem":
                         Process_Hem(swApp, swModel, swFeat);

                         break;
                     case "Jog":
                         Process_Jog(swApp, swModel, swFeat);

                         break;
                     case "LoftedBend":
                         Process_LoftedBend(swApp, swModel, swFeat);

                         break;
                     case "Rip":
                         Process_Rip(swApp, swModel, swFeat);

                         break;
                     case "CornerFeat":
                         Process_CornerFeat(swApp, swModel, swFeat);

                         break;
                     default:
                         break;
                     // Probably not a sheet metal feature

                 }

                 // process sheet metal sub-features
                 swSubFeat = (Feature)swFeat.GetFirstSubFeature();

                 while ((swSubFeat != null))
                 {
                     switch (swSubFeat.GetTypeName())
                     {
                         case "OneBend":
                             Process_OneBend(swApp, swModel, swSubFeat);

                             break;
                         default:
                             break;
                         // Probably not a sheet metal feature
                     }

                     swSubFeat = (Feature)swSubFeat.GetNextSubFeature();
                 }

                 swFeat = (Feature)swFeat.GetNextFeature();

             }

         }

         public SldWorks swApp;

     }

 }
```
