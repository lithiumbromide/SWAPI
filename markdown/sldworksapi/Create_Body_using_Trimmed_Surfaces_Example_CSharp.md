---
title: "Create Body using Trimmed Surfaces Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Body_using_Trimmed_Surfaces_Example_CSharp.htm"
---

# Create Body using Trimmed Surfaces Example (VB.NET)

## Create Body Using Trimmed Surfaces Example (C#)

The basic outline for creating a body using trimmed surfaces is as follows:

1. Create a new temporary body in a part using IPartDoc::CreateNewBody.
2. Create trimmed surfaces to create a body (for example, create six square surfaces that intersect at the edges to form a cube):

  1. Create a planar surface using IBody2::CreatePlanarSurface(RootPoint, Normal).
  2. Add a trimming loop to the planar surface using
    ISurface::AddTrimmingLoop2(Numcurves, _
    Order, _
    Dimen, _
    Periodic, _
    NumKnots, _
    NumCtrlPoints, _
    Knots, _
    CtrlPointDbls, _
    UVRange)
  3. The arguments for Surface::AddTrimmingLoop2 and their values for a square trimming loop are:

    | Argument | Description |
    | --- | --- |
    | NumCurves | Number of spline curves that make up the trimming loop (Long 4) |
    | Order | Orders for the spline curves ({2, 2, 2, 2} Array of Longs. Second-order linear curves) |
    | Dimen | Dimension of the control points for the spline curves ({2, 2, 2, 2} Array of Longs) |
    | Periodic | Periodicity of the spline curves ({0, 0, 0, 0} Array of Longs) |
    | NumKnots | Number of knots of the spline curves ({4, 4, 4, 4} Array of Longs) |
    | NumCtrlPoints | Number of control points for the spline curves ({2, 2, 2, 2} Array of Longs) |
    | Knots | Describes the locations of the knots on the spline curves ({0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1} Array of Doubles. Each spline curve contains 4 knots) |
    | CtrlPointDbls | Coordinates of control points for the square trimming loop ({0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0} Array of Doubles. (Two for each spline curve of the square trimming loop * Dimen) = 16 coordinates for the square trimming loop) |
    | UVRange | Min and max for the U and V values ({0, 1, 0, 1} Array of Doubles) |
  4. Create a trimmed surface on the body based on the trimming loop that was just created.
3. Sew the surfaces together into a new body using IBody2::CreateBodyFromSurfaces.

This example shows how to create trimmed surfaces and use them to create bodies.

```vb
  //-------------------------------------------------------------
 // Preconditions: Verify that the specified
 // part document template exists.
 //
 // Postconditions:
 // 1. Opens a new part document.
 // 2. Creates a temporary body.
 // 3. Creates six trimmed surfaces. For each:
 //    a. Creates a planar surface.
 //    b. Adds a trimming loop to the planar surface.
 //    c. Creates a trimmed surface on the temporary body based
 //       on the trimming loop.
 // 4. Sews the six trimmed surfaces together to form a new cube body.
 // 5. Creates a trimmed surface that is offset from the back of the cube.
 // 6. Examine the FeatureManager design tree and
 //    graphics area.
  //----------------------------------------------

 using System.Windows.Forms;
 using System;
 using System.Runtime.InteropServices;
 using SolidWorks.Interop.sldworks;

 namespace AddTrimmingLoop2_CSharp
 {
       public  partial  class   SolidWorksMacro
      {
            private  ModelDoc2 Model;
            private  PartDoc Part;
            private  double[] RootPoint =   new   double[3];
            private  double[] Normal =   new   double[3];
            private  Body2 TempBody;
            private  bool isGood;
            public  void Main()
           {

                  swApp.UserControl =   true;

                   // Create a new blank document
                  Model = (ModelDoc2)swApp.NewDocument(@"C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2020\templates\part.prtdot", 0, 0, 0);
                  Part = (PartDoc)Model;

                   // Create a new temporary body in the part
                  TempBody = (Body2)Part.CreateNewBody();
                   if (TempBody ==   null)
                  {
                        MessageBox.Show("Could not create the new body.");
                        return;
                  }

                   // Create trimmed surfaces for a cube with one meter per side

                   // LEFT
                  RootPoint[0] = 0;   // X
                  RootPoint[1] = 0;   // Y
                  RootPoint[2] = 0;   // Z
                  Normal[0] = 1;   // X
                  Normal[1] = 0;   // Y
                  Normal[2] = 0;   // Z
                  isGood = CreateSquareSurface(Part, TempBody, RootPoint, Normal,   true);

                   // RIGHT
                  RootPoint[0] = 1;
                  RootPoint[1] = 0;
                  RootPoint[2] = 0;
                  Normal[0] = 1;
                  Normal[1] = 0;
                  Normal[2] = 0;
                  isGood = CreateSquareSurface(Part, TempBody, RootPoint, Normal,   true);

                   // BOTTOM
                  RootPoint[0] = 0;
                  RootPoint[1] = 0;
                  RootPoint[2] = -1;
                  Normal[0] = 0;
                  Normal[1] = 1;
                  Normal[2] = 0;
                  isGood = CreateSquareSurface(Part, TempBody, RootPoint, Normal,   true);

                  // TOP
                  RootPoint[0] = 0;
                  RootPoint[1] = 1;
                  RootPoint[2] = -1;
                  Normal[0] = 0;
                  Normal[1] = 1;
                  Normal[2] = 0;
                  isGood = CreateSquareSurface(Part, TempBody, RootPoint, Normal,  true);

                   // FRONT
                  RootPoint[0] = 0;
                  RootPoint[1] = 0;
                  RootPoint[2] = 0;
                  Normal[0] = 0;
                  Normal[1] = 0;
                  Normal[2] = 1;
                  isGood = CreateSquareSurface(Part, TempBody, RootPoint, Normal,   true);

                   // BACK
                  RootPoint[0] = 0;
                  RootPoint[1] = 0;
                  RootPoint[2] = -1;
                  Normal[0] = 0;
                  Normal[1] = 0;
                  Normal[2] = 1;
                  isGood = CreateSquareSurface(Part, TempBody, RootPoint, Normal,   true);

                   // Create the body from the trimmed surfaces just created
                  TempBody.CreateBodyFromSurfaces();

                   // Create an offset surface from the back
                  RootPoint[0] = 0;
                  RootPoint[1] = 0;
                  RootPoint[2] = -2;
                  Normal[0] = 0;
                  Normal[1] = 0;
                  Normal[2] = 1;
                  isGood = CreateSquareSurface(Part, TempBody, RootPoint, Normal,   false);

                  Model.ViewZoomtofit2();
              }

               // CreateSquareSurface creates a square trimmed surface
               private  bool CreateSquareSurface(PartDoc Part,   Body2 SurfaceBody,   object RootPoint,   object Normal,   bool IsPartOfTempBody)
              {
                   bool isGood;
                   // Temporary surface
                   Surface TmpSurf;
                   // Arguments that define the trimming loop
                   int NumCurves;
                   int[] Order =   new   int[4];
                   int[] Dimen =   new   int[4];
                   int[] Periodic =   new   int[4];
                   int[] NumKnots =   new   int[4];
                  int[] NumCtrlPoints =   new   int[4];
                   double[] Knots =   new   double[16];
                   double[] CtrlPointDbls =   new   double[16];
                   double[] UVRange =   new   double[4];
                   // Initially this function has no problems,
                   // set this value to false if errors encountered
                   //CreateSquareSurface = true;
                   // Create a new planar surface based at RootPoint with the Normal vector Normal
                  TmpSurf = (Surface)SurfaceBody.CreatePlanarSurface(RootPoint, Normal);
                   if (TmpSurf ==   null)
                  {
                        //CreateSquareSurface = false;
                        return   false;
                  }
                   // Set the arguments to define a square trimming loop
                   // There are four curves (four sides)
                  NumCurves = 4;
                   // Orders of the spline curves
                  Order[0] = 2;
                  Order[1] = 2;
                  Order[2] = 2;
                  Order[3] = 2;
                   // There are two dimensions
                  Dimen[0] = 2;
                  Dimen[1] = 2;
                  Dimen[2] = 2;
                  Dimen[3] = 2;
                   // No periodics
                  Periodic[0] = 0;
                  Periodic[1] = 0;
                  Periodic[2] = 0;
                  Periodic[3] = 0;
                   // There are four knots (corners)
                  NumKnots[0] = 4;
                  NumKnots[1] = 4;
                  NumKnots[2] = 4;
                  NumKnots[3] = 4;
                   // A square has two control points
                  NumCtrlPoints[0] = 2;
                  NumCtrlPoints[1] = 2;
                  NumCtrlPoints[2] = 2;
                  NumCtrlPoints[3] = 2;
                   // The locations of the knots
                  Knots[0] = 0;
                  Knots[1] = 0;
                  Knots[2] = 1;
                  Knots[3] = 1;
                  Knots[4] = 0;
                  Knots[5] = 0;
                  Knots[6] = 1;
                  Knots[7] = 1;
                  Knots[8] = 0;
                  Knots[9] = 0;
                  Knots[10] = 1;
                  Knots[11] = 1;
                  Knots[12] = 0;
                  Knots[13] = 0;
                  Knots[14] = 1;
                  Knots[15] = 1;
                   // Set the actual trimming corners
                  CtrlPointDbls[0] = 0; CtrlPointDbls[1] = 0;
                  CtrlPointDbls[2] = 1; CtrlPointDbls[3] = 0;
                  CtrlPointDbls[4] = 1; CtrlPointDbls[5] = 0;
                  CtrlPointDbls[6] = 1; CtrlPointDbls[7] = 1;
                  CtrlPointDbls[8] = 1; CtrlPointDbls[9] = 1;
                  CtrlPointDbls[10] = 0; CtrlPointDbls[11] = 1;
                  CtrlPointDbls[12] = 0; CtrlPointDbls[13] = 1;
                  CtrlPointDbls[14] = 0; CtrlPointDbls[15] = 0;
                   // The possible range for the UV values
                  UVRange[0] = 0;
                  UVRange[1] = 1;
                  UVRange[2] = 0;
                  UVRange[3] = 1;
                   // Create the trimming loop on the surface
                  isGood = TmpSurf.AddTrimmingLoop2(NumCurves, Order, Dimen, Periodic, NumKnots, NumCtrlPoints, Knots, CtrlPointDbls, UVRange);
                   if (isGood ==   false)
                  {
                      //CreateSquareSurface = false;
                        return   false;
                  }

                   // Create the trimmed surface on the body
                   // based on the trimming loop just created
                  isGood = SurfaceBody.CreateTrimmedSurface();
                   if (isGood ==   false)
                  {
                        //CreateSquareSurface = false;
                        return   false;
                  }

                   if (IsPartOfTempBody)
                  {
                        //do nothing
                  }
                   else
                      SurfaceBody.CreateBodyFromSurfaces();

               Marshal.ReleaseComObject(TmpSurf);

               GC.WaitForPendingFinalizers();
               GC.Collect();

               GC.WaitForPendingFinalizers();
               GC.Collect();

               return  true;
              }

       // The SldWorks swApp variable is pre-assigned for you.
       public  SldWorks swApp;

      }
 }
```
