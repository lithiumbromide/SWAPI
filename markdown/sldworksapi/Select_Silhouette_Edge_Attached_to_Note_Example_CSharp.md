---
title: "Select Silhouette Edge Attached to Note Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Silhouette_Edge_Attached_to_Note_Example_CSharp.htm"
---

# Select Silhouette Edge Attached to Note Example (C#)

This example shows how to select a silhouette edge attached to a note in a
drawing.

```
//-------------------------------------------
// Preconditions:
// 1. Verify that the drawing to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified drawing.
// 2. Activates Drawing View1.
// 3. Gets the note in Drawing View1
//    and the silhouette edge to which
//    the note is attached.
// 4. Examine the Immediate window and graphics area.
//---------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Select2SilhouetteEdgeCSharp.csproj
{

    partial class SolidWorksMacro
    {

        ModelDoc2 swModel;
        DrawingDoc swDrawing;
        View swView;
        SilhouetteEdge swSilhouetteEdge;
        Note swNote;
        Annotation swAnnotation;
        bool status;
        int errors;
        int warnings;
        string fileName;
        object[] attachedEntities;

        public void Main()
        {
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2025\\samples\\tutorial\\api\\cylinder20.SLDDRW";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swDrawing = (DrawingDoc)swModel;
            status = swDrawing.ActivateView("Drawing View1");
            swView = (View)swDrawing.ActiveDrawingView;

            // Get note and any attached entities
            swNote = (Note)swView.GetFirstNote2();
            swAnnotation = (Annotation)swNote.GetAnnotation();
            attachedEntities = (object[])swAnnotation.GetAttachedEntities3();
            // Select the silhouette edge to which the note is attached
            foreach (object attachedEntity in attachedEntities)
            {
                swSilhouetteEdge = (SilhouetteEdge)attachedEntity;
                status = swSilhouetteEdge.Select2(false, null);
                if (status)
                {
                    Debug.Print("Silhouette edge selected.");
                }
            }

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }

}
```
