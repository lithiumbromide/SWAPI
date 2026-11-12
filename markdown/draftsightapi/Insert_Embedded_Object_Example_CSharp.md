---
title: "Insert Embedded Object Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Embedded_Object_Example_CSharp.htm"
---

# Insert Embedded Object Example (C#)

This example shows how to embed a file object in a DraftSight drawing.

```vb
 //--------------------------------------------------------------
 // Preconditions:
 // 1. Create a C# Windows console project.
 // 2. Copy and paste this example into the C# IDE.
 // 3. Add a reference to:
 //    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 // 4. Add references to System and System.Windows.Forms.
 // 5. Place the document to embed in the project assembly folder.
 // 6. Right-click the project and select Add > Existing Item.
 // 7. Select the document to embed and click Add.
 // 8. Right-click the file in Solution Explorer and select Properties.
 // 9. For the Copy to Output property select Copy Always.
 //10. Modify the document name referenced in the code.
 //11. Start DraftSight and open a drawing document.
 //12. Start debugging the project.
 //
 // Postconditions:
 // 1. The file object is embedded in the drawing.
 // 2. Inspect the Immediate window for its position and parameters.
 //----------------------------------------------------------------
 using System;
 using System.Collections.Generic;
 using System.Text;
 using DraftSight;
 using System.Windows.Forms;
 using System.Runtime.InteropServices;
 using System.Diagnostics;
 using System.IO;
 using System.Reflection;

 namespace InsertEmbeddedObject
 {
     class Program
     {
         static void Main(string[] args)
         {
             //Connect to DraftSight application
             DraftSight.Application dsApp = ConnectToDraftSight();
             if (null == dsApp)
             {
                 return;
             }

             dsApp.AbortRunningCommand();  // abort any command currently running in DraftSight to avoid nested commands

             //Get active document
             Document dsDoc = dsApp.GetActiveDocument();
             if (null == dsDoc)
             {
                 MessageBox.Show("There are no open documents in DraftSight.");
                 return;
             }

             //Get model space
             Model dsModel = dsDoc.GetModel();

             //Get sketch manager
             SketchManager dsSketchMgr = dsModel.GetSketchManager();

             //Embedded object parameters
             string filePath = Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), "SampleDoc.docx");
             bool link = true;
             bool displayAsIcon = false;

             //Insert embedded object
             EmbeddedObject dsEmbeddedObject = dsSketchMgr.InsertEmbeddedObjectFromFile(filePath, link, displayAsIcon);
             if (null != dsEmbeddedObject)
             {
                 PrintParameters(dsEmbeddedObject);
             }
             else
             {
                 MessageBox.Show("Embedded object entity was not added to the current drawing.");
             }
         }

         private static void PrintParameters(EmbeddedObject dsEmbeddedObject)
         {
             Debug.Print(Environment.NewLine + "Embedded object parameters...");

             //Print common entity parameters
             Debug.Print("Handle = " + dsEmbeddedObject.Handle);
             Debug.Print("Color = " + dsEmbeddedObject.Color.GetNamedColor());
             Debug.Print("Erased = " + dsEmbeddedObject.Erased);
             Debug.Print("Layer = " + dsEmbeddedObject.Layer);
             Debug.Print("LineScale = " + dsEmbeddedObject.LineScale);
             Debug.Print("LineStyle = " + dsEmbeddedObject.LineStyle);
             Debug.Print("LineWeight = " + dsEmbeddedObject.LineWeight);
             Debug.Print("Visible = " + dsEmbeddedObject.Visible);

             double x1, y1, z1;
             double x2, y2, z2;
             dsEmbeddedObject.GetBoundingBox(out x1, out y1, out z1, out x2, out y2, out z2);
             Debug.Print(string.Format("BoundingBox: ({0},{1},{2}) and ({3},{4},{5})", x1, y1, z1, x2, y2, z2));

             //Print embedded object parameters
             Debug.Print("Height = " + dsEmbeddedObject.Height);
             Debug.Print("Width = " + dsEmbeddedObject.Width);
             Debug.Print("PrintQuality = " + dsEmbeddedObject.PrintQuality);
             Debug.Print("LinkPath = " + dsEmbeddedObject.GetLinkPath());
             Debug.Print("SourceApplication = " + dsEmbeddedObject.GetSourceApplication());
             Debug.Print("Type = " + dsEmbeddedObject.GetType());

             //Get position of embedded object
             double x, y, z;
             dsEmbeddedObject.GetPosition(out x, out y, out z);
             Debug.Print(string.Format("Position = ({0},{1},{2})", x, y, z));
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
