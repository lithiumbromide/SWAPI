---
title: "InsertImportedFeature Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "InsertImportedFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertImportedFeature.html"
---

# InsertImportedFeature Method (IPartDoc)

Inserts a third-party native CAD file into this part.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertImportedFeature( _
   ByVal FileName As System.String, _
   ByRef Errors As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim FileName As System.String
Dim Errors As System.Integer
Dim value As System.Object

value = instance.InsertImportedFeature(FileName, Errors)
```

### C#

```csharp
System.object InsertImportedFeature(
   System.string FileName,
   out System.int Errors
)
```

### C++/CLI

```cpp
System.Object^ InsertImportedFeature(
   System.String^ FileName,
   [Out] System.int Errors
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Full path name of the third-party native CAD file to insert
- `Errors`: Error code as defined in [swFileLoadError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileLoadError_e.html)

### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html) if successful; null or Nothing otherwise

## VBA Syntax

See [PartDoc::InsertImportedFeature](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~InsertImportedFeature.html).

## Remarks

To successfully use this method, you must first turn on 3D Interconnect by either:

- Setting **Tools > Options > System Options > Import > Enable 3D Interconnect**

- or -

- Calling [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html)([swUserPreferenceToggle_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swMultiCAD_Enable3DInterconnect, True)

The feature is imported and positioned relative to the origin using coordinates of the imported file. To edit the feature, use [IFeature::GetImportedFeatureParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetImportedFeatureParameters.html) and [IFeature::SetImportedFeatureParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetImportedFeatureParameters.html).

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html) Remarks.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[ISldWorks::LoadFile4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.html)
[IAssemblyDoc::InsertImportedComponent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertImportedComponent.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
