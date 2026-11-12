---
title: "SetPerformanceOptions Method (IFeatureWorksApp)"
project: "FeatureWorks API Help"
interface: "IFeatureWorksApp"
member: "SetPerformanceOptions"
kind: "method"
source: "fworksapi/SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.IFeatureWorksApp~SetPerformanceOptions.html"
---

# SetPerformanceOptions Method (IFeatureWorksApp)

Sets the desired performance options.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPerformanceOptions( _
   ByVal options As System.Short _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureWorksApp
Dim options As System.Short
Dim value As System.Boolean

value = instance.SetPerformanceOptions(options)
```

### C#

```csharp
System.bool SetPerformanceOptions(
   System.short options
)
```

### C++/CLI

```cpp
System.bool SetPerformanceOptions(
   System.short options
)
```

### Parameters

- `options`: Performance options as defined by [fwPerformanceOptions_e](SOLIDWORKS.Interop.fworks~SOLIDWORKS.Interop.fworks.fwPerformanceOptions_e.html)

### Return Value

True if the performance options are set, false if not

## VBA Syntax

See [FeatureWorksApp::SetPerformanceOptions](ms-its:fworksapivb6.chm::/FeatureWorks~FeatureWorksApp~SetPerformanceOptions.html).

## See Also

[IFeatureWorksApp Interface](SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.IFeatureWorksApp.html)
[IFeatureWorksApp Members](SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.IFeatureWorksApp_members.html)

## Availability

FeatureWorks API 2004 FCS
