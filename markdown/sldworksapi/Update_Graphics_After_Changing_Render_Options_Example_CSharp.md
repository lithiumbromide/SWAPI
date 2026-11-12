---
title: "Update Graphics Area After Changing Render Options Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Update_Graphics_After_Changing_Render_Options_Example_CSharp.htm"
---

# Update Graphics Area After Changing Render Options Example (C#)

This example shows how to update the graphics area after changing the ray-trace rendering engine's options.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Verify that:
//    * specified part exists.
//    * ray-trace rendering engine is loaded in SOLIDWORKS Design.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. If prompted to use perspective views in rendering, click
//    Continue without camera or perspective and OK.
// 2. Changes the specified render options and updates the graphics area.
// 3. Examine the graphics area and Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//---------------------------------------------------------------------------
using System;
using System.Diagnostics;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;

namespace RayTraceRendererCSharp.csproj
{
    partial class SolidWorksMacro
    {

        ModelDoc2 swModel;
        RayTraceRenderer swRayTraceRenderer;
        RayTraceRendererOptions swRayTraceRenderOptions;
        int errors;
        int warnings;
        string fileName;

        public void Main()
        {
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\routing-pipes\\fittings\\filter.sldprt";
            swModel = swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            // Access ray-trace rendering engine
            // swRayTraceRenderer = (RayTraceRenderer)swApp.GetRayTraceRenderer((int)swRayTraceRenderType_e.ray_trace_renderer_member);

            // Get and set render options
            swRayTraceRenderOptions = swRayTraceRenderer.RayTraceRendererOptions;

            // Get current render values
            Debug.Print("Current render values");
            Debug.Print("  Contour/cartoon enabled? " + swRayTraceRenderOptions.ContourCartoonRenderingEnabled);
            Debug.Print("  Render type (0 = cartoon; 1 = contour) = " + swRayTraceRenderOptions.RenderType);
            Debug.Print(" ");

            // Change render values and update graphics area
            Debug.Print("Changed render values");
            swRayTraceRenderOptions.ContourCartoonRenderingEnabled = true;
            Debug.Print("  Contour/cartoon enabled? " + swRayTraceRenderOptions.ContourCartoonRenderingEnabled);
            swRayTraceRenderOptions.RenderType = (int)swRayTraceRenderingType_e.swRayTraceCartoon;
            Debug.Print("  Render type (0 = cartoon; 1 = contour) = " + swRayTraceRenderOptions.RenderType);
            swRayTraceRenderOptions.HasCartoonEdges = true;
            Debug.Print("  Has cartoon edges? " + swRayTraceRenderOptions.HasCartoonEdges);
            swRayTraceRenderOptions.UpdateGraphics();
        }

        public SldWorks swApp;
    }
}
```
