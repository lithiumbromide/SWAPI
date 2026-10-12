---
title: "CurrentConfiguration Property (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "CurrentConfiguration"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~CurrentConfiguration.html"
---

# CurrentConfiguration Property (IMacroFeatureData)

Gets the macro feature configuration being rebuilt.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurrentConfiguration As Configuration
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As Configuration

value = instance.CurrentConfiguration
```

### C#

```csharp
Configuration CurrentConfiguration {get;}
```

### C++/CLI

```cpp
property Configuration^ CurrentConfiguration {
   Configuration^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Configuration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration.html) being rebuilt

## VBA Syntax

See [MacroFeatureData::CurrentConfiguration](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~CurrentConfiguration.html).

## Examples

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2
