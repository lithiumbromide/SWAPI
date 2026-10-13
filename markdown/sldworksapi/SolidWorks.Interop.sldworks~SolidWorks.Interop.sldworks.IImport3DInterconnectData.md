---
title: "IImport3DInterconnectData Interface"
project: "SOLIDWORKS API Help"
interface: "IImport3DInterconnectData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html"
---

# IImport3DInterconnectData Interface

Allows access to 3D Interconnect feature data.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IImport3DInterconnectData
```

### Visual Basic (Usage)

```vb
Dim instance As IImport3DInterconnectData
```

### C#

```csharp
public interface IImport3DInterconnectData
```

### C++/CLI

```cpp
public interface class IImport3DInterconnectData
```

## VBA Syntax

See [Import3DInterconnectData](ms-its:sldworksapivb6.chm::/sldworks~Import3DInterconnectData.html).

## Examples

[Use 3D Interconnect to Import Third-Party Native CAD Files (C#)](Import3DInterconnect_Example_CSharp.htm)

## Remarks

This interface requires 3D Interconnect. Enable 3D Interconnect by:

- Setting **Tools > Options > System Options > Import > Enable 3D Interconnect**.

- or -

- Calling [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html)([swUserPreferenceToggle_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swMultiCAD_Enable3DInterconnect, True).

Access this interface after importing a third-party native CAD file into:

- an existing SOLIDWORKS part using [IPartDoc::InsertImportedFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertImportedFeature.html).
- an existing SOLIDWORKS assembly using [IAssemblyDoc::InsertImportedComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertImportedComponent.html).
- a new SOLIDWORKS part using [ISldWorks::LoadFile4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.html).
- a new SOLIDWORKS assembly using ISldWorks::LoadFile4.

Use [IFeature::Is3DInterconnectFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Is3DInterconnectFeature.html) to determine whether a feature is a 3D Interconnect feature and whether this interface applies.

ISldWorks::LoadFile4 imports into the appropriate native SOLIDWORKS part or assembly as follows:

- For both imported parts and assemblies, you can:

  - Determine whether an update is required ([IFeature::Is3DInterconnectUpdateAvailable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Is3DInterconnectUpdateAvailable.html)) and update the model ([IFeature::Update3DInterconnectModel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Update3DInterconnectModel.html)).
  - Edit the imported data using this interface, its accessor (IFeature::GetImportedFeatureParameters), or [IFeature::SetImportedFeatureParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetImportedFeatureParameters.html).
  - Break the link to the original third-party native CAD file using [IFeature::BreakLink](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~BreakLink.html). After you break a link, all references to the original CAD file are lost, and you can no longer change the features to transfer from the original file.
- For imported parts only, the native SOLIDWORKS file created is a copy of the original non-native file. The copy retains an external reference to the original third-party native CAD file. If the original CAD file is modified in its orginal application, the SOLIDWORKS copy can be updated to import those changes. Changes to the SOLIDWORKS copy do not propagate back to the original CAD file.
- For imported assemblies only, after import you must save the new SOLIDWORKS assembly in order for SOLIDWORKS to import and create a copy to edit. Only after saving the new SOLIDWORKS assembly can you edit the imported top-level assembly or break its reference links. Editing lower-level imported components or individually breaking their reference links is not supported.

3D Interconnect supports the following third-party native CAD file formats and versions:

- ACIS: .sat, .sab, .asat, .asab for r1 - 2018 1.0
- Autodesk® Inventor: .ipt for V6-V2018, .iam for V11 - V2018
- CATIA® V5: .CATPart, .CATProduct for V5R8 - V5-6R2017
- IGES: .igs, .iges for up to 5.3
- JT: .jt for JT 8.x, 9.x, and 10.x
- PTC®: .prt, .prt.*, .asm.* for Pro/ENGINEER® 16 - Creo 4.0
- Solid Edge®: .par, .asm, .psm for V18 - ST10
- STEP: .stp, .step for AP203, AP214, AP242
- NX™ software: .prt for UG 11 - NX 11

The transfer properties of this interface apply to a subset of supported third-party native CAD files (e.g., Inventor, CATIA V5, Creo, NX, Solid Edge, and a few others). The types of properties that can be imported vary with file format. See the **SOLIDWORKS 3D Interconnect** topics in the SOLIDWORKS Design user-interface help for specific information.

## Accessors

[IFeature::GetImportedFeatureParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetImportedFeatureParameters.html)

## Access Diagram

[Import3DInterconnectData](SWObjectModel.pdf#Import3DInterconnectData)

## See Also

[IImport3DInterconnectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
