---
title: "SaveWithPartGrouping Method (IVisualizeAddinManager2)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IVisualizeAddinManager2"
member: "SaveWithPartGrouping"
kind: "method"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2~SaveWithPartGrouping.html"
---

# SaveWithPartGrouping Method (IVisualizeAddinManager2)

Exports the currently loaded SOLIDWORKS model to a Visualize Project file (***.SVPJ**).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SaveWithPartGrouping( _
   ByVal filename As System.String, _
   ByVal partGroupingMode As PartGroupingMode_e _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IVisualizeAddinManager2
Dim filename As System.String
Dim partGroupingMode As PartGroupingMode_e

instance.SaveWithPartGrouping(filename, partGroupingMode)
```

### C#

```csharp
void SaveWithPartGrouping(
   System.string filename,
   PartGroupingMode_e partGroupingMode
)
```

### C++/CLI

```cpp
void SaveWithPartGrouping(
   System.String^ filename,
   PartGroupingMode_e partGroupingMode
)
```

### Parameters

- `filename`: Full path name where the **.SVPJ** file is saved
- `partGroupingMode`: How geometry from SOLIDWORKS is grouped in the Visualize scene as defined by [PartGroupingMode_e](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.PartGroupingMode_e.html)

## VBA Syntax

See [IVisualizeAddinManager2::SaveWithPartGrouping](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IVisualizeAddinManager2~SaveWithPartGrouping.html).

## Remarks

This method allows control over how the model hierarchy is structured in Visualize. You can specify how geometry is grouped.

## See Also

[IVisualizeAddinManager2 Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2.html)
[IVisualizeAddinManager2 Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2026 FCS
