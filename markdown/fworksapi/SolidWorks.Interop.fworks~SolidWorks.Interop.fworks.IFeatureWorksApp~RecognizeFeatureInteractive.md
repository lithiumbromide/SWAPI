---
title: "RecognizeFeatureInteractive Method (IFeatureWorksApp)"
project: "FeatureWorks API Help"
interface: "IFeatureWorksApp"
member: "RecognizeFeatureInteractive"
kind: "method"
source: "fworksapi/SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.IFeatureWorksApp~RecognizeFeatureInteractive.html"
---

# RecognizeFeatureInteractive Method (IFeatureWorksApp)

Recognizes imported features interactively in a SOLIDWORKS part document.

## Syntax

### Visual Basic (Declaration)

```vb
Function RecognizeFeatureInteractive( _
   ByVal FeatureType As System.String, _
   ByVal options As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureWorksApp
Dim FeatureType As System.String
Dim options As System.Integer
Dim value As System.Boolean

value = instance.RecognizeFeatureInteractive(FeatureType, options)
```

### C#

```csharp
System.bool RecognizeFeatureInteractive(
   System.string FeatureType,
   System.int options
)
```

### C++/CLI

```cpp
System.bool RecognizeFeatureInteractive(
   System.String^ FeatureType,
   System.int options
)
```

### Parameters

- `FeatureType`: Type of body or sheet metal feature to recognize
- `options`: Interactive options as defined by [fwInteractiveRecognitionOptions_e](SOLIDWORKS.Interop.fworks~SOLIDWORKS.Interop.fworks.fwInteractiveRecognitionOptions_e.html)

### Return Value

True if the feature is recognized, false if not

## VBA Syntax

See [FeatureWorksApp::RecognizeFeatureInteractive](ms-its:fworksapivb6.chm::/FeatureWorks~FeatureWorksApp~RecognizeFeatureInteractive.html).

## Examples

[Recognizing Features Interactively (VBA)](Recognizing_Features_Interactively.htm)

## See Also

[IFeatureWorksApp Interface](SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.IFeatureWorksApp.html)
[IFeatureWorksApp Members](SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.IFeatureWorksApp_members.html)
[IFeatureWorksApp::RecognizeFeatureAutomatic Method](SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.IFeatureWorksApp~RecognizeFeatureAutomatic.html)

## Availability

FeatureWorks API 2004 FCS
