---
title: "Render Annotations to Separate Image File Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Render_Annotations_to_Separate_Image_File_Example_CSharp.htm"
---

# Render Annotations to Separate Image File Example (C#)

This example shows how to render annotations and dimensions visible in a model to a separate image file.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Open a model document.
// 2. Add a note to the model.
// 3. Right-click Annotations in the FeatureManager design tree
//    and click Show Feature Dimensions, if dimensions
//    are not visible in the model.
// 4. Verify that:
//    * ray-trace rendering engine is loaded.
//    * c:\temp exists.
//
// Preconditions:
// 1. Sets the options to include and render annotations and dimensions
//    visible in a model to a separate image file.
// 2. If prompted to add camera or perspective, click Continue
//    without Camera or Perspective.
// 3. Renders:
//    * model to c:\temp\annotations.png
//    * note and dimensions to c:\temp\annotations_1.png
// 4. Open both files to verify the previous step.
//--------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            RayTraceRenderer swRayTraceRenderer = default(RayTraceRenderer);
            RayTraceRendererOptions swRayTraceRenderOptions = default(RayTraceRendererOptions);
            bool status = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;

            //Access the ray-trace rendering engine
            //swRayTraceRenderer = (RayTraceRenderer)swApp.GetRayTraceRenderer();

            //Set options to include and render annotations and dimensions
            //visible in a model to a separate image file
            swRayTraceRenderOptions = (RayTraceRendererOptions)swRayTraceRenderer.RayTraceRendererOptions;
            swRayTraceRenderOptions.IncludeAnnotationsInRendering = true;
            swRayTraceRenderOptions.RenderAnnotationsToSeparateImage = true;
            status = swRayTraceRenderer.RenderToFile("c:\\temp\\annotations.png", 0, 0);
            status = swRayTraceRenderer.CloseFinalRenderWindow();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
