---
title: "InsertMacroFeature3 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertMacroFeature3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMacroFeature3.html"
---

# InsertMacroFeature3 Method (IFeatureManager)

Inserts a macro feature in this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMacroFeature3( _
   ByVal BaseName As System.String, _
   ByVal ProgId As System.String, _
   ByVal MacroMethods As System.Object, _
   ByVal ParamNames As System.Object, _
   ByVal ParamTypes As System.Object, _
   ByVal ParamValues As System.Object, _
   ByVal DimTypes As System.Object, _
   ByVal DimValues As System.Object, _
   ByVal EditBodies As System.Object, _
   ByVal IconFiles As System.Object, _
   ByVal Options As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim BaseName As System.String
Dim ProgId As System.String
Dim MacroMethods As System.Object
Dim ParamNames As System.Object
Dim ParamTypes As System.Object
Dim ParamValues As System.Object
Dim DimTypes As System.Object
Dim DimValues As System.Object
Dim EditBodies As System.Object
Dim IconFiles As System.Object
Dim Options As System.Integer
Dim value As Feature

value = instance.InsertMacroFeature3(BaseName, ProgId, MacroMethods, ParamNames, ParamTypes, ParamValues, DimTypes, DimValues, EditBodies, IconFiles, Options)
```

### C#

```csharp
Feature InsertMacroFeature3(
   System.string BaseName,
   System.string ProgId,
   System.object MacroMethods,
   System.object ParamNames,
   System.object ParamTypes,
   System.object ParamValues,
   System.object DimTypes,
   System.object DimValues,
   System.object EditBodies,
   System.object IconFiles,
   System.int Options
)
```

### C++/CLI

```cpp
Feature^ InsertMacroFeature3(
   System.String^ BaseName,
   System.String^ ProgId,
   System.Object^ MacroMethods,
   System.Object^ ParamNames,
   System.Object^ ParamTypes,
   System.Object^ ParamValues,
   System.Object^ DimTypes,
   System.Object^ DimValues,
   System.Object^ EditBodies,
   System.Object^ IconFiles,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BaseName`: Name of the base feature (see **Remarks**)
- `ProgId`: COM or .NET callback object; empty string if VBA (see Remarks)
- `MacroMethods`: Array of strings of size 9 only for VBA; "" otherwise (see Remarks)
- `ParamNames`: Array of strings of the names of the parameters
- `ParamTypes`: Array of the types of parameters of size paramCount as defined by [swMacroFeatureParamType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMacroFeatureParamType_e.html)
- `ParamValues`: Array of strings of the values of parameters
- `DimTypes`: Array of the types of dimensions as defined by [swDimensionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionType_e.html) (see **Remarks**)
- `DimValues`: Array of values of the dimensions
- `EditBodies`: Array of [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) objects to modify in the macro feature
- `IconFiles`: Array of strings of the files names for the icons (see **Remarks**)
- `Options`: Placement of the macro feature in the FeatureManager design tree as defined by [swMacroFeatureOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMacroFeatureOptions_e.html) (see **Remarks**)

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertMacroFeature3](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertMacroFeature3.html).

## Examples

[Create Macro Feature Subfeature (VBA)](Create_Macro_Feature_Subfeature_Example_VB.htm)
[Create Multibody Macro Feature (VBA)](Create_Multibody_Macro_Feature_Example_VB.htm)
[Create Multibody Macro Feature (VB.NET)](Create_Multibody_Macro_Feature_Example_VBNET.htm)
[Create Multibody Macro Feature (C#)](Create_Multibody_Macro_Feature_Example_CSharp.htm)

## Remarks

**BaseName**

- The argument BaseName is serialized within the feature and cannot be changed.
- You can find out the name of the base feature by using [IMacroFeatureData::GetBaseName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~GetBaseName.html).
- The BaseName argument is also used to generate the name of the feature when the feature is first created.

**ProgId**

| If creating a macro feature using... | Then ProgId is... |
| --- | --- |
| COM callbacks | The name of the program ID for the component that implements the COM callback methods. The object that is represented by ProgID must support the ISwComFeature interface. InsertMacroFeature3 ("Sample", "Sample.MyFeature", _ Nothing, paramNames, paramTypes, _ paramValues, dimTypes, dimValues, _ editBodies, iconFiles, _ swMacroFeatureByDefault) In the COM server, the Sample.Feature class is derived from ISwComFeature and implements rebuild , edit , and security functions. |
| VBA | An empty string. InsertMacroFeature3("Sample", "",...) |
| .NET add-in callbacks | The name of the class that implements the .NET callbacks and ISwComFeature. InsertMacroFeature3("Sample", " project_name.class_module ",...) |

**MacroMethods**

The macroMethods argument is implemented for VBA only. The array of nine strings consists of the following values:

1. Filename - File executed during feature generation.
2. Module - Source module executed during feature generation.
3. Procedure - Source procedure executed during feature generation.
4. Filename - File executed after edit definition is selected.
5. Module - Source module executed after edit definition is selected.
6. Procedure - Source procedure executed after edit definition is selected.
7. Filename - File executed while querying security; optional, see the next paragraph.
8. Module - Source Module executed while querying security; optional, see the next paragraph.
9. Procedure - Source Procedure executed while querying security; optional, see the next paragraph.

Filename should be the full pathname to the macro file. If the procedure resides in the same macro file that calls IFeatureManager::InsertMacroFeature3, then a call to [ISldWorks::GetCurrentMacroPathName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetCurrentMacroPathName.html) provides all of the information necessary for the Filename.

[IModelDoc2::ListAuxiliaryExternalFileReferences](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferences.html) returns an array containing the names of the features that include external references and an array containing the names of the external files for Filename elements 1, 4, and 7 in the array.

The list of:

- features can contain duplicates, if the macro feature uses more than one procedure.
- file names can contain duplicates if:

  - the procedures are implemented in the same macro file.
  - more than one instance of the same macro feature is present.

If a security procedure is not used, then Filename, Module, and Procedure must all be empty strings.

Procedure names must have an swm prefix in the name. This prefix identifies the procedures to execute.

**DimTypes**

Only these dimension types are supported by this method:

- swAngularDimension
- swLinearDimension
- swRadialDimension

**IconFiles**

The array of the file names for the icons can contain either three or nine strings.

| Number of strings in array | Types of images in this order | Image format and sizes |
| --- | --- | --- |
| Three | Regular Suppressed Highlighted | Windows bitmap ( *.bmp ) format 16 pixels wide X 18 pixels high |
| Nine NOTES: This size array is only valid for macro features created in parts, assemblies, and drawings in SOLIDWORKS 2017 and later. SOLIDWORKS displays the appropriate images based on the current DPI setting of the display device. | Regular small Suppressed small Highlighted small Regular medium Suppressed medium Highlighted medium Regular large Suppressed large Highlighted large | Windows bitmap ( *.bmp ) format Recommended sizes are: Small: 20 pixels wide X 20 pixels high Medium: 32 pixels wide X 32 pixels high Large: 40 pixels wide X 40 pixels high |

You can specify either the full path name or just the file name for the strings; for example, c:\bitmaps\icon1.bmp or icon1.bmp.

**Options**

swMacroFeatureOptions_e.swMacroFeatureEmbedMacroFile is not supported by programming languages for the Microsoft .NET Framework; for example, not supported by C#, Visual Basic .NET, or Managed C++.

See [Overview of Macro Features](sldworksAPIProgGuide.chm::/Macro_Features/Overview_of_Macro_Features.htm) for more information.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::IInsertMacroFeature3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMacroFeature3.html)
[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
