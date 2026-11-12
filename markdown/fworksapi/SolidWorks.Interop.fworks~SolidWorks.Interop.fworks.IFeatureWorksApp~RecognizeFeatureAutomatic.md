---
title: "RecognizeFeatureAutomatic Method (IFeatureWorksApp)"
project: "FeatureWorks API Help"
interface: "IFeatureWorksApp"
member: "RecognizeFeatureAutomatic"
kind: "method"
source: "fworksapi/SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.IFeatureWorksApp~RecognizeFeatureAutomatic.html"
---

# RecognizeFeatureAutomatic Method (IFeatureWorksApp)

Recognizes imported features automatically in a SOLIDWORKS part document.

## Syntax

### Visual Basic (Declaration)

```vb
Function RecognizeFeatureAutomatic( _
   ByVal options As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureWorksApp
Dim options As System.Integer
Dim value As System.Integer

value = instance.RecognizeFeatureAutomatic(options)
```

### C#

```csharp
System.int RecognizeFeatureAutomatic(
   System.int options
)
```

### C++/CLI

```cpp
System.int RecognizeFeatureAutomatic(
   System.int options
)
```

### Parameters

- `options`: Automatic options as defined by [fwAutomaticRecognitionOptions_e](SOLIDWORKS.Interop.fworks~SOLIDWORKS.Interop.fworks.fwAutomaticRecognitionOptions_e.html)

### Return Value

Number of features recognized

## VBA Syntax

See [FeatureWorksApp::RecognizeFeatureAutomatic](ms-its:fworksapivb6.chm::/FeatureWorks~FeatureWorksApp~RecognizeFeatureAutomatic.html).

## Examples

[Recognizing Features Automatically (VBA)](Recognizing_Features_Automatically.htm)

## See Also

[IFeatureWorksApp Interface](SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.IFeatureWorksApp.html)
[IFeatureWorksApp Members](SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.IFeatureWorksApp_members.html)
[IFeatureWorksApp::RecognizeFeatureInteractive Method](SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.IFeatureWorksApp~RecognizeFeatureInteractive.html)

## Availability

FeatureWorks API 2004 FCS
