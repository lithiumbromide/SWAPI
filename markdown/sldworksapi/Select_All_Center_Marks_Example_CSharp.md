---
title: "Select All Center Marks Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_All_Center_Marks_Example_CSharp.htm"
---

# Select All Center Marks Example (C#)

In the SOLIDWORKS API, center marks can be features or annotations.
Use these enumerators with ISelectionMgr::GetSelectedObjectType3 to return
that specific type of center mark:

- swSelCENTERMARKS for center marks that are features
- swSelCENTERMARKSSYMS for center marks that are
  annotations

Traversal over the two types is different for the center marks that
are:

- Annotations. Use IView::GetFirstCenterMark and
  ICenterMark::GetNext
- Features. Use IView::GetCenterMarks.

It is not directly possible to select center marks that are features,
even though they appear in a feature traversal. This example shows how
to indirectly select center marks that are features.

```
//------------------------------------------------
// Preconditions:
// 1. Verify that the drawing document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified drawing document.
// 2. Prints the path and file name of the drawing document to
//    the Immediate window.
// 3. Iterates the sheet and drawing views.
// 4. Prints the name of the sheet, drawing views,
//    and center mark annotations to the Immediate window.
// 5. Iterates the FeatureManager design tree.
// 6. Prints to the Immediate window that no center mark
//    features exist in the drawing document.
//------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace CenterMarkCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModExt = default(ModelDocExtension);
            DrawingDoc swDrawing = default(DrawingDoc);
            View swView = default(View);
            CenterMark swCtrMark = default(CenterMark);
            Annotation swAnn = default(Annotation);
            Feature swFeat = default(Feature);
            Feature swSubFeat = default(Feature);
            Feature swSubSubFeat = default(Feature);
            SelectionMgr swSelMgr = default(SelectionMgr);
            SelectData swSelData = default(SelectData);
            bool status = false;
            string fileName = null;
            int errors = 0;
            int warnings = 0;
            int i = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2025\\samples\\tutorial\\advdrawings\\foodprocessor.slddrw";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModExt = (ModelDocExtension)swModel.Extension;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swSelData = (SelectData)swSelMgr.CreateSelectData();
            swDrawing = (DrawingDoc)swModel;
            swView = (View)swDrawing.GetFirstView();
            swModel.ClearSelection2(true);
            Debug.Print("File = " + swModel.GetPathName());
            Debug.Print("---------------");

            i = 0;
            while ((swView != null))
            {
                Debug.Print("  View = " + swView.Name);
                // Traverse over annotation center marks
                swCtrMark = (CenterMark)swView.GetFirstCenterMark2();
                while ((swCtrMark != null))
                {
                    swAnn = (Annotation)swCtrMark.GetAnnotation();
                    Debug.Print("    " + swAnn.GetName());
                    // Select directly through annotation
                    status = swAnn.Select3(true, swSelData);
                    Debug.Assert(status);
                    swCtrMark = (CenterMark)swCtrMark.GetNext();
                    i = i + 1;
                }
                swView = (View)swView.GetNextView();
            }

            if (i == 0)
            {
                Debug.Print("No center mark annotations.");
            }

            Debug.Print("---------------");
            // Traverse over feature center marks
            i = 0;
            swFeat = (Feature)swModel.FirstFeature();
            while ((swFeat != null))
            {
                swSubFeat = (Feature)swFeat.GetFirstSubFeature();
                while ((swSubFeat != null))
                {
                    swSubSubFeat = (Feature)swSubFeat.GetFirstSubFeature();
                    while ((swSubSubFeat != null))
                    {
                        if ("CenterMark" == swSubSubFeat.GetTypeName2())
                        {
                            Debug.Print("  " + swSubSubFeat.Name);
                            // Cannot directly select feature because feature does not
                            // explicitly appear in FeatureManager design tree
                            // Must indirectly select feature through user interface
                            status = swModExt.SelectByID2(swSubSubFeat.Name, "CENTERMARKS", 0.0, 0.0, 0.0, true, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
                            Debug.Assert(status);
                        }
                        swSubSubFeat = (Feature)swSubSubFeat.GetNextSubFeature();
                    }
                    swSubFeat = (Feature)swSubFeat.GetNextSubFeature();
                }
                swFeat = (Feature)swFeat.GetNextFeature();
            }
            if (i == 0)
            {
                Debug.Print("No center mark features.");
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
