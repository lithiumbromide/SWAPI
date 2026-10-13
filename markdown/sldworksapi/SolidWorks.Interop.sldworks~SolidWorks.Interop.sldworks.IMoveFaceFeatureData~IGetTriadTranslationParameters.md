---
title: "IGetTriadTranslationParameters Method (IMoveFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData"
member: "IGetTriadTranslationParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~IGetTriadTranslationParameters.html"
---

# IGetTriadTranslationParameters Method (IMoveFaceFeatureData)

Gets the translation parameters for this Move Face feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTriadTranslationParameters() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveFaceFeatureData
Dim value As System.Double

value = instance.IGetTriadTranslationParameters()
```

### C#

```csharp
System.double IGetTriadTranslationParameters()
```

### C++/CLI

```cpp
System.double IGetTriadTranslationParameters();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of three doubles that are the X, Y, and Z translation parameters

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html)
[IMoveFaceFeatureData::ISetTriadTranslationParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~ISetTriadTranslationParameters.html)
[IMoveFaceFeatureData::TriadTranslationParameters Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~TriadTranslationParameters.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
