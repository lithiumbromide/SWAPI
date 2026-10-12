---
title: "Provider Property (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "Provider"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~Provider.html"
---

# Provider Property (IMacroFeatureData)

Gets or sets the error message to display in the What's Wrong dialog when a non-embedded macro feature fails to rebuild due to missing files.

## Syntax

### Visual Basic (Declaration)

```vb
Property Provider As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As System.String

instance.Provider = value

value = instance.Provider
```

### C#

```csharp
System.string Provider {get; set;}
```

### C++/CLI

```cpp
property System.String^ Provider {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Error message

## VBA Syntax

See [MacroFeatureData::Provider](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~Provider.html).

## Remarks

This property allows you to replace the generic error message that appears in the What's Wrong dialog with a more detailed error message when this non-embedded macro feature fails to load or rebuild due to missing files.

Possible causes of macro feature rebuild failure:

- The model contains this COM-based macro feature, but the rebuild, edit, and security callbacks exist in an add-in that SOLIDWORKS cannot locate.
- The model references this non-embedded macro feature which exists in a VBA macro that SOLIDWORKS cannot locate.
- Third-party DLLs, add-in files, or other files associated with this non-embedded macro feature are missing.

**NOTE:** All files required by embedded macro features are serialized with the model, so **File not found** errors do not occur for embedded macros, and this property need not be set for them.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::EmbedMacroFile Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EmbedMacroFile.html)
[IMacroFeatureData::MacroFileEmbedded Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~MacroFileEmbedded.html)
[IModelDocExtension::GetWhatsWrong Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetWhatsWrong.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
