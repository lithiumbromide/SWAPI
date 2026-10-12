---
title: "CreateFeatures Method (IFeatureWorksApp)"
project: "FeatureWorks API Help"
interface: "IFeatureWorksApp"
member: "CreateFeatures"
kind: "method"
source: "fworksapi/SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.IFeatureWorksApp~CreateFeatures.html"
---

# CreateFeatures Method (IFeatureWorksApp)

Creates recognized imported features in a SOLIDWORKS part document.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFeatures( _
   ByVal CreationOptions As System.Short _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureWorksApp
Dim CreationOptions As System.Short
Dim value As System.Boolean

value = instance.CreateFeatures(CreationOptions)
```

### C#

```csharp
System.bool CreateFeatures(
   System.short CreationOptions
)
```

### C++/CLI

```cpp
System.bool CreateFeatures(
   System.short CreationOptions
)
```

### Parameters

- `CreationOptions`: Options as defined by [fwFeatureCreationOptions_e](SOLIDWORKS.Interop.fworks~SOLIDWORKS.Interop.fworks.fwFeatureCreationOptions_e.html)

### Return Value

True if the feature is created, false if not

## VBA Syntax

See [FeatureWorksApp::CreateFeatures](ms-its:fworksapivb6.chm::/FeatureWorks~FeatureWorksApp~CreateFeatures.html).

## Examples

[Recognizing Features Automatically (VBA)](Recognizing_Features_Automatically.htm)
[Recognizing Features Interactively (VBA)](Recognizing_Features_Interactively.htm)

## See Also

[IFeatureWorksApp Interface](SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.IFeatureWorksApp.html)
[IFeatureWorksApp Members](SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.IFeatureWorksApp_members.html)
[IFeatureWorksApp::RecognizeFeatureAutomatic Method](SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.IFeatureWorksApp~RecognizeFeatureAutomatic.html)
[IFeatureWorksApp::RecognizeFeatureInteractive Method](SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.IFeatureWorksApp~RecognizeFeatureInteractive.html)

## Availability

FeaturesWorks API 2004 FCS
