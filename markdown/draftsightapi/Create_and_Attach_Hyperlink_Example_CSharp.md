---
title: "Create and Attach HyperLink Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_and_Attach_Hyperlink_Example_CSharp.htm"
---

# Create and Attach HyperLink Example (C#)

This example shows how to create and attach a HyperLink to a Circle.

```vb
 //--------------------------------------------------------------
 // Preconditions:
 // 1. Create a C# Windows console project.
 // 2. Copy and paste this example into the C# IDE.
 // 3. Add a reference to:
 //    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 // 4. Add references to System and System.Windows.Forms.
 // 5. Start DraftSight and open a drawing document.
 // 6. Click Start Debugging.
 //
 // Postconditions:
 // 1. A Circle is constructed in the drawing document.
 // 2. A HyperLink is created and attached to the Circle.
 // 3. In DraftSight, put the cursor on the Circle to see the
 //    the hyperlink and Ctrl+click to open DraftSight's website.
 //----------------------------------------------------------------
 using System.Text;
 using DraftSight.Interop.dsAutomation;
 using System.Runtime.InteropServices;
 using System.Windows.Forms;

 namespace HyperLinkCSharp
 {
     class Program
     {
         private static DraftSight.Interop.dsAutomation.Application dsApp;

         static void Main(string[] args)
         {
             Document dsDoc = default(Document);
             Model dsModel = default(Model);
             SketchManager dsSketchManager = default(SketchManager);
             Circle dsCircle = default(Circle);
             double centerX = 0;
             double centerY = 0;
             double centerZ = 0;
             double radius = 0;

             //Connect to DraftSight application
             dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
             dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands

             //Get active document
             dsDoc = dsApp.GetActiveDocument();

             if ((dsDoc != null))
             {
                 //Get model space
                 dsModel = dsDoc.GetModel();

                 //Get Sketch Manager
                 dsSketchManager = dsModel.GetSketchManager();

                 //Circle parameters
                 centerX = 1.0;
                 centerY = 2.0;
                 centerZ = 0.0;
                 radius = 5.0;

                 //Construct a Circle
                 dsCircle = dsSketchManager.InsertCircle(centerX, centerY, centerZ, radius);

                 //Create and attach HyperLink to Circle
                 double startCornerX = 0;
                 startCornerX = 0.0;
                 double startCornerY = 0;
                 startCornerY = 0.0;
                 double startCornerZ = 0;
                 startCornerZ = 0.0;
                 double oppositeCornerX = 0;
                 startCornerX = 0.0;
                 double oppositeCornerY = 0;
                 startCornerY = 0.0;
                 double oppositeCornerZ = 0;
                 startCornerZ = 0.0;
                 string hyperLinkAddress = null;
                 hyperLinkAddress =  "http://www.3ds.com/products/draftsight/free-cad-software/";
                 string description = null;
                 description = "DraftSight's website";
                 PolyLine3D ds3DPolyLine = default(PolyLine3D);
                 HyperLink dsHyperLink = default(HyperLink);

                 dsHyperLink = dsSketchManager.AttachLinkToArea(startCornerX, startCornerY, startCornerZ, oppositeCornerX, oppositeCornerY, oppositeCornerZ, hyperLinkAddress, description,  out ds3DPolyLine);
                 dsCircle.SetHyperLink(dsHyperLink);

             }
             else
             {
                 MessageBox.Show ("There are no open documents in DraftSight.");

             }
         }
     }

 }
```
