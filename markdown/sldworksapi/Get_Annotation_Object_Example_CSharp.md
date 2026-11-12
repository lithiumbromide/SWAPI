---
title: "Get Annotation Object Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Annotation_Object_Example_CSharp.htm"
---

# Get Annotation Object Example (C#)

This example shows how to obtain the annotation object for the selected annotation symbol.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a model document that contains an annotation symbol.
 // 2. Select the annotation symbol.
 //
 // Postconditions: The annotation object for the selected symbol is obtained.
 // ---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace GetAnnotationObject_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         SelectionMgr SelMgr;
         object AnnoObject;
         WeldSymbol aWeldSymbol;
         WeldBead aWeldBead;
         TableAnnotation aTableAnno;
         SFSymbol anSFSymbol;
         RevisionCloud aRevisionCloud;
         Note aNote;
         MultiJogLeader aLeader;
         Gtol aGtol;
         DowelSymbol aDowelSym;
         DisplayDimension aDispDim;
         DatumTargetSym aDatTarSym;
         DatumTag aDatumTag;
         DatumOrigin aDatumOrigin;
         CustomSymbol aCustomSymbol;
         CenterMark aCenterMark;
         CenterLine aCenterLine;
         CThread aCThread;

         Annotation Anno;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             SelMgr = (SelectionMgr)Part.SelectionManager;
             AnnoObject = SelMgr.GetSelectedObject6(1, -1);

             switch (SelMgr.GetSelectedObjectType3(1, -1))
             {
                 case (int)swSelectType_e.swSelWELDS:
                     Debug.Print("Selected annotation is a WeldSymbol.");
                     aWeldSymbol = (WeldSymbol)AnnoObject;
                     Anno = (Annotation)aWeldSymbol.GetAnnotation();
                     break;
                 case (int)swSelectType_e.swSelWELDBEADS:
                     Debug.Print("Selected annotation is a WeldBead.");
                     aWeldBead = (WeldBead)AnnoObject;
                     Anno = (Annotation)aWeldBead.GetAnnotation();
                     break;
                 case (int)swSelectType_e.swSelANNOTATIONTABLES:
                     Debug.Print("Selected annotation is a TableAnnotation.");
                     aTableAnno = (TableAnnotation)AnnoObject;
                     Anno = (Annotation)aTableAnno.GetAnnotation();
                     break;
                 case (int)swSelectType_e.swSelSFSYMBOLS:
                     Debug.Print("Selected annotation is an SFSymbol.");
                     anSFSymbol = (SFSymbol)AnnoObject;
                     Anno = (Annotation)anSFSymbol.GetAnnotation();
                     break;
                 case (int)swSelectType_e.swSelREVISIONCLOUDS:
                     Debug.Print("Selected annotation is a RevisionCloud.");
                     aRevisionCloud = (RevisionCloud)AnnoObject;
                     Anno = (Annotation)aRevisionCloud.GetAnnotation();
                     break;
                 case (int)swSelectType_e.swSelNOTES:
                     Debug.Print("Selected annotation is a Note.");
                     aNote = (Note)AnnoObject;
                     Anno = (Annotation)aNote.GetAnnotation();
                     break;
                 case (int)swSelectType_e.swSelLEADERS:
                     Debug.Print("Selected annotation is a Leader.");
                     aLeader = (MultiJogLeader)AnnoObject;
                     Anno = (Annotation)aLeader.GetAnnotation();
                     break;
                 case (int)swSelectType_e.swSelGTOLS:
                     Debug.Print("Selected annotation is a Gtol.");
                     aGtol = (Gtol)AnnoObject;
                     Anno = (Annotation)aGtol.GetAnnotation();
                     break;
                 case (int)swSelectType_e.swSelDOWELSYMS:
                     Debug.Print("Selected annotation is a DowelSymbol.");
                     aDowelSym = (DowelSymbol)AnnoObject;
                     Anno = (Annotation)aDowelSym.GetAnnotation();
                     break;
                 case (int)swSelectType_e.swSelDIMENSIONS:
                     Debug.Print("Selected annotation is a DisplayDimension.");
                     aDispDim = (DisplayDimension)AnnoObject;
                     Anno = (Annotation)aDispDim.GetAnnotation();
                     break;
                 case (int)swSelectType_e.swSelDTMTARGS:
                     Debug.Print("Selected annotation is a DatumTargetSym.");
                     aDatTarSym = (DatumTargetSym)AnnoObject;
                     Anno = (Annotation)aDatTarSym.GetAnnotation();
                     break;
                 case (int)swSelectType_e.swSelDATUMTAGS:
                     Debug.Print("Selected annotation is a DatumTag.");
                     aDatumTag = (DatumTag)AnnoObject;
                     Anno = (Annotation)aDatumTag.GetAnnotation();
                     break;
                 case (int)swSelectType_e.swSelDATUMPOINTS:
                     Debug.Print("Selected annotation is a DatumOrigin.");
                     aDatumOrigin = (DatumOrigin)AnnoObject;
                     Anno = (Annotation)aDatumOrigin.GetAnnotation();
                     break;
                 case (int)swSelectType_e.swSelCUSTOMSYMBOLS:
                     Debug.Print("Selected annotation is a CustomSymbol.");
                     aCustomSymbol = (CustomSymbol)AnnoObject;
                     Anno = (Annotation)aCustomSymbol.GetAnnotation();
                     break;
                 case (int)swSelectType_e.swSelCTHREADS:
                     Debug.Print("Selected annotation is a CThread.");
                     aCThread = (CThread)AnnoObject;
                     Anno = (Annotation)aCThread.GetAnnotation();
                     break;
                 case (int)swSelectType_e.swSelCENTERMARKSYMS:
                     Debug.Print("Selected annotation is a CenterMark.");
                     aCenterMark = (CenterMark)AnnoObject;
                     Anno = (Annotation)aCenterMark.GetAnnotation();
                     break;
                 case (int)swSelectType_e.swSelCENTERLINES:
                     Debug.Print("Selected annotation is a CenterLine.");
                     aCenterLine = (CenterLine)AnnoObject;
                     Anno = (Annotation)aCenterLine.GetAnnotation();
                     break;
             }

             Debug.Print("Annotation: " + Anno.GetName());

         }

         public SldWorks swApp;

     }

 }
```
