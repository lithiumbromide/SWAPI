---
title: "Get Distance Between Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Distance_Between_Entities_Example_CSharp.htm"
---

# Get Distance Between Entities Example (C#)

This example shows how to get the minimum and maximum distances between face and edge entities.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\multibody\multi_inter.sldprt.
 // 2. Open the Immediate window.
  // 3. Put your cursor anywhere in the Main module in the IDE and press F5.
 //
 // Postconditions:
  // 1. Creates a sketch line that depicts the maximum distance between
 //    the face and edge entities.
 // 2. Put your cursor over Sketch4 in the FeatureManager design tree and
 //    examine the graphics area.
 // 3. Examine the Immediate window.
 //
  // NOTE: Because the part is used elsewhere, do not save changes.
  //-----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace GetDistanceBetweenEntities_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swDoc;
         SelectionMgr swSM;
         Face2 swFace;
         Edge swEdge;
         Entity swTop1;
         Entity swTop2;
         bool bMin;
         long retval;
         double dist;
         double[] varParam;
         object varPos1;
         object varPos2;
         double[] Pos1 = new double[3];
         double[] Pos2 = new double[3];
         int caseType;
         bool boolstatus;

         public void Main()
         {

             varParam = null;
             swDoc = (ModelDoc2)swApp.ActiveDoc;
             swSM = (SelectionMgr)swDoc.SelectionManager;

             for (caseType = 1; caseType <= 2; caseType++)
             {
                 switch (caseType)
                 {
                     case 1:
                         FaceFaceMinDistance();
                         break;
                     case 2:
                         FaceEdgeMaxDistance();
                         break;
                     default:
                         break;
                 }
             }
         }

         public void SetParameterForEdge()
         {
             double[] startPt = new double[3]; ;
             double[] endPt = new double[3]; ;
             double[] startPara = new double[2]; ;
             double[] endPara = new double[2]; ;

             swEdge = (Edge)swSM.GetSelectedObject6(2, -1);
             startPt = (double[])((Vertex)swEdge.GetStartVertex()).GetPoint();
             endPt = (double[])((Vertex)swEdge.GetEndVertex()).GetPoint();
             startPara = (double[])swEdge.GetParameter(startPt[0], startPt[1], startPt[2]);
             endPara = (double[])swEdge.GetParameter(endPt[0], endPt[1], endPt[2]);

             double[] paramDl = new double[2];
             paramDl[0] = startPara[0];
             paramDl[1] = endPara[0];
             varParam = paramDl;
         }

         public void SetParameterForFace()
         {
             swFace = (Face2)swSM.GetSelectedObject6(2, -1);
             Surface swSurface = default(Surface);
             swSurface = (Surface)swFace.GetSurface();
             double[] varBox = new double[6];
             varBox = (double[])swFace.GetBox();
             double[] varLowParam = new double[2];
             double[] varHighParam = new double[2];
             varLowParam = (double[])swSurface.ReverseEvaluate(varBox[0], varBox[1], varBox[2]);
             varHighParam = (double[])swSurface.ReverseEvaluate(varBox[3], varBox[4], varBox[5]);

             double[] paramD2 = new double[4];
             paramD2[0] = varLowParam[0];
             paramD2[1] = varLowParam[1];
             paramD2[2] = varHighParam[0];
             paramD2[3] = varHighParam[1];
             varParam = paramD2;
         }

         public void CreateLine()
         {
             SketchManager swSkM = default(SketchManager);
             SketchSegment skSegment = default(SketchSegment);
             swSkM = swDoc.SketchManager;
             swDoc.Extension.SelectByID2("Front", "PLANE", 0, 0, 0, false, 0, null, 0);
             swSkM.InsertSketch(true);
             skSegment = swSkM.CreateLine(Pos1[0], Pos1[1], Pos1[2], Pos2[0], Pos2[1], Pos2[2]);
             swDoc.ClearSelection2(true);
             swSkM.InsertSketch(true);
         }

         public void FaceFaceMinDistance()
         {
             swDoc.ClearSelection();
             boolstatus = swDoc.Extension.SelectByID2("", "FACE", -0.07448317477082, -0.04390354307787, 0.08443247713632, false, 0, null, 0);
             boolstatus = swDoc.Extension.SelectByID2("", "FACE", -0.05640517674067, -0.005486808589922, 0.06500000000005, true, 0, null, 0);
             SetParameterForFace();
             if ((swSM.GetSelectedObjectCount() == 2))
             {
                 swTop1 = (Entity)swSM.GetSelectedObject6(1, -1);
                 swTop2 = (Entity)swSM.GetSelectedObject6(2, -1);
                 bMin = true;
                 retval = swTop1.GetDistance(swTop2, bMin, varParam, out varPos1, out varPos2, out dist);
                 Pos1 = (double[])varPos1;
                 Pos2 = (double[])varPos2;
                 Debug.Print("IEquity::GetDistance return value (0 = success; 1 = failure) : " + retval);
                 Debug.Print("Face1 coordinate: " + Pos1[0] + "," + Pos1[1] + "," + Pos1[2]);
                 Debug.Print("Face2 coordinate: " + Pos2[0] + "," + Pos2[1] + "," + Pos2[2]);
                 Debug.Print("Minimum distance between two faces = " + dist * 1000 + " mm");
                 Debug.Print("");
                 CreateLine();
             }
         }
         public void FaceEdgeMaxDistance()
         {
             swDoc.ClearSelection();
             boolstatus = swDoc.Extension.SelectByID2("", "FACE", -0.0712080569869, -0.04996892464504, 0.08163440548356, false, 0, null, 0);
             boolstatus = swDoc.Extension.SelectByID2("", "EDGE", -0.04898677039967, 0.0004196506486664, 0.06476403488529, true, 0, null, 0);
             SetParameterForEdge();
             if ((swSM.GetSelectedObjectCount() == 2))
             {
                 swTop1 = (Entity)swSM.GetSelectedObject6(1, -1);
                 swTop2 = (Entity)swSM.GetSelectedObject6(2, -1);
                 bMin = false;
                 retval = swTop1.GetDistance(swTop2, bMin, varParam, out varPos1, out varPos2, out dist);
                 Pos1 = (double[])varPos1;
                 Pos2 = (double[])varPos2;
                 Debug.Print("IEquity::GetDistance return value (0 = success; 1 = failure) : " + retval);
                 Debug.Print("Face coordinate: " + Pos1[0] + "," + Pos1[1] + "," + Pos1[2]);
                 Debug.Print("Edge coordinate: " + Pos2[0] + "," + Pos2[1] + "," + Pos2[2]);
                 Debug.Print("Maximum distance between face and edge = " + dist * 1000 + " mm");
                 Debug.Print("");
                 CreateLine();
             }
         }

         public SldWorks swApp;

     }
 }
```
