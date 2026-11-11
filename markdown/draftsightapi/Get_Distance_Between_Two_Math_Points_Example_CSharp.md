---
title: "Get Distance Between Two Math Points Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_Distance_Between_Two_Math_Points_Example_CSharp.htm"
---

# Get Distance Between Two Math Points Example (C#)

This example shows how to get the distance between two math points.

```vb
 //-------------------------------------------------------------------
 // Preconditions:
 // 1. Create a C# Windows console project.
 // 2. Copy and paste this project into the C# IDE.
 // 3. Add a reference to:
 //    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.
 // 4. Add references to System and System.Windows.Forms.
 // 5. Start DraftSight.
 // 6. Run the macro.
 // 7. Select two points when prompted in the DraftSight command window.
 //
 // Postconditions: The distance between two math points is printed in
 // the DraftSight command window.
 //-------------------------------------------------------------------
 using System;
 using System.Collections.Generic;
 using System.Text;
 using DraftSight;
 using System.Runtime.InteropServices;
 using System.Windows.Forms;

 namespace GetDistance
 {
     class Program
     {
         private static DraftSight.Application dsApp;

         static void Main(string[] args)
         {
             //Connect to DraftSight application
             dsApp = ConnectToDraftSight();
             if (null == dsApp)
             {
                 return;
             }

             dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands

             //Get active document
             Document dsDoc = dsApp.GetActiveDocument();
             if (null == dsDoc)
             {
                 MessageBox.Show("There are no open documents in DraftSight.");
                 return;
             }

             //Get math utility
             MathUtility dsMathUtility = dsApp.GetMathUtility();

             //Get distance between two points
             GetDistance(dsMathUtility);
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

         private static void GetDistance(MathUtility dsMathUtility)
         {
             //Get command message
             CommandMessage dsCommandMessage = dsApp.GetCommandMessage();

             dsCommandMessage.PrintLine("Get distance between two points");

             //Prompt to select the first point and second points
             //to calculate the distance between them
             double firstX, firstY, firstZ;
             double secondX, secondY, secondZ;
             if (dsCommandMessage.PromptForPoint("Specify the first point",  out firstX,  out firstY,  out firstZ) &&
                 dsCommandMessage.PromptForPoint("Specify the second point",  out secondX, out secondY, out secondZ))
             {
                 //Create the first math point
                 MathPoint dsFirstMathPoint = dsMathUtility.CreatePoint(firstX, firstY, firstZ);

                 //Create the second math point
                 MathPoint dsSecondMathPoint = dsMathUtility.CreatePoint(secondX, secondY, secondZ);

                 //Get distance between points
                 MathPoint dsResultPoint1, dsResultPoint2;
                 double distance = dsMathUtility.Distance(dsFirstMathPoint, dsSecondMathPoint,
                                                           out dsResultPoint1, out dsResultPoint2);

                 //Get result point coordinates
                 dsResultPoint1.GetPosition(out firstX, out firstY, out firstZ);
                 dsResultPoint2.GetPosition(out secondX, out secondY, out secondZ);

                 string message = string.Format("The distance between ({0},{1},{2}) and ({3},{4},{5}) point is {6}.\n",
                                                firstX, firstY, firstZ, secondX, secondY, secondZ, distance);
                 dsCommandMessage.PrintLine(message);
             }
         }
     }
 }
```
