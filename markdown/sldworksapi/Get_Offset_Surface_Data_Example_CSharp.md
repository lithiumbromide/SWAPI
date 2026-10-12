---
title: "Get Offset Surface Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Offset_Surface_Data_Example_CSharp.htm"
---

# Get Offset Surface Data Example (C#)

This example shows how to get data for an offset surface.

//----------------------------------------------------------------------
// Preconditions:
// 1. Open an assembly document that contains a component that
// has a surface offset feature.
// 2. Select the component's surface offset feature.
// 3. Open the Immediate window.
//
// Postconditions: Inspect the Immediate window.
//----------------------------------------------------------------------

```vb
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace AnalyzeOffsetSurface_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             SelectData swSelData = default(SelectData);
             SurfaceOffsetFeatureData swOffset = default(SurfaceOffsetFeatureData);
             Feature swFeat = default(Feature);
             Entity swEnt = default(Entity);
             object[] vFace = null;
             int i = 0;
             bool bRet = false;
             Component2 comp = default(Component2);
             Component2 swCompFace = default(Component2);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swSelData = (SelectData)swSelMgr.CreateSelectData();
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swOffset = (SurfaceOffsetFeatureData)swFeat.GetDefinition();
             comp = (Component2)swSelMgr.GetSelectedObjectsComponent3(1, -1);

             Debug.Print("File = " + swModel.GetPathName());
             Debug.Print("CompFeature = " + comp.Name2);
             Debug.Print("  " + swFeat.Name);
             Debug.Print("    Distance       = " + swOffset.Distance * 1000.0 + " mm");
             Debug.Print("    Flip           = " + swOffset.Flip);
             Debug.Print("    FacesCount     = " + swOffset.GetEntitiesCount());

             bRet = swOffset.AccessSelections(swModel, comp);

             swModel.ClearSelection2(true);

             vFace = (object[])swOffset.Entities;

             for (i = 0; i <= vFace.GetUpperBound(0); i++)
             {
                 swEnt = (Entity)vFace[i];
                                  Debug.Print(" Entity selected = " + swEnt.Select4(true, null));

                 swCompFace = (Component2)swEnt.GetComponent();
                 Debug.Print("    Component face = " + swCompFace.Name2);

             }

             swOffset.ReleaseSelectionAccess();

         }

         public SldWorks swApp;

     }
 }
```
