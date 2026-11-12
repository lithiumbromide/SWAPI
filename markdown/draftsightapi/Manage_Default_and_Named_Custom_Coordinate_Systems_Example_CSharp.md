---
title: "Manage Custom Coordinate Systems Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Manage_Default_and_Named_Custom_Coordinate_Systems_Example_CSharp.htm"
---

# Manage Custom Coordinate Systems Example (C#)

This example shows how to manage World, default, and named custom coordinate systems.

```vb
 //--------------------------------------------------------------------------
 //Preconditions:
 // 1. Create a C# Windows console project.
 // 2. Copy and paste this project into the C# IDE.
 // 3. Add a reference to:
 //    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.
 // 4. Add references to System and System.Windows.Forms.
 // 5. Start DraftSight.
 // 6. Set a breakpoint in Main() and step through the macro.
 //
 //Postconditions:
 //1. Inspect the Immediate Window.
 //2. A new named custom coordinate system is created, renamed, and removed.
 //--------------------------------------------------------------------------
 using System;
 using System.Collections.Generic;
 using System.Text;
 using DraftSight;
 using System.Windows.Forms;
 using System.Runtime.InteropServices;
 using System.Diagnostics;

 namespace CCSUsage
 {
     class Program
     {
         private static DraftSight.Application dsApp;
         private static Document dsDoc;

         static void Main(string[] args)
         {
             //Connect to DraftSight application
             dsApp = ConnectToDraftSight();
             if (null == dsApp)
             {
                 return;
             }

             dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands

             //Create new document
             dsDoc = dsApp.NewDocument("standard.dwt");
             if (null == dsDoc)
             {
                 MessageBox.Show("Failed to create a new document in DraftSight.");
                 return;
             }

             //Get custom coordinate system manager
             CustomCoordinateSystemManager dsCCSMgr = dsDoc.GetCustomCoordinateSystemManager();

             UsageOfDefaultCustomCoordinateSystems(dsCCSMgr);

             UsageOfNamedCustomCoordinateSystems(dsCCSMgr);
         }

         private static void UsageOfDefaultCustomCoordinateSystems(CustomCoordinateSystemManager dsCCSMgr)
         {
             //Get World Coordinate System
             CustomCoordinateSystem dsWorldCCS = dsCCSMgr.GetWorldCustomCoordinateSystem();

             Debug.Print(Environment.NewLine + "Get World CCS.");

             PrintCoordinateSystemParameters(dsWorldCCS);

             //Get default bottom custom coordinate system
             CustomCoordinateSystem dsBottomCCS = dsCCSMgr.GetDefaultCustomCoordinateSystem(dsDefaultCustomCoordinateSystem_e.dsDefaultCustomCoordinateSystem_Bottom);

             Debug.Print(Environment.NewLine + "Get default Bottom CCS.");

             PrintCoordinateSystemParameters(dsBottomCCS);

             //Activate default bottom custom coordinate system
             dsBottomCCS.Activate();

             //Get previous CCS; it should be WCS.
             CustomCoordinateSystem dsPreviousCCS = dsCCSMgr.GetPreviousCustomCoordinateSystem();

             Debug.Print(Environment.NewLine + "Get previous CCS.");

             PrintCoordinateSystemParameters(dsPreviousCCS);

             //Get active CCS; it should be bottom CCS
             CustomCoordinateSystem dsActiveCCS = dsCCSMgr.GetActiveCustomCoordinateSystem();

             Debug.Print(Environment.NewLine + "Get active CCS.");

             PrintCoordinateSystemParameters(dsActiveCCS);

             //The active custom coordinate system can be modified
             //Change origin of active custom coordinate system
             double originX = 2;
             double originY = 3;
             double originZ = 1;
             dsCCSMgr.SetActiveCustomCoordinateSystemOrigin(originX, originY, originZ);

             Debug.Print(Environment.NewLine + "Origin of active CCS has been changed.");

             PrintCoordinateSystemParameters(dsActiveCCS);

             //Align custom coordinate system by entity
             AlignActiveCCSByEntity(dsCCSMgr);

             Debug.Print(Environment.NewLine + "The active CCS has been aligned by line entity.");

             PrintCoordinateSystemParameters(dsActiveCCS);
         }

         private static void AlignActiveCCSByEntity(CustomCoordinateSystemManager dsCCSMgr)
         {
             //Get model space
             Model dsModel = dsDoc.GetModel();

             //Get sketch manager
             SketchManager dsSketchMgr = dsModel.GetSketchManager();

             //Draw a line entity
             double[] startPoint = { 5, 5, 0 };
             double[] endPoint = { 12, 15, 0 };
             Line dsLine = dsSketchMgr.InsertLine(startPoint[0], startPoint[1], startPoint[2],
                                                  endPoint[0], endPoint[1], endPoint[2]);

             //Align active CCS by the created line entity
             dsCCSMgr.AlignActiveCustomCoordinateSystemByEntity(dsLine, startPoint);
         }

         private static void UsageOfNamedCustomCoordinateSystems(CustomCoordinateSystemManager dsCCSMgr)
         {
             //Get view manager
             ViewManager dsViewManager = dsDoc.GetViewManager();

             //Set isometric view
             dsViewManager.SetPredefinedView(dsPredefinedView_e.dsPredefinedView_SWIsometric);

             //Zoom extents
             dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);

             //Create a new named CCS by saving the active view as new CCS
             string name = "newCCS";
             CustomCoordinateSystem dsNewCCS;
             dsCreateObjectResult_e saveViewResult = dsCCSMgr.SaveActiveViewAs(name,  out dsNewCCS);
             if (null != dsNewCCS && dsCreateObjectResult_e.dsCreateObjectResult_Success == saveViewResult)
             {
                 Debug.Print(Environment.NewLine + "New named CCS has been created by saving active view as new CCS.");

                 PrintCoordinateSystemParameters(dsNewCCS);

                 //Rename new CCS
                 string newName = name + "_Changed";
                 if (RenameCCS(dsNewCCS, newName))
                 {
                     Debug.Print(Environment.NewLine + "The CCS has been renamed.");

                     PrintCoordinateSystemParameters(dsNewCCS);

                     //Print named CCS list
                     PrintNamedCCSList(dsCCSMgr);

                     //Remove the created CCS
                     dsCCSMgr.RemoveCustomCoordinateSystem(newName);

                     //Print named CCS list
                     PrintNamedCCSList(dsCCSMgr);
                 }
             }
             else
             {
                 MessageBox.Show(string.Format("Failed to save the active view as new \"{0}\" custom coordinate system.", name));
             }
         }

         private static void PrintNamedCCSList(CustomCoordinateSystemManager dsCCSMgr)
         {
             string[] namedCCS = (string[])dsCCSMgr.GetNamedCustomCoordinateSystemList();
             if (null == namedCCS)
             {
                 Debug.Print(Environment.NewLine + "There are no named custom coordinate systems in the current document.");
             }
             else
             {
                 Debug.Print(Environment.NewLine + "Named custom coordinate systems:");

                 foreach (string  name in namedCCS)
                 {
                     Debug.Print(name);
                 }
             }
         }

         private static bool RenameCCS(CustomCoordinateSystem dsNewCCS, string newName)
         {
             dsCreateObjectResult_e renameResult = dsNewCCS.Rename(newName);
             if (dsCreateObjectResult_e.dsCreateObjectResult_Success != renameResult)
             {
                 MessageBox.Show(string.Format("Failed to rename custom coordinate system. New name should be {0}. Renaming result: {1}.", newName, renameResult.ToString()));

                 return false;
             }

             return true;
         }

         private static void PrintCoordinateSystemParameters(CustomCoordinateSystem dsCustomCoordinateSystem)
         {
             Debug.Print(Environment.NewLine + "Custom Coordinate System Parameters:");

             Debug.Print("Name = " + dsCustomCoordinateSystem.GetName());

             bool isDefault;
             dsDefaultCustomCoordinateSystem_e defaultFlag;
             dsCustomCoordinateSystem.GetDefaultCustomCoordinateSystemFlag(out isDefault, out defaultFlag);
             Debug.Print("IsDefault = " + isDefault.ToString());
             Debug.Print("DefaultCustomCoordinateSystemFlag = " + defaultFlag.ToString());

             double x, y, z;
             dsCustomCoordinateSystem.GetOrigin(out x, out y, out z);
             Debug.Print(string.Format("Origin ({0},{1},{2})", x, y, z));

             dsCustomCoordinateSystem.GetXAxisDirection(out x, out y, out z);
             Debug.Print(string.Format("XAxisDirection ({0},{1},{2})", x, y, z));

             dsCustomCoordinateSystem.GetYAxisDirection(out x, out y, out z);
             Debug.Print(string.Format("YAxisDirection ({0},{1},{2})", x, y, z));

             dsCustomCoordinateSystem.GetZAxisDirection(out x, out y, out z);
             Debug.Print(string.Format("ZAxisDirection ({0},{1},{2})", x, y, z));
         }

         private static DraftSight.Application ConnectToDraftSight()
         {
             DraftSight.Application dsApp = null;

             try
             {
                 //Connect to DraftSight
                 dsApp = (DraftSight.Application)Marshal.GetActiveObject("DraftSight.Application");
             }
             catch (Exception ex)
             {
                 MessageBox.Show("Failed to connect to DraftSight. Cause: " + ex.Message);
                 dsApp = null;
             }

             return dsApp;
         }
     }
 }
```
