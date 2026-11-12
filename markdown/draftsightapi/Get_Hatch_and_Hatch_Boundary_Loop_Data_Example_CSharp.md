---
title: "Get Hatch and Hatch Boundary Loop Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_Hatch_and_Hatch_Boundary_Loop_Data_Example_CSharp.htm"
---

# Get Hatch and Hatch Boundary Loop Data Example (C#)

This example shows how to get Hatch and Hatch boundary loop data.

```vb
 //--------------------------------------------------------------
 // Preconditions:
 // 1. Create a C# Windows console project.
 // 2. Copy and paste this example into the C# IDE.
 // 3. Add a reference to:
 //    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 // 4. Add references to System and System.Windows.Forms.
 // 5. Start DraftSight, construct a Circle, Rectangle, Spline, or
 //    Ellipse, and apply a Hatch to the entity.
 // 6. Open the Immediate window.
 // 7. Start debugging the project.
 //
 // Postconditions:
 // 1. When the prompt appears in the DraftSight command window to
 //    select an entity, select the entity with the Hatch.
 // 2. The selected entity's Hatch and Hatch boundary loop data is printed
 //    to the  Immediate Window.
 //----------------------------------------------------------------

 using System;
 using System.Collections.Generic;
 using System.Text;
 using DraftSight.Interop.dsAutomation;
 using System.Runtime.InteropServices;
 using System.Windows.Forms;
 using System.Diagnostics;

 namespace HatchBoundaryLoops
 {
     class Program
     {
         private static DraftSight.Interop.dsAutomation.Application dsApp;

         static void Main(string[] args)
         {
             //Connect to DraftSight application
             dsApp = ConnectToDraftSight();
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

             //Get Selection Manager
             SelectionManager dsSelectionMgr = dsDoc.GetSelectionManager();

             //Get selection filter
             SelectionFilter dsSelectionFilter = dsSelectionMgr.GetSelectionFilter();

             //Clear selection filter
             dsSelectionFilter.Clear();

             //Add hatch entity to the selection filter
             dsSelectionFilter.AddEntityType(dsObjectType_e.dsHatchType);

             //Activate selection filter
             dsSelectionFilter.Active = true;

             //Get command message object
             CommandMessage dsCommandMessage = dsApp.GetCommandMessage();

             //Prompt user to select a Hatch entity
             //and get whether selected entity is a Hatch entity
             bool singleSelection = true;
             string prompt = "Please select a Hatch entity.";
             string errorMessage = "Selected entity is not a Hatch entity.";
             if (dsCommandMessage.PromptForSelection(singleSelection, prompt, errorMessage))
             {
                 //Get selected entity
                 int index = 0;
                 dsObjectType_e entityType;
                 object selectedEntity = dsSelectionMgr.GetSelectedObject(dsSelectionSetType_e.dsSelectionSetType_Previous, index, out entityType);

                 if (dsObjectType_e.dsHatchType != entityType)
                 {
                     MessageBox.Show(entityType + " was selected, but should be Hatch entity.");
                 }
                 else
                 {
                     Hatch dsHatch = selectedEntity as Hatch;
                     PrintHatchParameters(dsHatch);
                 }
             }
         }

         private static void PrintHatchParameters(Hatch dsHatch)
         {
             Debug.Print(Environment.NewLine + "Hatch parameters:");

             Debug.Print("Color = " + dsHatch.Color.GetNamedColor());
             Debug.Print("LineScale = " + dsHatch.LineScale);
             Debug.Print("LineStyle = " + dsHatch.LineStyle);
             Debug.Print("LineWeight = " + dsHatch.LineWeight);
             Debug.Print("Layer = " + dsHatch.Layer);
             Debug.Print("Visible = " + dsHatch.Visible);
             Debug.Print("Erased = " + dsHatch.Erased);
             Debug.Print("Handle = " + dsHatch.Handle);

             double x1, y1, z1;
             double x2, y2, z2;
             dsHatch.GetBoundingBox(out x1, out y1, out z1, out x2, out y2, out z2);
             Debug.Print(string.Format("BoundingBox: ({0},{1},{2}) and ({3},{4},{5})", x1, y1, z1, x2, y2, z2));

             //Iterate through Hatch boundary loops
             int loopsCount = dsHatch.GetBoundaryLoopsCount();
             Debug.Print("Count of loops = " + loopsCount);
             for (int index = 0; index < loopsCount; ++index)
             {
                 Debug.Print("Loop(" + index + "):");

                 //Get Hatch boundary loop
                 DraftSight.Interop.dsAutomation.HatchBoundaryLoop dsHatchBoundaryLoop = dsHatch.GetHatchBoundaryLoop(index);

                 Debug.Print("Type = " + dsHatchBoundaryLoop.Type);
                 Debug.Print("IsPolyline = " + dsHatchBoundaryLoop.IsPolyLine);

                 if (dsHatchBoundaryLoop.IsPolyLine)
                 {
                     //Get 2D PolyLine boundary loop data
                     GetPolyLineBoundaryLoopData(dsHatchBoundaryLoop);
                 }
                 else
                 {
                     //Get edges count
                     int edgesCount = dsHatchBoundaryLoop.GetEdgesCount();
                     Debug.Print("Edges count = " + edgesCount);
                     for (int edgeIndex = 0; edgeIndex < edgesCount; ++edgeIndex)
                     {
                         dsHatchEdgeType_e edgeType = dsHatchBoundaryLoop.GetEdgeType(edgeIndex);
                         Debug.Print("Edge type = " + edgeType);

                         switch (edgeType)
                         {
                             case dsHatchEdgeType_e.dsHatchEdgeType_Line:
                                 {
                                     //Get Line edge data
                                     GetLineEdgeData(dsHatchBoundaryLoop, edgeIndex);

                                     break;
                                 }
                             case dsHatchEdgeType_e.dsHatchEdgeType_CircleArc:
                                 {
                                     //Get Circle edge data
                                     GetArcEdgeData(dsHatchBoundaryLoop, edgeIndex);

                                     break;
                                 }
                             case dsHatchEdgeType_e.dsHatchEdgeType_EllipseArc:
                                 {
                                     //Get Ellipse edge data
                                     GetEllipseEdgeData(dsHatchBoundaryLoop, edgeIndex);

                                     break;
                                 }
                             case dsHatchEdgeType_e.dsHatchEdgeType_Spline:
                                 {
                                     //Get Spline edge data
                                     GetSplineEdgeData(dsHatchBoundaryLoop, edgeIndex);

                                     break;
                                 }
                         }
                     }
                 }
             }
         }

         private static void GetSplineEdgeData(HatchBoundaryLoop dsHatchBoundaryLoop, int edgeIndex)
         {
             int degree;
             bool rational;
             bool periodic;
             object knotValues;
             object controlPoints;
             dsHatchBoundaryLoop.GetSplineEdgeData(edgeIndex,  out degree,  out rational, out periodic, out knotValues, out controlPoints);
             Debug.Print("Spline edge data:");
             Debug.Print("   Degree = " + degree);
             Debug.Print("   Rational = " + rational);
             Debug.Print("   Periodic = " + periodic);

             if (knotValues != null)
             {
                 double[] knotValuesDblArray = (double[])knotValues;
                 if (knotValuesDblArray != null)
                 {
                     for (int index = 0; index < knotValuesDblArray.Length; ++index)
                     {
                         Debug.Print("   Knot(" + index +  "):" + knotValuesDblArray[index]);
                     }
                 }
             }

             if (controlPoints != null)
             {
                 double[] controlPointsDblArray = (double[])controlPoints;
                 if (controlPointsDblArray != null)
                 {
                     int controlPointIndex = 0;
                     for (int index = 0; index < controlPointsDblArray.Length; index += 2)
                     {
                         Debug.Print(string.Format("   Control point({0}): ({1},{2})", controlPointIndex, controlPointsDblArray[index], controlPointsDblArray[index + 1]));

                         controlPointIndex++;
                     }
                 }
             }
         }

         private static void GetEllipseEdgeData(HatchBoundaryLoop dsHatchBoundaryLoop, int edgeIndex)
         {
             double centerX;
             double centerY;
             double majorAxisX;
             double majorAxisY;
             double minorAxisLengthRatio;
             double startAngle;
             double endAngle;
             bool isCounterclockwiseFlag;
             dsHatchBoundaryLoop.GetEllipseEdgeData(edgeIndex,  out centerX, out centerY, out majorAxisX, out majorAxisY, out minorAxisLengthRatio, out startAngle, out endAngle, out isCounterclockwiseFlag);
             Debug.Print("Ellipse edge data:");
             Debug.Print("   Center X = " + centerX);
             Debug.Print("   Center Y = " + centerY);
             Debug.Print("   Major axis X = " + majorAxisX);
             Debug.Print("   Major axis Y = " + majorAxisY);
             Debug.Print("   Minor axis length ratio = " + minorAxisLengthRatio);
             Debug.Print("   Start angle = " + startAngle);
             Debug.Print("   End angle = " + endAngle);
             Debug.Print("   Is counter-clockwise = " + isCounterclockwiseFlag);
         }

         private static void GetArcEdgeData(HatchBoundaryLoop dsHatchBoundaryLoop, int edgeIndex)
         {
             double centerX;
             double centerY;
             double radius;
             double startAngle;
             double endAngle;
             bool isCounterclockwiseFlag;
             dsHatchBoundaryLoop.GetArcEdgeData(edgeIndex,  out centerX, out centerY, out radius, out startAngle, out endAngle, out isCounterclockwiseFlag);
             Debug.Print("Arc edge data:");
             Debug.Print("   Center X = " + centerX);
             Debug.Print("   Center Y = " + centerY);
             Debug.Print("   Radius = " + radius);
             Debug.Print("   Start angle = " + startAngle);
             Debug.Print("   End angle = " + endAngle);
             Debug.Print("   Is counter-clockwise = " + isCounterclockwiseFlag);
         }

         private static void GetLineEdgeData(HatchBoundaryLoop dsHatchBoundaryLoop, int edgeIndex)
         {
             double startPointX;
             double startPointY;
             double endPointX;
             double endPointY;
             dsHatchBoundaryLoop.GetLineEdgeData(edgeIndex,  out startPointX, out startPointY, out endPointX, out endPointY);
             Debug.Print("Line edge data:");
             Debug.Print("   Start point X = " + startPointX);
             Debug.Print("   Start Point Y = " + startPointY);
             Debug.Print("   End point X = " + endPointX);
             Debug.Print("   End point Y = " + endPointY);
         }

         private static void GetPolyLineBoundaryLoopData(HatchBoundaryLoop dsHatchBoundaryLoop)
         {
             bool hasBulge;
             bool isClosed;
             object coordinates;
             object bulges;
             dsHatchBoundaryLoop.GetPolyLineBoundaryLoopData(out hasBulge, out isClosed, out coordinates, out bulges);

             Debug.Print("2D PolyLine boundary loop data:");
             Debug.Print("   Has bulge = " + hasBulge);
             Debug.Print("   Is closed = " + isClosed);
             if (coordinates != null)
             {
                 double[] coordinatesDblArray = (double[])coordinates;
                 if (coordinatesDblArray != null)
                 {
                     int vertexIndex = 0;
                     for (int coordinateIndex = 0; coordinateIndex < coordinatesDblArray.Length; coordinateIndex += 2)
                     {
                         Debug.Print(string.Format("   Coordinate({0}): ({1},{2},{3})", vertexIndex++, coordinatesDblArray[coordinateIndex], coordinatesDblArray[coordinateIndex + 1]));
                     }
                 }
             }

             if (hasBulge && bulges != null)
             {
                 double[] bulgesDblArray = (double[])bulges;
                 if (bulgesDblArray != null)
                 {
                     for (int bulgeIndex = 0; bulgeIndex < bulgesDblArray.Length; ++bulgeIndex)
                     {
                         Debug.Print("   Bulge(" + bulgeIndex +  "):" + bulgesDblArray[bulgeIndex]);
                     }
                 }
             }
         }

         private static DraftSight.Interop.dsAutomation.Application ConnectToDraftSight()
         {
             DraftSight.Interop.dsAutomation.Application dsApp = null;

             try
             {
                 //Connect to DraftSight
                 dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
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
