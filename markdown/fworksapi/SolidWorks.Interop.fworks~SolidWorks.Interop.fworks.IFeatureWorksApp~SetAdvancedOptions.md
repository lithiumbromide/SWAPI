---
title: "SetAdvancedOptions Method (IFeatureWorksApp)"
project: "FeatureWorks API Help"
interface: "IFeatureWorksApp"
member: "SetAdvancedOptions"
kind: "method"
source: "fworksapi/SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.IFeatureWorksApp~SetAdvancedOptions.html"
---

# SetAdvancedOptions Method (IFeatureWorksApp)

Set the specified advanced options.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAdvancedOptions( _
   ByVal options As System.Short _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureWorksApp
Dim options As System.Short
Dim value As System.Boolean

value = instance.SetAdvancedOptions(options)
```

### C#

```csharp
System.bool SetAdvancedOptions(
   System.short options
)
```

### C++/CLI

```cpp
System.bool SetAdvancedOptions(
   System.short options
)
```

### Parameters

- `options`: Advanced options as defined in [fwAdvancedOptions_e](SOLIDWORKS.Interop.fworks~SOLIDWORKS.Interop.fworks.fwAdvancedOptions_e.html)

### Return Value

True if the advanced options are set, false if not

## VBA Syntax

See [FeatureWorksApp::SetAdvancedOptions](ms-its:fworksapivb6.chm::/FeatureWorks~FeatureWorksApp~SetAdvancedOptions.html).

## See Also

[IFeatureWorksApp Interface](SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.IFeatureWorksApp.html)
[IFeatureWorksApp Members](SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.IFeatureWorksApp_members.html)

## Availability

FeatureWorks API 2009 FCS
