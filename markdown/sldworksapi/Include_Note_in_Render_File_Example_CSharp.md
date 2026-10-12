---
title: "Include Note in Render File Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Include_Note_in_Render_File_Example_CSharp.htm"
---

# Include Note in Render File Example (C#)

This example shows how to include a note visible in a model in the render file.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Open a model document.
// 2. Add a note to the model.
// 3. Verify that.
//    * a ray-trace rendering engine is loaded.
//    * c:\temp exists.
// 4. Open the Immediate window.
//
// Preconditions:
// 1. Sets the option to include the note visible in the model
//    in the render file.
// 2. If prompted to add camera or perspective, click Continue
//    without Camera or Perspective.
// 3. Examine the Immediate window and c:\temp\annotations.png.
//--------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace RayTraceRendererCSharp.csproj
{

    partial class SolidWorksMacro
    {

        public void Main()
        {

            ModelDoc2 swModel;
            RayTraceRenderer swRayTraceRenderer;
            RayTraceRendererOptions swRayTraceRenderOptions;
            bool status = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;

            //Access the ray-trace rendering engine
            //swRayTraceRenderer = (RayTraceRenderer)swApp.GetRayTraceRenderer();

            //Set option to include note visible in the model in the render file
            swRayTraceRenderOptions = (RayTraceRendererOptions)swRayTraceRenderer.RayTraceRendererOptions;
            swRayTraceRenderOptions.IncludeAnnotationsInRendering = true;
            Debug.Print("Include note in render file? " + swRayTraceRenderOptions.IncludeAnnotationsInRendering);
            status = swRayTraceRenderer.RenderToFile("c:\\temp\\annotations.png", 0, 0);
            Debug.Print("Note included in render file? " + status);
            status = swRayTraceRenderer.CloseRayTraceRender();
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;

    }
}
```
