---
title: "Insert DXF/DWG File and Add Dimensions Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_DXF_File_and_Add_Dimensions_Example_CSharp.htm"
---

# Insert DXF/DWG File and Add Dimensions Example (C#)

This example shows how to insert a DXF/DWG image on a preselected plane or face and then autodimension it.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Open a part.
// 2. Replace path_name with the pathname of an existing DXF/DWG file.
// 3. Select a plane or face on which to insert the DXF/DWG image.
//
// Postconditions:
// 1. Adds the DXF/DWG image as a sketch.
// 2. Autodimensions the sketch.
// 3. Use Zoom to Area to inspect the sketch dimensioning.
// 4. Press F5 to rebuild the model.
//---------------------------------------------------------------------------
```

```vb
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 namespace InsertDXFAndAutodimension_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         const double nTolerance = 1E-08;
         ModelView swModelView;
         SketchManager swSketchMgr;
         int nRetVal;

          public void Main()
         {
             const string sDwgFileName = "path_name";

             ModelDoc2 swModel = default(ModelDoc2);
             FeatureManager swFeatMgr = default(FeatureManager);
             Feature swFeat = default(Feature);
             Sketch swSketch = default(Sketch);
             SelectionMgr swSelMgr = default(SelectionMgr);
             SelectData swSelData = default(SelectData);
             bool bRet = false;
             ImportDxfDwgData importData = default(ImportDxfDwgData);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelView = (ModelView)swModel.ActiveView;
             swFeatMgr = swModel.FeatureManager;
             importData = (ImportDxfDwgData)swApp.GetImportFileData(sDwgFileName);

             //Unit
             importData.set_LengthUnit("", (int)swLengthUnit_e.swMM);

             //Position
             bRet = importData.SetPosition("", (int)swDwgImportEntitiesPositioning_e.swDwgEntitiesCentered, 0, 0);

             //Sheet scale
             bRet = importData.SetSheetScale("", 1.0, 2.0);

             //Paper size
             bRet = importData.SetPaperSize("", (int)swDwgPaperSizes_e.swDwgPaperAsize, 0.0, 0.0);

             //Import method
             importData.set_ImportMethod("", (int)swImportDxfDwg_ImportMethod_e.swImportDxfDwg_ImportToExistingPart);

             swFeat = swFeatMgr.InsertDwgOrDxfFile2(sDwgFileName, importData);

             swSketch = (Sketch)swFeat.GetSpecificFeature2();
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swSelData = swSelMgr.CreateSelectData();

             nRetVal = AutoDimensionSketch(swApp, swModel, swSketch, swSelData);

             System.Diagnostics.Debugger.Break();

             // Rebuild to update sketch
             swModel.EditRebuild3();

         }

         public object GetAllSketchLines(SldWorks swApp, ModelDoc2 swModel, Sketch swSketch)
         {
             object functionReturnValue = null;

             Object[] vSketchSegArr = null;
             object vSketchSeg = null;
             SketchSegment swSketchSeg = default(SketchSegment);
             SketchLine swSketchCurrLine = default(SketchLine);
             SketchLine[] swSketchLineArr = new SketchLine[1];

             vSketchSegArr = (Object[])swSketch.GetSketchSegments();

             if ((vSketchSegArr != null))
             {
                 foreach (SketchSegment vSketchSeg_loopVariable in vSketchSegArr)
                 {
                     vSketchSeg = vSketchSeg_loopVariable;
                     swSketchSeg = (SketchSegment)vSketchSeg;
                     if ((int)swSketchSegments_e.swSketchLINE == swSketchSeg.GetType())
                     {
                         swSketchCurrLine = (SketchLine)swSketchSeg;
                         swSketchLineArr[swSketchLineArr.GetUpperBound(0)] = swSketchCurrLine;
                         Array.Resize(ref swSketchLineArr, swSketchLineArr.GetUpperBound(0) + 2);
                     }
                 }
             }

             if (0 == swSketchLineArr.GetUpperBound(0))
             {
                 // No straight lines in this sketch
                 functionReturnValue = null;
                 return functionReturnValue;
             }

             // Remove last, empty sketch line
             Array.Resize(ref swSketchLineArr, swSketchLineArr.GetUpperBound(0));
             functionReturnValue = swSketchLineArr;
             return functionReturnValue;

         }

         public bool GetSketchPoint(SldWorks swApp, ModelDoc2 swModel, Sketch swSketch, SketchPoint swSketchPt)
         {
             bool functionReturnValue = false;

             SketchPoint[] vSketchPtArr = null;
             vSketchPtArr = (SketchPoint[])swSketch.GetSketchPoints2();
             if ((vSketchPtArr != null))
             {
                 // Use first point
                 swSketchPt = (SketchPoint)vSketchPtArr[0];
                 functionReturnValue = true;
                 return functionReturnValue;
             }
             functionReturnValue = false;
             return functionReturnValue;

         }

         public bool FindVerticalOrigin(SldWorks swApp, ModelDoc2 swModel, Sketch swSketch, SketchSegment swSketchSegVert, SketchPoint swSketchPtVert)
         {
             bool functionReturnValue = false;

             SketchLine[] vSketchLineArr = null;
             object vSketchLine = null;
             SketchLine swSketchCurrLine = default(SketchLine);
             SketchPoint swStartPt = default(SketchPoint);
             SketchPoint swEndPt = default(SketchPoint);

             // Get first vertical line
             vSketchLineArr = (SketchLine[])GetAllSketchLines(swApp, swModel, swSketch);

             if ((vSketchLineArr != null))
             {
                 foreach (SketchLine vSketchLine_loopVariable in vSketchLineArr)
                 {
                     vSketchLine = vSketchLine_loopVariable;
                     swSketchCurrLine = (SketchLine)vSketchLine;
                     swStartPt = (SketchPoint)swSketchCurrLine.GetStartPoint2();
                     swEndPt = (SketchPoint)swSketchCurrLine.GetEndPoint2();

                     if (Math.Abs(swStartPt.X - swEndPt.X) < nTolerance)
                     {
                         swSketchSegVert = (SketchSegment)swSketchCurrLine;
                         functionReturnValue =  true;
                         return functionReturnValue;
                     }
                 }
             }

             // Get first point
             functionReturnValue = GetSketchPoint(swApp, swModel, swSketch, swSketchPtVert);
             return functionReturnValue;

         }

         public bool FindHorizontalOrigin(SldWorks swApp, ModelDoc2 swModel, Sketch swSketch, SketchSegment swSketchSegHoriz, SketchPoint swSketchPtHoriz)
         {
             bool functionReturnValue = false;

             SketchLine[] vSketchLineArr = null;
             object vSketchLine = null;
             SketchLine swSketchCurrLine = default(SketchLine);
             SketchPoint swStartPt = default(SketchPoint);
             SketchPoint swEndPt = default(SketchPoint);

             // Get first horizontal line
             vSketchLineArr = (SketchLine[])GetAllSketchLines(swApp, swModel, swSketch);

             if ((vSketchLineArr != null))
             {
                 foreach (SketchLine vSketchLine_loopVariable in vSketchLineArr)
                 {
                     vSketchLine = vSketchLine_loopVariable;
                     swSketchCurrLine = (SketchLine)vSketchLine;
                     swStartPt = (SketchPoint)swSketchCurrLine.GetStartPoint2();
                     swEndPt = (SketchPoint)swSketchCurrLine.GetEndPoint2();

                     if (Math.Abs(swStartPt.Y - swEndPt.Y) < nTolerance)
                     {
                         swSketchSegHoriz = (SketchSegment)swSketchCurrLine;
                         functionReturnValue =  true;
                         return functionReturnValue;
                     }
                 }
             }

             // Get first point
             functionReturnValue = GetSketchPoint(swApp, swModel, swSketch, swSketchPtHoriz);
             return functionReturnValue;

         }

         public int AutoDimensionSketch(SldWorks swApp, ModelDoc2 swModel, Sketch swSketch, SelectData swSelData)
         {
             int functionReturnValue = 0;

             Feature swFeat = default(Feature);
             SketchSegment swSketchSegHoriz = null;
             SketchPoint swSketchPtHoriz = null;
             SketchSegment swSketchSegVert = null;
             SketchPoint swSketchPtVert = null;
             bool bRet = false;

             if (false == FindHorizontalOrigin(swApp, swModel, swSketch, swSketchSegHoriz, swSketchPtHoriz))
             {
                 functionReturnValue = (int)swAutodimStatus_e.swAutodimStatusDatumLineNotHorizontal;
                 return functionReturnValue;
             }

             if (false == FindVerticalOrigin(swApp, swModel, swSketch, swSketchSegVert, swSketchPtVert))
             {
                 functionReturnValue = (int)swAutodimStatus_e.swAutodimStatusDatumLineNotVertical;
                 return functionReturnValue;
             }

             swFeat = (Feature)swSketch;

             bRet = swFeat.Select2(false, 0);

             // Editing sketch clears selections
             swModel.EditSketch();

             // Reselect sketch segments with correct marks for auto-dimensioning
             if ((swSketchSegVert != null))
             {
                 // Vertical line is for horizontal datum
                 bRet = swSketchSegVert.Select4(true, swSelData);
             }
             else if ((swSketchPtHoriz != null))
             {
                 bRet = swSketchPtHoriz.Select4(true, swSelData);
             }
             else if ((swSketchPtVert != null))
             {
                 // Use any sketch point for horizontal datum
                 bRet = swSketchPtVert.Select4(true, swSelData);
             }

             if ((swSketchSegHoriz != null))
             {
                 // Horizontal line is for vertical datum
                 bRet = swSketchSegHoriz.Select4(true, swSelData);
             }
             else if ((swSketchPtVert != null))
             {
                 bRet = swSketchPtVert.Select4(true, swSelData);
             }
             else if ((swSketchPtHoriz != null))
             {
                 // Use any sketch point for vertical datum
                 bRet = swSketchPtHoriz.Select4(true, swSelData);
             }

             // If contains circles use sketch points for datums
             if ((GetAllSketchLines(swApp, swModel, swSketch) ==  null))
             {
                 if ((swSketchPtHoriz != null))
                 {
                     bRet = swSketchPtHoriz.Select4(false, swSelData);
                 }
                 else if ((swSketchPtVert != null))
                 {
                     bRet = swSketchPtVert.Select4(false, swSelData);
                 }
             }

             swSketchMgr = swModel.SketchManager;
             nRetVal = swSketchMgr.FullyDefineSketch(true, true, (int)swSketchFullyDefineRelationType_e.swSketchFullyDefineRelationType_Vertical | (int)swSketchFullyDefineRelationType_e.swSketchFullyDefineRelationType_Horizontal, true, 1, null, 1, null, 1, 1);

             // Redraw so dimensions are displayed immediately
             double[] rect = null;
             rect = null;
             swModelView.GraphicsRedraw(rect);
             return functionReturnValue;

         }

         public SldWorks swApp;

     }
 }
```
