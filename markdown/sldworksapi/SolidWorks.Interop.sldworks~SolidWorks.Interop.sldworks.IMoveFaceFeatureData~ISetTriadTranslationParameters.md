---
title: "ISetTriadTranslationParameters Method (IMoveFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData"
member: "ISetTriadTranslationParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~ISetTriadTranslationParameters.html"
---

# ISetTriadTranslationParameters Method (IMoveFaceFeatureData)

Sets the translation parameters for this Move Face feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetTriadTranslationParameters( _
   ByRef TranslationParameters As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveFaceFeatureData
Dim TranslationParameters As System.Double

instance.ISetTriadTranslationParameters(TranslationParameters)
```

### C#

```csharp
void ISetTriadTranslationParameters(
   ref System.double TranslationParameters
)
```

### C++/CLI

```cpp
void ISetTriadTranslationParameters(
   System.double% TranslationParameters
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TranslationParameters`: - in-process, unmanaged C++: pointer to an array of three doubles for the X, Y, and Z translation parameters
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html)
[IMoveFaceFeatureData::IGetTriadTranslationParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~IGetTriadTranslationParameters.html)
[IMoveFaceFeatureData::TriadTranslationParameters Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~TriadTranslationParameters.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
