---
title: "Creating Flat Representations of 3D Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Creating_Flat_Representations_of_3D_Entities_Example_CSharp.htm"
---

# Creating Flat Representations of 3D Entities Example (C#)

This example shows how to flatten 3D entities.

//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
// `install_dir`\**APISDK\tlb\DraftSight.Interop.dsAutomation.dll**
// 4. Add references to **System** and **System.Windows.Forms**.
// 5. Start DraftSight.
// 6. Press F5 to debug the project.
//
// Postconditions:
// 1. Extrudes a 3D entity.
// 2. Creates a block with a flat representation of the 3D entity.
// 3. Creates a new block, Test, containing a circle.
// 4. Replaces the Test block with a flat representation
// of the 3D entity.
// 5. Exports to `mainpath`**\newFile.dwg** a flat representation of the
// 3D entity.
//----------------------------------------------------------------

```vb
 using System;
 using System.IO;
 using System.Text.RegularExpressions;
 using System.Reflection;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using DraftSight.Interop.dsAutomation;
 using System.Runtime.InteropServices;
 using System.Windows.Forms;

 namespace FlatteningEntitiesConsoleApp1
 {
       class  Program
      {
            static  void Main(string[] args)
           {
               //Connect to DraftSight application
              DraftSight.Interop.dsAutomation.Application application = ConnectToDraftSight();
               if (null == application)
              {
                   return;
              }

              application.AbortRunningCommand();   // abort any command currently running in DraftSight to avoid nested commands

               string appPath = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);

              String[] extract = Regex.Split(appPath,  "bin");
              String mainPath = extract[0].TrimEnd('\\');

              Document dsDoc = application.GetActiveDocument();

               if (null == dsDoc)
              {
                   return;
              }

              Model dsModel = dsDoc.GetModel();
               if (null == dsModel)
              {
                   return;
              }

              SketchManager dsSketchManager = dsModel.GetSketchManager();
               if (null == dsSketchManager)
              {
                   return;
              }

              PolyLine dsPolyline;
              {
                  dsPolyline = dsSketchManager.InsertPolyline2D(
                    new  double[] { 128.253, 166.459, 128.253, 43.84, 307.848, 43.84, 307.848, 166.459 },
                    true);
              }

              DispatchWrapper[] dsEntities1 =   new DispatchWrapper[1];
              dsEntities1[0] =   new DispatchWrapper(dsPolyline);

               // Extrude entities to solid by height
              Object extrudes =   null;
              dsSketchManager.ExtrudeEntitiesToSolidByHeight(dsEntities1, 20, 0,  out extrudes);

               // Flat shot and insert as block
              dsSketchManager.FlatShotByInsertAsBlock(2.0, 22.0, 0.0, 1.0, 1.0, 1.0, 0.0);

              Circle dsCircle;
              {
                  dsCircle = dsSketchManager.InsertCircle(23.0, 5.0, 0.0, 5.0);
              }

              DispatchWrapper[] dsEntities =   new DispatchWrapper[1];
              dsEntities[0] =   new DispatchWrapper(dsCircle);

               int[] dsEntityTypes_0 =   new   int[] { (int)dsObjectType_e.dsCircleType };
              BlockDefinition dsBlockDefinition = dsDoc.CreateBlockDefinition(
                "Test",
                "",
               0.0,
               0.0,
               0.0,
               dsEntityTypes_0,
               dsEntities,
               dsBlockDefinitionEntities_e.dsBlockDefinitionEntities_RemoveFromDrawing);

              BlockInstance dsBlockInstance = dsSketchManager.InsertBlock2("Test", -1.075, 14.997, 0.0, 1.0, 1.0, 1.0, 0.0);

               // Flat shot and replace existing block
              dsSketchManager.FlatShotByReplaceExistingBlock("Test");

               // Flat shot and export to file
              dsSketchManager.FlatShotByExportToFile(mainPath +  "\\" +  "newFile.dwg");

            application.Zoom(dsZoomRange_e.dsZoomRange_Bounds, null, null);
           }
            public  static DraftSight.Interop.dsAutomation.Application ConnectToDraftSight()
           {

              DraftSight.Interop.dsAutomation.Application dsApp =  null;

               try
              {
                 //Connect to DraftSight
                 dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
              }
               catch (Exception ex)
              {
                  MessageBox.Show("Failed to connect to DraftSight. Cause: " + ex.Message);
                  dsApp =   null;
              }

               return dsApp;
           }
      }
 }
```
