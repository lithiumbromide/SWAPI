---
title: "EmbedMacroFile Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "EmbedMacroFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EmbedMacroFile.html"
---

# EmbedMacroFile Method (IMacroFeatureData)

Sets whether to embed the macro file in the model with the macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function EmbedMacroFile() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As System.Boolean

value = instance.EmbedMacroFile()
```

### C#

```csharp
System.bool EmbedMacroFile()
```

### C++/CLI

```cpp
System.bool EmbedMacroFile();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True to embed the macro file in the model with the macro feature, false to not

## VBA Syntax

See [MacroFeatureData::EmbedMacroFile](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~EmbedMacroFile.html).

## Remarks

Call [IMacroFeatureData::MacroFileEmbedded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~MacroFileEmbedded.html) to determine if the macro file is embedded with the macro feature.

If this property is set to false, you should specify a detailed error message to display in the What's Wrong dialog when SOLIDWORKS fails to find files during macro feature load or rebuild. Specify this error message using [IMacroFeatureData:Provider](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~Provider.html).

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
