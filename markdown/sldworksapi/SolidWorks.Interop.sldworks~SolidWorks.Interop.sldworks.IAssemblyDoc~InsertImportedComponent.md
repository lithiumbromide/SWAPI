---
title: "InsertImportedComponent Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "InsertImportedComponent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertImportedComponent.html"
---

# InsertImportedComponent Method (IAssemblyDoc)

Inserts a third-party native CAD part or assembly into the current configuration of this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertImportedComponent( _
   ByVal FileName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByRef CompInserted As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim FileName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim CompInserted As System.Object
Dim value As System.Integer

value = instance.InsertImportedComponent(FileName, X, Y, Z, CompInserted)
```

### C#

```csharp
System.int InsertImportedComponent(
   System.string FileName,
   System.double X,
   System.double Y,
   System.double Z,
   out System.object CompInserted
)
```

### C++/CLI

```cpp
System.int InsertImportedComponent(
   System.String^ FileName,
   System.double X,
   System.double Y,
   System.double Z,
   [Out] System.Object^ CompInserted
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Full path name of the third-party native CAD file to insert
- `X`: X-coordinate of the component center
- `Y`: Y-coordinate of the component center
- `Z`: Z-coordinate of the component center
- `CompInserted`: [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html); null or Nothing if unsuccessful

### Return Value

Error code as defined in [sw3DInterconnectImportErrors_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DInterconnectImportErrors_e.html)

## VBA Syntax

See [AssemblyDoc::InsertImportedComponent](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~InsertImportedComponent.html).

## Remarks

To successfully use this method, you must first turn on 3D Interconnect by either:

- Setting **Tools > Options > System Options > Import > Enable 3D Interconnect**

- or -

- Calling [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html)([swUserPreferenceToggle_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swMultiCAD_Enable3DInterconnect, True)

To edit the imported assembly, save the SOLIDWORKS assembly and then use [IFeature::GetImportedFeatureParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetImportedFeatureParameters.html) and [IFeature::SetImportedFeatureParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetImportedFeatureParameters.html).

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html) Remarks.

If 3D Interconnect is turned off, use [IAssemblyDoc::AddComponent5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponent5.html) instead of this method.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[ISldWorks::LoadFile4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.html)
[IPartDoc::InsertImportedFeature Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertImportedFeature.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
