---
title: "MacroFileEmbedded Property (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "MacroFileEmbedded"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~MacroFileEmbedded.html"
---

# MacroFileEmbedded Property (IMacroFeatureData)

Gets whether the macro file is embedded ini the model with the macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MacroFileEmbedded As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As System.Boolean

value = instance.MacroFileEmbedded
```

### C#

```csharp
System.bool MacroFileEmbedded {get;}
```

### C++/CLI

```cpp
property System.bool MacroFileEmbedded {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the macro file is embedded in the model with the macro feature, false if not

## VBA Syntax

See [MacroFeatureData::MacroFileEmbedded](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~MacroFileEmbedded.html).

## Remarks

If this property is false, you should specify a detailed error message to display in the What's Wrong dialog when SOLIDWORKS fails to find files during macro feature load or rebuild. To specify this error message, use [IMacroFeatureData:Provider](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~Provider.html).

Call [IMacroFeatureData::EmbedMacroFile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~EmbedMacroFile.html) to set whether to embed the macro file with the macro feature.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
