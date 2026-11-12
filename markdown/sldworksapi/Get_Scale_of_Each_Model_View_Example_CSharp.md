---
title: "Get Scale Factor of Each Model View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Scale_of_Each_Model_View_Example_CSharp.htm"
---

# Get Scale Factor of Each Model View Example (C#)

This example shows how to get the scale factor of each model view in a part document.

```
//---------------------------------
// Preconditions:
// 1. Open a part document.
// 2. Click Window > Viewport > Four View.
// 3. Click a model view and spin the middle-mouse
//    button forward or back.
// 4. Open the Immediate Window.
//
// Postconditions:
// 1. Gets the number of model views in the part document.
// 2. Gets the scale factor of each model view.
// 3. Examine the Immediate Window.
//----------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace GetModelViewScalesCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 SwModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            ModelView swModView = default(ModelView);
            object[] modViews = null;
            long Count = 0;

            SwModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)SwModel.Extension;

            // Get model views
            modViews = (object[])swModelDocExt.GetModelViews();

            // Get number of model views
            Count = swModelDocExt.GetModelViewCount();
            Debug.Print("Number of model views: " + Count);

            // Get the scale factor of each model view
            for (long i = 0; i < Count; i++)
            {
                swModView = (ModelView)modViews[i];
                Debug.Print("Scale factor of this model view is: " + swModView.Scale2);
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
