---
title: "Get Temporary Axis and Its Reference Face Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Temporary_Axis_and_Its_Reference_Face_Example_CSharp.htm"
---

# Get Temporary Axis and Its Reference Face Example (C#)

This example shows how to get a temporary axis and its reference face.

```
//---------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\api\box.sldprt.
// 2. Click View > Hide/Show > Temporary Axes.
// 3. Select the temporary axis.
// 4. Open the Immediate window.
//
// Postconditions:
// 1. Gets whether the selected entity is a temporary
//    axis.
// 2. Gets the reference face of the temporary axis.
// 3. Examine the Immediate window and graphics area.
//
// NOTE: Because the part is used elsewhere, do not save
// changes.
//---------------------------------------------------
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
            SelectionMgr swSelMgr = default(SelectionMgr);
            Feature swFeature = default(Feature);
            Entity swEntity = default(Entity);
            RefAxis swRefAxis = default(RefAxis);
            object obj = null;
            Face2 swFace = default(Face2);

            swModel = (ModelDoc2)swApp.ActiveDoc;

            //Get selected entity
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swEntity = (Entity)swFeature;

            if (swEntity.GetType() == (int)swSelectType_e.swSelDATUMAXES)
            {
                swRefAxis = (RefAxis)swFeature.GetSpecificFeature2();
                //Get whether selected entity is a temporary axis
                if (swRefAxis.IsTempAxis())
                {
                    Debug.Print("Is temporary reference axis");
                    //Get reference face of temporary axis
                    obj = (object)swRefAxis.GetTempAxisReferenceFace();
                    if ((obj != null))
                    {
                        Debug.Print("  Got reference face of temporary axis");
                        swFace = (Face2)obj;
                        swFace.Highlight(true);
                        Debug.Print("  Highlighted reference face of temporary axis; examine the graphics area");
                    }
                    else
                    {
                        Debug.Print("Did not get reference face of temporary axis");
                    }
                }
                else
                {
                    Debug.Print("Not a temporary axis");
                }
            }
            else
            {
                Debug.Print("Select a temporary axis and run the macro again");
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
