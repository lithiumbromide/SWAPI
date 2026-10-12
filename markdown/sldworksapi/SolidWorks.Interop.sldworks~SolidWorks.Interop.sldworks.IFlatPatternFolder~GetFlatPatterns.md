---
title: "GetFlatPatterns Method (IFlatPatternFolder)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFolder"
member: "GetFlatPatterns"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFolder~GetFlatPatterns.html"
---

# GetFlatPatterns Method (IFlatPatternFolder)

Gets the flat-pattern features in this folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFlatPatterns() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFolder
Dim value As System.Object

value = instance.GetFlatPatterns()
```

### C#

```csharp
System.object GetFlatPatterns()
```

### C++/CLI

```cpp
System.Object^ GetFlatPatterns();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)s

## VBA Syntax

See [FlatPatternFolder::GetFlatPatterns](ms-its:sldworksapivb6.chm::/sldworks~FlatPatternFolder~GetFlatPatterns.html).

## Examples

See [IFlatPatternFolder](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFlatPatternFolder.html) examples.

## See Also

[IFlatPatternFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFolder.html)
[IFlatPatternFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFolder_members.html)
[IFlatPatternFolder::GetFlatPatternCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFolder~GetFlatPatternCount.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
