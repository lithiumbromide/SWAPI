---
title: "IRayTraceRendererOptions Interface Properties"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions_properties"
member: ""
kind: "properties"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_properties.html"
---

# IRayTraceRendererOptions Interface Properties

For a list of all members of this type, see [IRayTraceRendererOptions members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AlphaOutput | Gets or sets whether to render the model as alpha or final color output. |
| Property | BloomEnabled | Gets or sets whether to enable bloom effect. |
| Property | BloomRadius | Gets or sets the the distance bloom radiates from source. |
| Property | BloomThreshold | Gets or sets the level of brightness or emissiveness to which bloom effect is applied. |
| Property | CausticAmount | Gets or sets the maximum number of photons fired, which controls the amount of visible caustics. |
| Property | CausticQuality | Gets or sets the number of photons sampled at each pixel, which controls the quality of the caustics. |
| Property | ClientWorkload | Gets or sets how many buckets (sections of rendering) are sent to each client processor. |
| Property | ContourCartoonRenderingEnabled | Gets or sets whether to enable contour/cartoon rendering. |
| Property | ContourEnabled | Obsolete. Superseded by IRayTraceRendererOptions::ContourCartoonRenderingEnabled . |
| Property | ContourLineColor | Gets or sets the color of the contour lines. |
| Property | ContourLineThickness | Gets or sets the thickness of contour lines. |
| Property | CustomRenderSettings | Gets or sets whether to enable custom render settings. |
| Property | DefaultImagePath | Gets or sets the default path to which to save the image. |
| Property | DirectCaustics | Gets or sets whether to enable direct caustics in the final render . |
| Property | FinalRenderQuality | Gets or sets quality of the final render . |
| Property | Gamma | Gets or sets the value for midtones of the rendered image while preserving the extreme whites and blacks. |
| Property | HasCartoonEdges | Gets or sets whether to render with cartoon edges. |
| Property | HasCartoonShading | Gets or sets whether to render with cartoon shading. |
| Property | ImageFormat | Gets or sets the format of the image. |
| Property | ImageHeight | Gets or sets the height of the image. |
| Property | ImageWidth | Gets or sets the width of the image. |
| Property | IncludeAnnotationsInRendering | Gets or sets whether to include annotations and dimensions visible in the model when rendering to a file . |
| Property | NetworkRendering | Gets or sets whether to enable network rendering. |
| Property | NetworkSharedDirectory | Gets or sets the name of the shared network directory for network renders . |
| Property | NumberOfReflections | Gets or sets the number of reflections in the final render . |
| Property | NumberOfRefractions | Gets or sets the number of refractions in the final render . |
| Property | OffloadedRendering | Gets or sets whether to offload rendering to other networked machines. |
| Property | OutputAmbientOcclusion | Gets or sets whether to render with ambient occlusion. |
| Property | PreviewRenderQuality | Gets or sets the quality of the rendering in the preview window. |
| Property | RenderAnnotationsToSeparateImage | Gets or sets whether to render annotations and dimensions visible in the model to a separate image file. |
| Property | RenderType | Gets or sets whether to render with contour or cartoon lines. |
| Property | SendDataForNetworkJob | Gets or sets whether to send rendering data over the network. |
| Property | ShadedContour | Gets or sets whether to shade the contours lines. |
| Property | UseSceneBackgroundImageAspectRatio | Gets or sets whether to use the aspect ratio of the scene's background image for ray-trace rendering engine preview and final renders. |
| Property | UseSolidWorksViewAspectRatio | Gets or sets whether to use the aspect ratio of the SOLIDWORKS view for ray-trace rendering engine preview and final renders. |

[Top](#topBookmark)

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
