---
title: "Get Display State Settings Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Display_State_Settings_CSharp.htm"
---

# Get Display State Settings Example (C#)

This example shows how to get display modes, transparency states, and visibility states of components.

```vb
 //------------------------------------------------------------------------------
 // Preconditions: Open an assembly that contains a minimum of three top-level
 // components and two display states, "DS_1" and "DS_2".
 //
 // Postconditions: Inspect the Immediate Window for the display modes,
 // transparency states, and visibility states of all three components
 // in both DS_1 and DS_2.
 //-----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace GetDisplayMode.csproj
 {
     public partial class SolidWorksMacro
     {
         ModelDoc2 swDoc = null;
         ModelDocExtension swExt = null;
         DisplayStateSetting swDSS = null;
         object varStatus;
         object varTStatus;
         object varVStatus;
         Array statusArray;
         Array statusTArray;
         Array statusVArray;
         const int maxEntMode = 3;

         public void Main()
         {
             swDoc = (ModelDoc2)(swApp.ActiveDoc);
             swExt = swDoc.Extension;
             int docType = swDoc.GetType();
             if (docType == (int)swDocumentTypes_e.swDocASSEMBLY)
             {
                 CreateDisplayStateSetting();

                 varStatus = swExt.get_DisplayMode(swDSS);
                 statusArray = (Array)varStatus;

                 varTStatus = swExt.get_Transparency(swDSS);
                 statusTArray = (Array)varTStatus;

                 varVStatus = swExt.get_Visibility(swDSS);
                 statusVArray = (Array)varVStatus;

                 WriteOutput();
             }
         }

         public void CreateDisplayStateSetting()
         {
             swDSS = swExt.GetDisplayStateSetting((int)swDisplayStateOpts_e.swThisDisplayState);
             swDSS.Option = (int)swDisplayStateOpts_e.swSpecifyDisplayState;

             string[] specDSNames = new string[2];
             specDSNames[0] = "DS_1";
             specDSNames[1] = "DS_2";
             object varSpecDSNames = specDSNames;
             swDSS.Names = varSpecDSNames;

             AssemblyDoc swADoc;
             swADoc = (AssemblyDoc)swDoc;
             int compCnt = swADoc.GetComponentCount(true);
             Component2[] listComp = new Component2[maxEntMode];
             if (compCnt >= maxEntMode)
             {
                 object[] varComp = (object[])(swADoc.GetComponents(true));
                 listComp[0] = (Component2)varComp[0];
                 listComp[1] = (Component2)varComp[1];
                 listComp[2] = (Component2)varComp[2];
                 swDSS.Entities = listComp;
             }

         }

         public void WriteOutput()
         {
             int entCount = swDSS.GetEntityCount();
             object[] listComp = (object[])swDSS.Entities;
             int allCtr = 0;
             for (int entctr = 0; entctr < entCount; ++entctr)
             {
                 Component2 swComp = (Component2)listComp[entctr];
                 Debug.Print(swComp.Name2);
                 int dsNameCount = swDSS.GetNameCount();
                 object[] dsNames = (object[])swDSS.Names;

                 for (int namectr = 0; namectr < dsNameCount; ++namectr)
                 {
                     Debug.Print("   " + (string)dsNames[namectr]);
                     int status = (int)statusArray.GetValue(allCtr);
                     int statusT = (int)statusTArray.GetValue(allCtr);
                     int statusV = (int)statusVArray.GetValue(allCtr);
                     WriteMode(status);
                     WriteTransparency(statusT);
                     WriteVisibility(statusV);
                     ++allCtr;
                 }
             }
         }
         public void WriteMode(int status)
         {
             switch (status)
             {
                 case (int)swDisplayMode_e.swDisplayModeDEFAULT:
                     Debug.Print("       swDisplayModeDEFAULT");
                     break;
                 case (int)swDisplayMode_e.swHIDDEN:
                     Debug.Print("       swHIDDEN");
                     break;
                 case (int)swDisplayMode_e.swHIDDEN_GREYED:
                     Debug.Print("       swHIDDEN_GREYED");
                     break;
                 case (int)swDisplayMode_e.swSHADED:
                     Debug.Print("       swSHADED");
                     break;
                 case (int)swDisplayMode_e.swSHADED_EDGES:
                     Debug.Print("       swSHADED_EDGES");
                     break;
                 case (int)swDisplayMode_e.swWIREFRAME:
                     Debug.Print("       swWIREFRAME");
                     break;
                 case (int)swDisplayMode_e.swDisplayModeUNKNOWN:
                     Debug.Print("       Error:swDisplayModeUNKNOWN");
                     break;
                 Case CInt(swDisplayMode_e.swFACETED_WIREFRAME)
                     Debug.Print ("       swFACETED_WIREFRAME")
                     break;
                Case CInt(swDisplayMode_e.swFACETED_HIDDEN_GREYED)
                     Debug.Print ("       swFACETED_HIDDEN_GREYED")
                     break;
                Case CInt(swDisplayMode_e.swFACETED_HIDDEN)
                     Debug.Print ("       swFACETED_HIDDEN")
                     break;

             }
         }
         public void WriteTransparency(int status)
         {
             switch (status)
             {
                 case (int)swTransparencyState_e.swTransparencyStateTransparent:
                     Debug.Print("       swTransparencyStateTransparent");
                     break;
                 case (int)swTransparencyState_e.swTransparencyStateNonTransparent:
                     Debug.Print("       swTransparencyStateNonTransparent");
                     break;
                 case (int)swTransparencyState_e.swTransparencyStateUnknown:
                     Debug.Print("       ERROR : swTransparencyStateUnknown");
                     break;
             }
         }
         public void WriteVisibility(int status)
         {
             switch (status)
             {
                 case (int)swVisibilityState_e.swVisibilityStateHide:
                     Debug.Print("       swVisibilityStateHide");
                     break;
                 case (int)swVisibilityState_e.swVisibilityStateShown:
                     Debug.Print("       swVisibilityStateShown");
                     break;
                 case (int)swVisibilityState_e.swVisibilityStateUnknown:
                     Debug.Print("       ERROR : swVisibilityStateUnknown");
                     break;
             }
         }

         public SldWorks swApp;
     }
 }
```
