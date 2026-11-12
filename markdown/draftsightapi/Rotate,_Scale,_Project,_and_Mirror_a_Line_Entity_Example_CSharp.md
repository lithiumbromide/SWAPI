---
title: "Rotate, Scale, Project, and Mirror a Line Entity Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_CSharp.htm"
---

# Rotate, Scale, Project, and Mirror a Line Entity Example (C#)

This example shows how to use a math transform to rotate, scale, project, and mirror a Line entity.

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
 //
 // Postconditions:
 // 1. A Line is drawn, rotated, scaled, projected, and
 //    mirrored.
 // 2. The transformation parameters are printed before each
 //    transformation.
 // 3. The Line parameters are printed before and after
 //    each transformation.
 //-------------------------------------------------------------------
 using System;
 using System.Collections.Generic;
 using System.Text;
 using DraftSight.Interop.dsAutomation;
 using System.Windows.Forms;
 using System.Runtime.InteropServices;
 using System.Diagnostics;

 namespace MathFunctionality
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

             //Create different transformations
             Dictionary<string, MathTransform> transformations = CreateDifferentTransformations(dsMathUtility);

             //Draw a Line
             Line dsLine = DrawLine(dsDoc);

             TransformLine(dsLine, transformations);
         }

         private static Dictionary<string, MathTransform> CreateDifferentTransformations(MathUtility dsMathUtility)
         {
             Dictionary<string, MathTransform> transformations = new Dictionary<string, MathTransform>();

             //Create translation transformation
             MathVector dsTranslationVector = dsMathUtility.CreateVector(2, 3, 0);
             MathTransform dsTranslationTransformation = dsMathUtility.CreateTransformTranslation(dsTranslationVector);

             transformations.Add("translation", dsTranslationTransformation);

             //Create scaling transformation
             MathPoint dsCenterPoint = dsMathUtility.CreatePoint(0, 0, 0);
             double scaleFactor = 1.2;
             MathTransform dsScalingTransformation = dsMathUtility.CreateTransformScaling(dsCenterPoint, scaleFactor);

             transformations.Add("scaling", dsScalingTransformation);

             //Create rotation transformation
             MathVector dsRotationAxis = dsMathUtility.CreateVector(0, 0, 1);
             double rotationAngle = Math.PI / 4; //45 degrees in radians
             MathTransform dsRotationTransformation = dsMathUtility.CreateTransformRotation(dsCenterPoint, dsRotationAxis,
                                                                                            rotationAngle);

             transformations.Add("rotation", dsRotationTransformation);

             //Create mirror transformation about point
             MathPoint dsMirrorPoint = dsMathUtility.CreatePoint(0, 0, 0);
             MathTransform dsMirrorAboutPointTransformation = dsMathUtility.CreateTransformMirroringAboutPoint(dsMirrorPoint);

             transformations.Add("mirror about point", dsMirrorAboutPointTransformation);

             //Create mirror transformation about Line
             MathLine dsMirrorLine = dsMathUtility.CreateLine(0, 0, 0, 0, 20, 0,  dsMathLineType_e.dsMathLineType_Bounded);
             MathTransform dsMirrorAboutLineTransformation = dsMathUtility.CreateTransformMirroringAboutLine(dsMirrorLine);

             transformations.Add("mirror about Line", dsMirrorAboutLineTransformation);

             //Create mirror transformation about plane
             MathPlane dsMirrorPlane = dsMathUtility.CreateZXPlane();
             MathTransform dsMirrorAboutPlaneTransformation = dsMathUtility.CreateTransformMirroringAboutPlane(dsMirrorPlane);

             transformations.Add("mirror about plane", dsMirrorAboutPlaneTransformation);

             //Create projection transformation
             MathPlane dsProjectionPlane = dsMathUtility.CreateYZPlane();
             MathVector dsProjectionDirection = dsMathUtility.CreateVector(1, 0, 0);
             MathTransform dsProjectionTransformation = dsMathUtility.CreateTransformProjection(dsProjectionPlane, dsProjectionDirection);

             transformations.Add("projection", dsProjectionTransformation);

             return transformations;
         }

         private static void TransformLine(Line dsLine, Dictionary<string, MathTransform> transformations)
         {
             //Get MathLine property of Line entity
             MathLine dsMathLine = dsLine.MathLine;

             //Print mathematical line parameters
             PrintMathLineParameters(dsMathLine);

             //Transform Line using the created transformations
             foreach (KeyValuePair<string, MathTransform> transformationItem in transformations)
             {
                 //Print transformation parameters
                 PrintMathTransformation(transformationItem.Key, transformationItem.Value);

                 //Transform mathematical line
                 dsMathLine.TransformBy(transformationItem.Value);

                 //Update Line
                 dsLine.MathLine = dsMathLine;

                 MessageBox.Show("The " + transformationItem.Key +  " transformation has been applied to a Line.");

                 //Zoom by window
                 double[] lowerLeftCorner = { -10, -10, 0 };
                 double[] upperRightCorner = { 10, 10, 0 };
                 dsApp.Zoom(dsZoomRange_e.dsZoomRange_Window, lowerLeftCorner, upperRightCorner);

                 //Print result mathematical line parameters
                 PrintMathLineParameters(dsMathLine);
             }
         }

         private static Line DrawLine(Document dsDoc)
         {
             //Get model space
             Model dsModel = dsDoc.GetModel();

             //Get sketch manager
             SketchManager dsSketchMgr = dsModel.GetSketchManager();

             //Draw a Line
             double[] startPoint = { 1, 1, 0 };
             double[] endPoint = { 5, 1, 0 };

             return dsSketchMgr.InsertLine(startPoint[0], startPoint[1], startPoint[2],
                                           endPoint[0], endPoint[1], endPoint[2]);
         }

         private static void PrintMathTransformation(string transformationName, MathTransform dsMathTransformation)
         {
             Debug.Print(Environment.NewLine + "The " + transformationName + " transformation:");

             int countOfRows = 4;
             int countOfColumns = 4;

             for (int i = 0; i < countOfRows; ++i)
             {
                 string rowInformation = "(";

                 for (int j = 0; j < countOfColumns; ++j)
                 {
                     rowInformation += dsMathTransformation.GetElementAt(i, j);

                     if (j != countOfColumns - 1)
                     {
                         rowInformation +=  "  ,  ";
                     }
                 }

                 rowInformation += ");";

                 Debug.Print(rowInformation);
             }
         }

         private static void PrintMathLineParameters(MathLine dsMathLine)
         {
             Debug.Print(Environment.NewLine + "Mathematical line parameters");

             Debug.Print(string.Format("Type = {0};", dsMathLine.GetType().ToString()));

             //Get start point
             MathPoint dsPoint = dsMathLine.StartPoint;

             double x, y, z;
             dsPoint.GetPosition(out x, out y, out z);

             Debug.Print(string.Format("StartPoint ({0}, {1}, {2});", x, y, z));

             //Get end point
             dsPoint = dsMathLine.EndPoint;

             dsPoint.GetPosition(out x, out y, out z);

             Debug.Print(string.Format("EndPoint ({0}, {1}, {2});", x, y, z));

             //Get direction
             MathVector dsVector;
             dsMathLine.GetDirection(out dsVector);

             dsVector.GetCoordinates(out x, out y, out z);

             Debug.Print(string.Format("Direction ({0}, {1}, {2});", x, y, z));

             Debug.Print(string.Format("Length = {0};", dsMathLine.GetLength().ToString()));
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
