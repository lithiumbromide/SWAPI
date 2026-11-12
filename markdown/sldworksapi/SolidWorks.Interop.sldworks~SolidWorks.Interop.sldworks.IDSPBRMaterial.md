---
title: "IDSPBRMaterial Interface"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html"
---

# IDSPBRMaterial Interface

Allows access to Dassault Systemes Physically Based Rendering (DSPBR) material object.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IDSPBRMaterial
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
```

### C#

```csharp
public interface IDSPBRMaterial
```

### C++/CLI

```cpp
public interface class IDSPBRMaterial
```

## VBA Syntax

See [DSPBRMaterial](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial.html).

## Remarks

The Enterprise PBR Shading Model (DSPBR) is a high-quality, easy-to-use material optimized for performance in real-time and interactive scenarios, suitable for rasterization and ray tracing. Inspired by the Disney Principled BRDF and the Unreal Shading Model, it combines a metallic and a dielectric bidirectional scattering distribution function (BSDF), including transparency for thin-walled and volumetric objects. In addition, it provides effects like emission, clear coat, metallic flakes and sheen to cover a wide range of appearances.

For the DSPBR design rationale and detailed mathematical description in terms of BSDF and related concepts, open https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2025x.md.html in an internet browser.

The properties in IDSPBRMaterial map to the appearance settings in the user interface, if the DSPBR appearance is activated in the user interface.

To activate the DSPBR appearance in the SOLIDWORKS Design user interface:

1. Select **System Options > Display > Appearance Visual Style > DSPBR (Dassault Systemes Physically Based Rendering)**.
2. Open a model.
3. Select MMGS in the unit system dropdown below the graphics area.
4. Click **Edit Appearance** in the graphics toolbar.
5. Click the **DSPBR** tab in the FeatureManager.
6. Select **Enerprise PBR Shading Model** from the DSPBR Appearance Type dropdown.

## Accessors

[IRenderMaterial::GetDSPBRMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetDSPBRMaterial.html)

## Access Diagram

[DSPBRMaterial](SWObjectModel.pdf#DSPBRMaterial)

## See Also

[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
