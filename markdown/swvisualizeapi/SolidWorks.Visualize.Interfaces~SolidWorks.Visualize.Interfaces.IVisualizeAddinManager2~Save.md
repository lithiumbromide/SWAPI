---
title: "Save Method (IVisualizeAddinManager2)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IVisualizeAddinManager2"
member: "Save"
kind: "method"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2~Save.html"
---

# Save Method (IVisualizeAddinManager2)

Obsolete. Superseded by [IVisualizeAddinManager2::SaveWithPartGrouping](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2~SaveWithPartGrouping.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Save( _
   ByVal filename As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IVisualizeAddinManager2
Dim filename As System.String

instance.Save(filename)
```

### C#

```csharp
void Save(
   System.string filename
)
```

### C++/CLI

```cpp
void Save(
   System.String^ filename
)
```

### Parameters

- `filename`: Visualize Project file name (***.SVPJ**)

## VBA Syntax

See [IVisualizeAddinManager::Save](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IVisualizeAddinManager~Save.html).

## See Also

[IVisualizeAddinManager2 Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2.html)
[IVisualizeAddinManager2 Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
