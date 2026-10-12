---
title: "IImportStepData Interface"
project: "SOLIDWORKS API Help"
interface: "IImportStepData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportStepData.html"
---

# IImportStepData Interface

Allows you to specify values when importing STEP data.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IImportStepData
```

### Visual Basic (Usage)

```vb
Dim instance As IImportStepData
```

### C#

```csharp
public interface IImportStepData
```

### C++/CLI

```cpp
public interface class IImportStepData
```

## VBA Syntax

See [ImportStepData](ms-its:sldworksapivb6.chm::/sldworks~ImportStepData.html).

## Examples

[Import STEP File (C#)](Import_STEP_File_Example_CSharp.htm)
[Import STEP File (VB.NET)](Import_STEP_File_Example_VBNET.htm)
[Import STEP File (VBA)](Import_STEP_File_Example_VB.htm)

## Remarks

When IImportStepData is initialized, the current default environment setting, [swImportStepConfigData](ms-its:swconst.chm::/FileOpenOptionsGeneral.htm), initializes IImportStepData::MapConfigurationData unless you explicitly set IImportStepData::MapConfigurationData. Then the IImportStepData::MapConfigurationData setting overrides swImportStepConfigData for this import only.

## Accessors

[ISldWorks::GetImportFileData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetImportFileData.html)

## Access Diagram

[ImportStepData](SWObjectModel.pdf#ImportStepData)

## See Also

[IImportStepData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportStepData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
