---
title: "ImportStudyFeatures Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "ImportStudyFeatures"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~ImportStudyFeatures.html"
---

# ImportStudyFeatures Method (ICWStudy)

Imports the study features of the specified component's study into this study.

## Syntax

### Visual Basic (Declaration)

```vb
Function ImportStudyFeatures( _
   ByVal SComponent As System.String, _
   ByVal SStudy As System.String, _
   ByVal SConfig As System.String, _
   ByVal NFilter As System.Integer, _
   ByVal BPropagate As System.Boolean, _
   ByRef ErrorCode As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim SComponent As System.String
Dim SStudy As System.String
Dim SConfig As System.String
Dim NFilter As System.Integer
Dim BPropagate As System.Boolean
Dim ErrorCode As System.Integer
Dim value As System.Boolean

value = instance.ImportStudyFeatures(SComponent, SStudy, SConfig, NFilter, BPropagate, ErrorCode)
```

### C#

```csharp
System.bool ImportStudyFeatures(
   System.string SComponent,
   System.string SStudy,
   System.string SConfig,
   System.int NFilter,
   System.bool BPropagate,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.bool ImportStudyFeatures(
   System.String^ SComponent,
   System.String^ SStudy,
   System.String^ SConfig,
   System.int NFilter,
   System.bool BPropagate,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SComponent`: Name of the assembly component from whose study to import study features
- `SStudy`: Name of SComponent's study from which to import study features
- `SConfig`: Name of SComponent's configuration
- `NFilter`: Study features to import as defined in [swsImportStudyFeaturesFilterType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsImportStudyFeaturesErrorCode_e.html)
- `BPropagate`: True to propagate imported study features to components in this study that are similar to SComponent, false to not
- `ErrorCode`: Result code as defined in [swsImportStudyFeaturesErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsImportStudyFeaturesErrorCode_e.html)

### Return Value

VARIANT_TRUE (-1) if successful, VARIANT_FALSE (0) if not

## VBA Syntax

See [CWStudy::ImportStudyFeatures](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~ImportStudyFeatures.html).

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
