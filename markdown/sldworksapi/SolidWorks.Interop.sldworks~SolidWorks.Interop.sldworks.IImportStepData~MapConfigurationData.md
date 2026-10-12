---
title: "MapConfigurationData Property (IImportStepData)"
project: "SOLIDWORKS API Help"
interface: "IImportStepData"
member: "MapConfigurationData"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportStepData~MapConfigurationData.html"
---

# MapConfigurationData Property (IImportStepData)

Gets or sets whether to import the STEP file configuration data plus geometric data or geometric data only.

## Syntax

### Visual Basic (Declaration)

```vb
Property MapConfigurationData As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImportStepData
Dim value As System.Boolean

instance.MapConfigurationData = value

value = instance.MapConfigurationData
```

### C#

```csharp
System.bool MapConfigurationData {get; set;}
```

### C++/CLI

```cpp
property System.bool MapConfigurationData {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import the STEP file configuration data plus geometric data, false to import geometric data only

## VBA Syntax

See [ImportStepData::MapConfigurationData](ms-its:sldworksapivb6.chm::/sldworks~ImportStepData~MapConfigurationData.html).

## Examples

[Import STEP File (C#)](Import_STEP_File_Example_CSharp.htm)
[Import STEP File (VB.NET)](Import_STEP_File_Example_VBNET.htm)
[Import STEP File (VBA)](Import_STEP_File_Example_VB.htm)

## Remarks

If this property is not set, then the current default environment setting, [swImportStepConfigData](ms-its:swconst.chm::/FileOpenOptionsGeneral.htm), is used. If this property is set, its setting overrides the swImportStepConfigData setting for this import only.

## See Also

[IImportStepData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportStepData.html)
[IImportStepData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportStepData_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
