---
title: "Render Model (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Render_Model_Example_CSharp.htm"
---

# Render Model (C#)

This example shows how to use a ray-trace rendering engine to render a model and save the rendered image in BMP and HDR formats. You must have a Premium license to run this example.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Verify that:
 //    * specified part exists.
 //    * c:\temp exists.
 //    * a ray-trace rendering engine is loaded in SOLIDWORKS Design.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. If prompted to use perspective views in renderings, click
 //    Continue without Camera or Perspective.
 // 2. Changes the specified rendering options.
 // 3. Creates c:\temp\Filter_1.bmp and c:\temp\Filter_2.hdr containing
 //    rendered images of the part.
 // 4. Examine the Immediate window and c:\temp.
 //
 // NOTE: Rendering can take several minutes to complete.
 //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
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

         bool status;

         public void Main()
         {
             fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\routing-pipes\\fittings\\filter.sldprt";
             swModel = swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

             // Access the ray-trace rendering engine
             //swRayTraceRenderer = (RayTraceRenderer)swApp.GetRayTraceRenderer((int)swRayTraceRenderType_e.ray_trace_rendering_engine_member);

             // Get and set rendering options
             swRayTraceRenderOptions = swRayTraceRenderer.RayTraceRendererOptions;

             // Get current rendering values
             Debug.Print("Current rendering values");
             Debug.Print("  Image height = " + swRayTraceRenderOptions.ImageHeight);
             Debug.Print("  Image width = " + swRayTraceRenderOptions.ImageWidth);
             Debug.Print("  Image format = " + swRayTraceRenderOptions.ImageFormat);
             Debug.Print("  Preview render quality = " + swRayTraceRenderOptions.PreviewRenderQuality);
             Debug.Print("  Final render quality = " + swRayTraceRenderOptions.FinalRenderQuality);
             Debug.Print("  Bloom enabled? " + swRayTraceRenderOptions.BloomEnabled);
             Debug.Print("  Bloom threshold = " + swRayTraceRenderOptions.BloomThreshold);
             Debug.Print("  Bloom radius = " + swRayTraceRenderOptions.BloomRadius);
             Debug.Print("  Contour/cartoon rendering enabled? " + swRayTraceRenderOptions.ContourCartoonRenderingEnabled);
             Debug.Print("  Render type = " + swRayTraceRenderOptions.RenderType);
             Debug.Print("  Shaded contour? " + swRayTraceRenderOptions.ShadedContour);
             Debug.Print("  Contour line thickness = " + swRayTraceRenderOptions.ContourLineThickness);
             Debug.Print("  Contour line color = " + swRayTraceRenderOptions.ContourLineColor);
             Debug.Print("  Use SOLIDWORKS Design view aspect ratio? " + swRayTraceRenderOptions.UseSolidWorksViewAspectRatio);
              Debug.Print("  Alpha output? " + swRayTraceRenderOptions.AlphaOutput);
             Debug.Print(" ");

             // Change rendering values
             Debug.Print("New rendering values");
             swRayTraceRenderOptions.ImageHeight = 567;
             Debug.Print("  Image height = " + swRayTraceRenderOptions.ImageHeight);
             swRayTraceRenderOptions.ImageWidth = 678;
             Debug.Print("  Image width = " + swRayTraceRenderOptions.ImageWidth);
             swRayTraceRenderOptions.ImageFormat = (int)swRayTraceRenderImageFormat_e.swImageFormat_HDR;
             Debug.Print("  Image format = " + swRayTraceRenderOptions.ImageFormat);
             swRayTraceRenderOptions.PreviewRenderQuality = (int)swRayTraceRenderQuality_e.swRenderQuality_Better;
             Debug.Print("  Preview render quality = " + swRayTraceRenderOptions.PreviewRenderQuality);
             swRayTraceRenderOptions.FinalRenderQuality = (int)swRayTraceRenderQuality_e.swRenderQuality_Best;
             Debug.Print("  Final render quality = " + swRayTraceRenderOptions.FinalRenderQuality);
             swRayTraceRenderOptions.BloomEnabled = false;
             Debug.Print("  Bloom enabled? " + swRayTraceRenderOptions.BloomEnabled);
             swRayTraceRenderOptions.BloomThreshold = 70;
             Debug.Print("  Bloom threshold = " + swRayTraceRenderOptions.BloomThreshold);
             swRayTraceRenderOptions.BloomRadius = 4;
             Debug.Print("  Bloom radius = " + swRayTraceRenderOptions.BloomRadius);
             swRayTraceRenderOptions.ContourCartoonRenderingEnabled = true;
             Debug.Print("  Contour/cartoon rendering enabled? " + swRayTraceRenderOptions.ContourCartoonRenderingEnabled);
             swRayTraceRenderOptions.RenderType = (int)swRayTraceRenderingType_e.swRayTraceContour;
             Debug.Print("  Render type = " + swRayTraceRenderOptions.RenderType);
             swRayTraceRenderOptions.ShadedContour = false;
             Debug.Print("  Shaded contour? " + swRayTraceRenderOptions.ShadedContour);
             swRayTraceRenderOptions.ContourLineThickness = 3;
             Debug.Print("  Contour line thickness = " + swRayTraceRenderOptions.ContourLineThickness);
             swRayTraceRenderOptions.ContourLineColor = 255;
             Debug.Print("  Contour line color = " + swRayTraceRenderOptions.ContourLineColor);
             swRayTraceRenderOptions.UseSolidWorksViewAspectRatio = true;
             Debug.Print("  Use SOLIDWORKS Design view aspect ratio? " + swRayTraceRenderOptions.UseSolidWorksViewAspectRatio);

             // Display the preview window
             //status = swRayTraceRenderer.DisplayPreviewWindow
             // Display final render window
             //status = swRayTraceRenderer.InvokeFinalRender

             // Render in HDR format
             status = swRayTraceRenderer.RenderToFile("c:\\temp\\Filter_2", 0, 0);
             // Render in BMP format
             swRayTraceRenderOptions.ImageFormat = (int)swRayTraceRenderImageFormat_e.swImageFormat_WindowsBmp;
             status = swRayTraceRenderer.RenderToFile("c:\\temp\\Filter_1", 0, 0);

             // Abort final render
             //status = swRayTraceRenderer.AbortFinalRender
              // Close preview and final render windows
             //status = swRayTraceRenderer.CloseRayTraceRender

         }

         public SldWorks swApp;

     }

 }
```
