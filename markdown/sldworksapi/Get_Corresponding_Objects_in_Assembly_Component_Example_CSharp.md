---
title: "Get Corresponding Objects in Assembly Component Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Corresponding_Objects_in_Assembly_Component_Example_CSharp.htm"
---

# Get Corresponding Objects in Assembly Component Example (C#)

This example shows how to get the corresponding sketch contour, sketch segments, and annotation for a component in the context of the assembly.

```
//------------------------------------------------------------------
// Preconditions:
// 1. Verify that:
//    * specified part and assembly templates
//    * C:\test
//    exist.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens a new part and creates a sketch containing
//    a sketch arc, sketch line, and a note.
// 2. Saves the part as C:\test\part1.sldprt.
// 3. Makes an assembly using the part document and saves
//    the assembly as C:\test\assem1.sldasm.
// 4. Activates the part.
//    a. Gets the persistent reference IDs of the sketch segments
//       in the sketch contour.
//    b. Gets the object ID of the note annotation.
// 5. Activates the assembly.
//    a. Gets the persistent reference IDs of the sketch
//       segments in the sketch contour in the context
//       of the assembly.
//    b. Gets the object ID of the note annotation in the context
//       of the assembly.
// 6. Examine the Immediate window.
//------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            AssemblyDoc swAssembly = default(AssemblyDoc);
            Component2 swComponent = default(Component2);
            SketchManager swSketchManager = default(SketchManager);
            SketchSegment swSketchSegment = default(SketchSegment);
            Note swNote = default(Note);
            Annotation swAnnotation = default(Annotation);
            TextFormat swTextFormat = default(TextFormat);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            Feature swFeature = default(Feature);
            Sketch swSketch = default(Sketch);
            SketchContour swSketchContour = null;
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            object swObject = null;
            object[] sketchSegments = null;
            object[] sketchContours = null;
            int nbrSketchContours = 0;
            int nbrSketchSegments = 0;
            int[] sketchSegmentIDs = null;
            int sketchSegmentType = 0;
            int annotationID = 0;
            int annotationType = 0;
            bool status = false;
            int errors = 0;
            int warnings = 0;
            int i = 0;
            int j = 0;

            //Create sketch containing a sketch arc,
            //sketch line, and annotation
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SolidWorks 2016\\templates\\Part.prtdot", 0, 0, 0);
            swSketchManager = (SketchManager)swModel.SketchManager;
            swSketchSegment = (SketchSegment)swSketchManager.CreateArc(-0.0756, 0.0, 0.0, -0.020568, 0.0, 0.0, -0.130614, 0.001423, 0.0, 1);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(-0.130614, 0.001423, 0.0, -0.0756, -0.047042, 0.0);
            swNote = (Note)swModel.InsertNote("This is a sketch segment");
            if ((swNote != null))
            {
                swNote.LockPosition = false;
                swNote.Angle = 0;
                status = swNote.SetBalloon(0, 0);
                swAnnotation = (Annotation)swNote.GetAnnotation();
                if ((swAnnotation != null))
                {
                    errors = swAnnotation.SetLeader3((int)swLeaderStyle_e.swUNDERLINED, 0, true, false, false, false);
                    status = swAnnotation.SetPosition2(-0.002501468059071, 0.0826874163970699, 0);
                    swTextFormat = null;
                    status = swAnnotation.SetTextFormat(0, true, swTextFormat);
                }
            }
            swModel.ClearSelection2(true);
            swModel.WindowRedraw();
            swSketchManager.InsertSketch(true);
            swModelDocExt = swModel.Extension;
            status = swModelDocExt.SaveAs("C:\\test\\part1.sldprt", (int)swSaveAsVersion_e.swSaveAsCurrentVersion, (int)swSaveAsOptions_e.swSaveAsOptions_Silent, null, ref errors, ref warnings);

            //Save part as assembly
            swAssembly = (AssemblyDoc)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SolidWorks 2016\\templates\\Assembly.asmdot", 0, 0, 0);
            swComponent = (Component2)swAssembly.AddComponent5("C:\\test\\part1.SLDPRT", (int)swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", false, "", -1.60609059776107E-05, 0, 8.47512097834624E-06);
            swModel = (ModelDoc2)swAssembly;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SaveAs("C:\\test\\Assem1.SLDASM", (int)swSaveAsVersion_e.swSaveAsCurrentVersion, (int)swSaveAsOptions_e.swSaveAsOptions_Silent, null, ref errors, ref warnings);

            //Get persistent reference IDs of sketch segments in sketch contour in part
            swModel = (ModelDoc2)swApp.ActivateDoc3("Part1.SLDPRT", false, (int)swRebuildOnActivation_e.swRebuildActiveDoc, ref errors);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0.0, 0.0, 0.0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swSketch = (Sketch)swFeature.GetSpecificFeature2();
            Debug.Print(swModel.GetPathName());
            Debug.Print("");
            if ((swSketch != null))
            {
                sketchContours = (object[])swSketch.GetSketchContours();
                nbrSketchContours = sketchContours.Length;
                Debug.Print("  Number of sketch contours in " + swFeature.Name + " = " + nbrSketchContours);
                for (i = 0; i < sketchContours.Length; i++)
                {
                    swSketchContour = (SketchContour)sketchContours[i];
                    if ((swSketchContour != null))
                    {
                        status = swSketchContour.Select2(false, null);
                    }
                    sketchSegments = (object[])swSketchContour.GetSketchSegments();
                    nbrSketchSegments = sketchSegments.Length;
                    for (j = 0; j < sketchSegments.Length; j++)
                    {
                        swSketchSegment = (SketchSegment)sketchSegments[j];
                        if ((swSketchSegment != null))
                        {
                            sketchSegmentIDs = (int[])swSketchSegment.GetID();
                            sketchSegmentType = swSketchSegment.GetType();
                            Debug.Print("  Persistent IDs = [" + sketchSegmentIDs[0] + ", " + sketchSegmentIDs[1] + "] and type = " + sketchSegmentType + " (0 = line; 1 = arc)");
                        }
                    }
                }
            }

            //Get object ID of note annotation in part
            status = swModelDocExt.SelectByID2("DetailItem1@Annotations", "NOTE", -0.00650517330771608, 0.0568327787544409, -0.035178659814812, false, 0, null, 0);
            swNote = (Note)swSelectionMgr.GetSelectedObject6(1, -1);
            swAnnotation = (Annotation)swNote.GetAnnotation();
            annotationType = swAnnotation.GetType();
            annotationID = swModelDocExt.GetObjectId(swAnnotation);
            Debug.Print("");
            Debug.Print("  Annotation ID = " + annotationID + " and type = " + annotationType + " (6 = note)");

            //Activate the assembly
            swModel = (ModelDoc2)swApp.ActivateDoc3("Assem1.SLDASM", false, (int)swRebuildOnActivation_e.swRebuildActiveDoc, ref errors);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Part1-1@Assem1", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swComponent = (Component2)swSelectionMgr.GetSelectedObject6(1, -1);
            Debug.Print("");
            Debug.Print(swModel.GetPathName());
            Debug.Print("");

            //Get corresponding sketch contour and sketch segments
            //and their persistent reference IDs in component
            swObject = (object)swComponent.GetCorresponding(swSketchContour);
            swSketchContour = null;
            swSketchContour = (SketchContour)swObject;
            if ((swSketchContour != null))
            {
                status = swSketchContour.Select2(false, null);
            }
            sketchSegments = (object[])swSketchContour.GetSketchSegments();
            Debug.Print("  Number of sketch contours in " + swFeature.Name + " = " + nbrSketchContours);
            nbrSketchSegments = sketchSegments.Length;
            for (j = 0; j < sketchSegments.Length; j++)
            {
                swSketchSegment = (SketchSegment)sketchSegments[j];
                if ((swSketchSegment != null))
                {
                    sketchSegmentIDs = (int[])swSketchSegment.GetID();
                    sketchSegmentType = swSketchSegment.GetType();
                    Debug.Print("  Persistent IDs = [" + sketchSegmentIDs[0] + ", " + sketchSegmentIDs[1] + "] and type = " + sketchSegmentType + " (0 = line; 1 = arc)");
                }
            }

            //Get object ID of corresponding note annotation in component
            swObject = (object)swComponent.GetCorresponding(swNote);
            swNote = null;
            swNote = (Note)swObject;
            if ((swNote != null))
            {
                swAnnotation = (Annotation)swNote.GetAnnotation();
                annotationType = swAnnotation.GetType();
                annotationID = swModelDocExt.GetObjectId(swAnnotation);
                Debug.Print("");
                Debug.Print("  Annotation ID = " + annotationID + " and type = " + annotationType + " (6 = note)");
            }
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
