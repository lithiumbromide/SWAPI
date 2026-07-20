---
title: "IRenderMaterial Interface Properties"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial_properties"
member: ""
kind: "properties"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_properties.html"
---

# IRenderMaterial Interface Properties

For a list of all members of this type, see[IRenderMaterial members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AboutAxis | Gets or sets the about axis value for a cylindrical mapping type. |
| Property | AccurateReflections | Selects or clears the Accurate reflections (slower) setting, which controls the level of surface reflections, for illuminating this appearance. |
| Property | AlongAxis | Gets or sets the along axis value for a cylindrical mapping type. |
| Property | Ambient | Gets or sets the ambient light intensity for illuminating this appearance. |
| Property | AnisotropicBias | Gets or sets the anisotropic bias, which makes the effect of light on the surface stronger in the horizontal or vertical direction, for illuminating this appearance. |
| Property | AnisotropicCylinderDistance | Gets or sets the anisotropic cylinder distance for illuminating this appearance. |
| Property | AnisotropicFloorHeight | Gets or sets the anisotropic floor height for illuminating this appearance. |
| Property | Brightness | Gets or sets how emissive the material is for the Constant illumination type for this appearance. |
| Property | BumpAmplitude | Obsolete. Superseded by IRenderMaterial::BumpStrength . |
| Property | BumpBlend | Gets or sets the blend, which is the extent of the boundary between each bump and the surface, of the surface finish for this appearance. |
| Property | BumpDetail | Gets or sets the level of granularity for any surface finish for this appearance. |
| Property | BumpMap | Obsolete. Superseded by IRenderMaterial::SurfaceFinishShaderType . |
| Property | BumpRadius | Gets or sets the radius, which controls the relative size and spacing of bumps for dimpled and tread plate styles, of the surface finish for this appearance. |
| Property | BumpRoughHigh | Gets or sets the high threshold of the surface finish for this appearance. |
| Property | BumpRoughLow | Gets or sets the low threshold of the surface finish for this appearance. |
| Property | BumpScale | Gets or sets the scale for the surface-finish pattern incidence for this appearance. |
| Property | BumpSharpness | Gets or sets the sharpness, which influences the shape of the surface finish, of this appearance. |
| Property | BumpStrength | Gets or sets the amplitude of the surface layer for this appearance. |
| Property | BumpTextureFilename | Obsolete. Superseded by IRenderMaterial::SurfaceFinishFile. Gets or sets the path and file name of the pattern based on an image file for the surface finish of this appearance. |
| Property | BumpUseMappingScale | Gets or sets whether to use the material's scale and mapping for the surface finish of this appearance. |
| Property | CausticsCast | Gets or sets whether specular materials reflect caustic photons for illuminating this appearance. |
| Property | CausticsReceive | Gets or sets whether diffuse materials absorb caustic photons for illuminating this appearance. |
| Property | ColorForm | Gets or sets the number of colors required to describe the appearance . |
| Property | CustomHoleMeshFile | Gets or sets the custom hole mesh file. |
| Property | DensityOfHoles | Gets or sets the density of the holes of the mesh in corroded or eroded materials for illuminating this appearance. |
| Property | Diffuse | Gets or sets the intensity of a light source illuminating a surface from all directions without attenuation or shadowing for this appearance. |
| Property | DimpleSize | Gets or sets the dimple size. |
| Property | Direction1RotationAngle | Gets or sets the angle at which to rotate the texture relative to the horizontal axis for mapping this appearance. |
| Property | Direction2RotationAngle | Gets or sets the angle at which to rotate the texture relative to the vertical axis for mapping this appearance. |
| Property | DoubleSided | Gets or sets whether to enable shading from both sides of a surface when rendering a model using a ray-trace rendering engine. |
| Property | Emission | Gets or sets how much light is projected from the appearance. |
| Property | FaceWidth | Gets or sets the face width. |
| Property | FileName | Gets or sets the path and file name (. p2m ) of the appearance. |
| Property | FitHeight | Gets or sets whether to stretch the height of the appearance texture to the selected entity when mapping the appearance. |
| Property | FitWidth | Gets or sets whether to stretch the width of the appearance texture to the selected entity when mapping the appearance. |
| Property | FixedAspectRatio | Gets or sets whether the aspect ratio is fixed for mapping this appearance texture. |
| Property | GlobalIlluminationCast | Gets whether specular materials reflect photons for illuminating this appearance.. |
| Property | GlobalIlluminationReceive | Gets or sets whether diffuse materials absorb photons for illuminating this appearance. |
| Property | Glossy | Gets or sets the specular factor of the lights reflected by the appearance. |
| Property | Height | Gets or sets the height for mapping this appearance texture. |
| Property | HeightMirror | Gets or sets whether to flip the appearance texture about the selected direction vertically. |
| Property | HoleMeshSize | Gets or sets the hole mesh size. |
| Property | IgnoreMissingFile | Gets or sets whether to ignore any missing image file warnings. |
| Property | IlluminationShaderType | Gets or sets the type of illumination of the appearance. |
| Property | IndexOfRefraction | Gets or sets the index of refraction for illuminating this appearance. |
| Property | KnurlAngle | Gets or sets the knurl angle of this appearance. |
| Property | KnurlHeightCap | Gets or sets the maximum knurl height of this appearance. |
| Property | LinkToFile | Gets or sets whether to link instances of the appearance to an appearance file ( .p2m ). |
| Property | MappingType | Gets or sets the mapping type for this appearance. |
| Property | MaterialID | Not supported in SOLIDWORKS 2011 and later . Superseded by IRenderMaterial::GetMaterialIds . |
| Property | MetallicAmplitude | Gets or sets the amplitude of the metallic flakes for illuminating the appearance. |
| Property | MetallicFlakeMaterial | Gets or sets the metallic flake material for illuminating the appearance. |
| Property | MetallicMix | Gets or sets the metallic quality of a material for illuminating the appearance. |
| Property | MetallicRoughness | Gets or sets the size (coarseness) any highlights on the surface for illuminating the appearance. |
| Property | MetallicScale | Gets or sets the size of the metallic flakes in the metallic layer for illuminating the appearance. |
| Property | NSamples | Gets or sets the number of samples used to calculate the contribution of the glossy component for illuminating the appearance. |
| Property | ObjectAreaLight | Gets or sets whether the appearance is an object area light or whether it has realistic falloff, or both. |
| Property | OffsetLatitude | Gets or sets the offset latitude value for a spherical mapping type. |
| Property | OffsetLongitude | Gets or sets the offset longitude value for a spherical mapping type. |
| Property | PatternScale | Gets or sets the pattern scale of procedural textures for mapping the appearance. |
| Property | PrimaryColor | Gets or sets the primary color of the appearance. |
| Property | ProjectionReference | Gets or sets the projection direction for mapping the appearance. |
| Property | Reflectivity | Gets or sets the reflectivity for illuminating the appearance. |
| Property | RotationAngle | Gets or sets the angle by which to rotate the texture relative to the axes for mapping this appearance. |
| Property | Roughness | Gets or sets the specular spread (roughness) of the appearance. |
| Property | RoundSharpEdges | Gets or sets the value by which to round sharp edges when rendering a model using a ray-trace rendering engine. |
| Property | SecondaryColor | Gets or sets the secondary color of the appearance. |
| Property | Specular | Gets or sets the intensity of the light surface for illuminating the appearance. |
| Property | SpecularColor | Gets or sets the specular color for illuminating this appearance. |
| Property | SurfaceFinishFile | Gets or sets the path and file name of the pattern based on an image file for the surface finish of this appearance. |
| Property | SurfaceFinishFileNormalMap | Gets or sets whether to map the surface finish file image to the normal. |
| Property | SurfaceFinishShaderType | Gets or sets the type of surface finish for the appearance. |
| Property | TertiaryColor | Gets or sets the tertiary color of the appearance. |
| Property | TextureFilename | Gets or sets the path and filename of the texture for this appearance. |
| Property | ToonShaderTextureFilename | Gets or sets the path and filename for the toon shader texture file. |
| Property | Translucency | Gets or sets the degree to which the material is able to filter and diffuse light for illuminating the appearance. |
| Property | Transparency | Gets or sets the degree to which a material allows light to pass through for illuminating the appearance. |
| Property | Width | Gets or sets the width for mapping this appearance texture. |
| Property | WidthMirror | Gets or sets whether to flip the appearance texture about the selected direction horizontally. |
| Property | XPosition | Gets or sets the X offset direction for the appearance. |
| Property | YPosition | Gets or sets the Y offset direction for the appearance. |

[Top](#topBookmark)

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)

[IModelDocExtension::CreateRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateRenderMaterial.html)

[IModelDocExtension::GetRenderMaterialsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterialsCount.html)

[IModelDocExtension::UpdateRenderMaterialsInSceneGraph Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateRenderMaterialsInSceneGraph.html)

[IModelDocExtension::GetRenderCustomReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderCustomReferences.html)

[IModelDocExtension::GetRenderStockReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderStockReferences.html)
